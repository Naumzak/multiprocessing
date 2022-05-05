import threading
import multiprocessing
import time


def start_func():
    print("Задача одним потоком выполняется:")
    thread_func(1)
    thread_func(int(input('Сколько потоков вы хотите запустиь?\n')))
    print('Время выполнения увеличилось. Значит, они не паралельны')
    process_func(int(input(f'Сколько процессов вы хотите запустиь?(Но не больше {multiprocessing.cpu_count()})\n')))
    print('Время выполнения не изменилось, значит процессы паралельны')

def func1(num):
    start_time = time.time()
    result = 1
    for i in range(num):
        result *= i ** i
    print(time.time() - start_time)


def process_func(num):
    prc_list = []
    for i in range(num):
        prc = multiprocessing.Process(target=func1, args=(800,), name=f"prc-{i}")
        prc.start()
        prc_list.append(prc)

    for i in prc_list:
        i.join()


def thread_func(num):
    thr_list = []
    for i in range(num):
        thr = threading.Thread(target=func1, args=(800,), name=f"thr-{i}")
        thr.start()
        thr_list.append(thr)

    for i in thr_list:
        i.join()


if __name__ == '__main__':
    start_func()
