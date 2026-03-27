for i in range(2,10):
    for j in range(1,10):
        print('{}*{}={:2d}'.format(i,j,i*j),end=' ')
    print()


n=11
for i in range(n):
    st=' '
    for j in range(i):
        st= st+ ' '
    print(st+'#')

n=12
for i in range(n):
    print(' '*i+'#'*i)


n=int(input('수 입력:'))       #<<코드 최적화 방안: False 한번 뜬 시점에서 break
is_prime=True
for num in range(2,n):
    if n % num == 0:
        is_prime=False
    
    print(n,'is prime:', is_prime)
