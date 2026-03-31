# 3-6
for i in range(5):
    print('Hello, Python')

for i in range(5):
    print(i)
    

#3-7
a=list(range(0,101,2))
print(a)

b=list(range(1,101,2))
print(b)

c=list(range(-99,0))
print(c)


#3-8
s=0
for i in range(0,101):
    s= s+i
print(s)

a=0
for j in range(0,101,2):
    a=a+j
print(a)

f=0
for k in range(1,101,2):
    f=f+k
print(f)


#3-9


for i in range(-7,0):
    print(' '*-i+ '#')
