n=int(input("Input the number of rows: "))
for i in range(1, n):
    print(' '*n, end='') 
    print('* '*(i)) 
    n-=1