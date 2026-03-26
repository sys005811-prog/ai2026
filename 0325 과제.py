# 5-1

list_a = [2, 4, 6, 8, 10]
print('even_list = ', list_a)

list_a = [i for i in range(1, 11) if i % 2 == 0]
print('even_list = ', list_a)

nations = ['Korea', 'China', 'India', 'Nepal']
print('nations = ', nations)

friends = ['영준','준영','일우' ,'수홍','운하']
print('friends = ', friends)

string = list('XYZ')
print('string = ', string)


# 5-2

prime_list = [ 2,3,5,7]
print('prime_list의 첫 원소: ', prime_list[0])
print('prime_list의 마지막 원소: ', prime_list[3])
print('prime_list의 마지막 원소: ', prime_list[-1])



nations = ['Korea', 'China', 'Russia', 'Malaysia']
print('nations의 첫 원소', nations[0])
print('nations의 마지막 원소', nations[3])
print('nations의 마지막 원소', nations[len(nations) -1])



# 5-3

prime_list= [2, 3, 5, 7]
print('소수 목록: ', prime_list)

prime_list.append(11)
print('추가 후 소수 목록: ', prime_list)

print('삭제 전 소수 목록: ', prime_list)
prime_list.remove(3)
print('삭제 후 소수 목록: ', prime_list)

nations = ['Korea', 'China', 'Russia', 'Malaysia']
print('국가 목록', nations)
nations.append('Nepal')
print('추가 후 국가 목록', nations)

a=input('국가명:')
if a in nations:
    print(a,'는(은) 국가 목록에 있습니다.')
else:
    print(a,'는(은) 국가 목록에 없습니다.')


# 5-4

prime_list = [2,3,5,7]
print('1에서 10까지의 소수:', prime_list)
print('최솟값:', min(prime_list))
print('최댓값:', max(prime_list))
print('합계:', sum(prime_list))
print('평균:', sum(prime_list)/len(prime_list))

nations = ['Korea', 'China', 'Russia', 'Malaysia']
print('국가 목록', nations)
print('사전에 가장 먼저 나오는 나라:', min(nations))
print('사전에 가장 뒤에 나오는 나라:', max(nations))


# 5-5

a=[1,2,3]
b=[10,20,30]
print(a)
print(b)
a.append(b)
print(a)

a=[1,2,3]
b=[10,20,30]
a.extend(b)
print(a)

nlist=[1,2,3,4,5,6,7,8,9,10]
nlist.insert(0,0)
print(nlist)

nlist.reverse()
print(nlist)


print('마지막 원소 = ', nlist.pop())
print(nlist)


