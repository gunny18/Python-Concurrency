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
    print("Starting clac square task")
    for i in range(5):
        calc_square((i+2)*1000000)
    print(f"Calc square finished in time {time.time()-s1}")

    s2 = time.time()
    print("Starting sleep task")
    for i in range(1, 6):
        sleep_time(i)
    print(f"Finished sleep task in {time.time()-s2}")


if __name__ == "__main__":
    main()
