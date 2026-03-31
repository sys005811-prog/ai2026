
n=3
for i in range(1,n):
    print(' '*(n-i)+'*'*(2*i)+' '*(n-i)+' '*(n-i)+'*'*(2*i))
a=6
for j in range(a-1,0,-1):
    print(' '*(a-j)+'*'*(2*j))

n=7
for i in range(3,n):
    print('   '*3+' '*(n-i)+'*'*(2*i)+' '*(n-i)+' '*(n-i)+'*'*(2*i))
a=14
for j in range(a-1,0,-1):
    print('   '*3+' '*(a-j)+'*'*(2*j))


n=10
for i in range(3,n):
    print('   '*10+' '*(n-i)+'*'*(2*i)+' '*(n-i)+' '*(n-i)+'*'*(2*i))
a=20
for j in range(a-1,0,-1):
    print('   '*10+' '*(a-j)+'*'*(2*j))

n=15
for i in range(3,n):
    print('   '*20+' '*(n-i)+'*'*(2*i)+' '*(n-i)+' '*(n-i)+'*'*(2*i))
a=30
for j in range(a-1,0,-1):
    print('   '*20+' '*(a-j)+'*'*(2*j))
