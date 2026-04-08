


'''
set1={1,2,3,3}         # 집합: 중복값 제외
print(set1)

set2={0,5,2,2,4,1}     # 오름차순으로 정렬됨 
print(set2)

set3={1,2,3,4}
set4={2,4,6,7}

set5=set3.union(set4)  # union(setX): X집합과의 합집합  (= set3|set4)
print(set5)

set5=set3|set4
print(set5)
'''


set3={1,2,3,4}
set4={2,4,6,7}

'''
set5=set3-set4  # 차집합      = set3.differnce(set4)      차집합은 순서에 따라 다르게 출력됨(순서에 유의)
print(set5)
'''

set5=set3.intersection(set4)  # 교집합  = set3 & set4
print(set5)
