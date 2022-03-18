import numpy as np
import time
'''
    arange(num)  返回 （0 ~ num-1)之间的整数
'''
def function():
    start1 = time.time()
    arr1 = np.arange(1000000)
    for _ in range(10):
        arr2 = arr1 * 2
    end1 = time.time()

    print("numpy处理对象时间:%f" % (end1 - start1))
    start2 = time.time()
    list1 = list(range(1000000))
    for _ in range(2):
        list2 = list1 * 2
    end2 = time.time()
    print("list处理对象的时间：%f" % (end2 - start2))


def main():
    function()

if __name__ == "__main__":
    main()