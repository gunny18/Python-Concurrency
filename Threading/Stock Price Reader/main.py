import time
from workers.WikiWorker import WikiWorker
from workers.YahooPriceReader import YahooPriceReader


def main():
    s1 = time.time()
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    print("Starting Worker to get list of companies from wikipedia")
    # could have done it even without worker as this is just a single network request, will anyways happen sequentially.
    w = WikiWorker(url)
    w.join()
    print(f"Finished wiki worker in {time.time()-s1}")
    print(f"List of companies----->{w.companies}")

    s2 = time.time()
    print("Starting the yahoo price reader work")
    all_workers = []
    for c in w.companies:
        y = YahooPriceReader(c)
        all_workers.append(y)
    for y in all_workers:
        y.join()
    print(f"Finished Yahoo Price Work in {time.time()-s2}")
    print(f"Company stock prices---->{YahooPriceReader.COMPANY_PRICE}")




if __name__ == "__main__":
    main()
