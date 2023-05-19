import time
from workers.WikiWorker import WikiWorker
from workers.YahooPriceReader import YahooPriceReaderScheduler
from multiprocessing import Queue


def main():
    symbolQ = Queue()
    s1 = time.time()
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    print("Starting Worker to get list of companies from wikipedia")
    # could have done it even without worker as this is just a single network request, will anyways happen sequentially.
    w = WikiWorker(url)
    w.join()
    print(f"Finished wiki worker in {time.time()-s1}")
    print(f"List of companies----->{w.companies}")
    num_yahooSchedulers = 25
    yahooSchedulerThreads = []
    for _ in range(num_yahooSchedulers):
        yahooScheduler = YahooPriceReaderScheduler(symbolQ)
        yahooSchedulerThreads.append(yahooScheduler)

    for company in w.companies:
        symbolQ.put(company)

    s2 = time.time()
    # Its important to put DONE because this is the condition when the schedular breaks of its infinite blocking mode, waiting for a symbol
    for _ in range(num_yahooSchedulers):
        symbolQ.put("DONE")

    for t in yahooSchedulerThreads:
        t.join()

    print(f"Finished in {time.time()-s2}")
    print(f"Sock prices------>{YahooPriceReaderScheduler.COMAPNY_PRICE_DICT}")


if __name__ == "__main__":
    main()
