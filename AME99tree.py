for i in range(1,10):
    b = i
    for j in range(1,b+1):
        a = j
        print('{}x{}={}'.format(a,b,a*b),end='\t')
    print('')