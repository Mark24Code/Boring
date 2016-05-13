"""
冒泡排序

相邻比较，大的值赋值给右边
对于大值就像气泡会冒上去
"""
import time

a = [9999,100,3,46,6,998,5,4,3,3,54,4949,44,3,3,2,23,23,3,4,5,5,31]

def pop_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = a[j+1],a[j]
    return arr

if __name__ == '__main__':
    print(pop_sort(a))