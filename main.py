import threading
import time

first_results = []
second_results = []
third_results = []


def first_func(iter_count):
    global first_results
    for x in range(iter_count):
        first_results.append(x ** 2 - x ** 2 + 4 * x - 5 * x + x + x)


def second_func(iter_count):
    global second_results
    for x in range(iter_count):
        second_results.append(x + x)


def third_func(a, b):
    for i in range(len(a)):
        third_results.append(a[i] + b[i])


spent_time = []


def iterations(iter_count):
    start1 = time.time()
    t1 = threading.Thread(target=first_func, args=[iter_count])
    t1.start()
    end1 = time.time()

    t2 = threading.Thread(target=second_func, args=[iter_count])
    t2.start()
    end2 = time.time()

    third_func(first_results, second_results)
    end3 = time.time()

    spent_time.append(end1 - start1)
    spent_time.append(end2 - start1)
    spent_time.append(end3 - start1)


iterations(10000)
print('''
FOR 10,000 ITERATIONS:
''')
print(f'{spent_time[0]} seconds spent for thread-1')
print(f'{spent_time[1]} seconds spent for thread-1 and thread-2')
print(f'{spent_time[2]} seconds spent for all')

spent_time.clear()
iterations(100000)
print('''
FOR 100,000 ITERATIONS:
''')
print(f'{spent_time[0]} seconds spent for thread-1')
print(f'{spent_time[1]} seconds spent for thread-1 and thread-2')
print(f'{spent_time[2]} seconds spent for all')

