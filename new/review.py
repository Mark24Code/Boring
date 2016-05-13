a=[12,4,5,23,34,1,213,123,23,4,4,5,6,6,7]

def selection_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]

    return arr


print(selection_sort(a))


def pop_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr


print(pop_sort(a))

sort_a = [1, 4, 4, 4, 5, 5, 6, 6, 7, 12, 23, 23, 34, 123, 213]

def half_find(arr,key):
    min_index = 0
    max_index = len(arr)-1
    mid_index = len(arr)//2
    while max_index>=min_index:
        if arr[mid_index]>key:
            max_index = mid_index-1
            mid_index = (min_index+max_index)//2
        elif arr[mid_index]<key:
            min_index = mid_index+1
            mid_index = (min_index+max_index)//2
        elif arr[mid_index] == key:
            return mid_index
    return -1

print(half_find(sort_a,1235))