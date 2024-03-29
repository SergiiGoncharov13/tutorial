from multiprocessing import cpu_count, Pool
from time import time
import logging
from functools import wraps


def handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        logging.info(f'Function "{func.__name__}" working: {(end - start):} seconds')
        return result
    return wrapper


def factorize(*number):
    result = list()
    for num in number:
        result_list = list()
        result_list.append(num)
        result_number = num
        while True:
            result_number = result_number - 1
            if (num % result_number) == 0:
                result_list.insert(0, result_number)
            if result_number == 1:
                result.append(result_list)
                break
    return result


def cpu_test():
    logging.info(f'Your have {cpu_count()} cores CPU')


@handler
def testing_single():
    a, b, c, d = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]


@handler
def testing_multi():
    with Pool(cpu_count()) as pool:
        a, b, c, d = pool.map(factorize, (128, 255, 99999, 10651060))
    pool.close()
    pool.join()

    assert a == [[1, 2, 4, 8, 16, 32, 64, 128]]
    assert b == [[1, 3, 5, 15, 17, 51, 85, 255]]
    assert c == [[1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]]
    assert d == [[1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]]


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format="%(threadName)s - %(message)s")
    cpu_test()
    testing_single()
    testing_multi()