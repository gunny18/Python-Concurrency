import threading
import time


def sleep_time(t):
    time.sleep(t)


def calc_square(n):
    sum_square = 0
    for i in range(n):
        sum_square += i**2
    print(sum_square)

def main():
    s1 = time.time()
    all_threads = []
    print("Starting calc squares")
    for i in range(5):
        t = threading.Thread(target=calc_square, args=((i+2)*1000000,))
        t.start()
        all_threads.append(t)
    for t in all_threads:
        t.join()
    print(f"Finished calc squares in {time.time()-s1}")

    s2 = time.time()
    print("Starting sleep")
    all_threads = []
    for i in range(1, 6):
        t = threading.Thread(target=sleep_time, args=(i,))
        t.start()
        all_threads.append(t)
    for t in all_threads:
        t.join()
    print(f"Finished sleep in {time.time()-s2}")

if __name__ == "__main__":
    main()
