def pop_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = a[j+1],a[j]
    return arr

a = [100,3,46,6,998,5,4,3,3,54,4949,44,3,3,2,23,23,3,4,5,5,31]

def easy_find(arr,key):
    res = []
    for index in range(len(arr)):
        if arr[index] == key:
            res.append(index)
    if res:
        if len(res)==1:
            return res[0]
        else:
            return res
    else:
        return -1

# print(easy_find(a,998))

# sort_a = pop_sort(a)
# print('sort_a')
# print(sort_a)
sort_a = [2, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 6, 23, 23, 31, 44, 46, 54, 100, 998, 4949]
sort_b = [1,2,3,4,5]
def b_find(arr,key):
    min_index = 0
    max_index = len(arr)-1
    mid_index = len(arr)//2
    while arr[mid_index] != key:
        if(key>arr[mid_index]):
            min_index = mid_index+1
        elif(key<arr[mid_index]):
            max_index = mid_index-1

        mid_index = (min_index+max_index)//2

        if(max_index<min_index):
            return -1
    return mid_index

def b_find2(arr,key):
    min_index = 0
    max_index = len(arr)-1
    mid_index = len(arr)//2
    #也OK这是思路II
    while max_index>=min_index:
        if(key == arr[mid_index]):
            return mid_index
        elif(key>arr[mid_index]):
            min_index = mid_index+1
            mid_index = (min_index+max_index)//2
        elif(key<arr[mid_index]):
            max_index = mid_index-1
            mid_index = (min_index+max_index)//2
    return -1


# print(b_find(sort_b,4))
# print(b_find2(sort_b,4))

def b_think(arr,key):
    min_index = 0
    max_index = len(arr)-1
    mid_index = len(arr)//2

    while max_index>=min_index:
        if key == arr[mid_index]:
            return mid_index
        elif key>arr[mid_index]:
            min_index = mid_index+1
            mid_index = (min_index+max_index)//2
        elif key<arr[mid_index]:
            max_index = mid_index-1
            mid_index = (min_index+max_index)//2
    return -min_index-1

sort_b = [1,2,3,4,5]
print(b_think(sort_b,6))

# def insert_b(arr,b):
#     insert_index = b_think(arr,b)
#     return arr.insert(insert_index,b)
# insert_b(sort_b,1)
# print(sort_b)