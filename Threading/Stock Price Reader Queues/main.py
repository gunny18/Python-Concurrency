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
    yahooSchedulerThreads = []
    for _ in range(25):
        yahooScheduler = YahooPriceReaderScheduler(symbolQ)
        yahooSchedulerThreads.append(yahooScheduler)

    for company in w.companies:
        symbolQ.put(company)

    s2 = time.time()
    for _ in range(len(yahooSchedulerThreads)):
        symbolQ.put("DONE")


    for t in yahooSchedulerThreads:
        t.join()

    print(f"Finished in {time.time()-s2}")
    




if __name__ == "__main__":
    main()
