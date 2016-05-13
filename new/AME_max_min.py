a = [91,2,4,5,9,93,665]

def mmax(arr):
    maxv = 0
    for i in arr:
        if i>maxv:
            maxv = i
    return maxv

print(mmax(a))