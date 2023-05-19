import time
from workers.SumSquareWorker import SumSquareWorker
from workers.SleepWorker import SleepWorker

def main():
    s1 = time.time()
    print("Starting sum square workers")
    all_workers = []
    for i in range(5):
        w = SumSquareWorker((i+2)*1000000)
        all_workers.append(w)
    for w in all_workers:
        w.join()
    print(f"Finished sum square worker in {time.time()-s1}")

    s2 = time.time()
    print("Starting sleep workers")
    all_workers = []
    for i in range(1,6):
        w = SleepWorker(i)
        all_workers.append(w)
    for w in all_workers:
        w.join()
    print(f"Finished sleep work in {time.time()-s2}")



if __name__ == "__main__":
    main()