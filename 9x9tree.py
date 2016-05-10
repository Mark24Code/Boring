print("==== 9x9 Tree ====")

num_array = [i for i in range(1,10)]

num_len = len(num_array)

for i in num_array:
    b = i
    for j in range(1,b+1):
        a = j
        print('{}x{}={}'.format(a,b,a*b),end='\t')
    print('\n')
