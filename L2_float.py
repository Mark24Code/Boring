import math
def almost_equal(x,y,places = 7):
    return round(abs(x-y),places) == 0


res = almost_equal(sum(0.1 for i in range(10)),1.0)

print(res)

def getF(x):
    res = math.sqrt(x+1)-math.sqrt(x)
    return res

def getF2(x):
    res = math.sqrt(x+1)+math.sqrt(x)
    return res
print(getF(5))

print(1/getF2(5))