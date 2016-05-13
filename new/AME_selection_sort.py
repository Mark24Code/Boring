"""
选择排序：

从外循环开始，第一个元素，依次和所有元素比较，选出最小值，交换位置
依次循环所有元素
最后获得完整顺序
"""
a = [100,3,46,6,998,5,4,3,3,54,4949,44,3,3,2,23,23,3,4,5,5,31]

def selection_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr
print(selection_sort(a))



def eff_selection_sort(arr):
    '''
    用num，index储存最小值
    在最后结束后，进行一次换位
    提高效率
    '''
    for i in range(len(arr)-1):
        num = arr[i]
        index = i
        for j in range(i+1,len(arr)):
            if num>arr[j]:
                num = arr[j]
                index = j
                # arr[i],arr[j] = arr[j],arr[i]
        if index != i:
            arr[i],arr[index] = a[index],a[i]
    return arr

print(eff_selection_sort(a))