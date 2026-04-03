    #2차방정식의 근의 공식 


#1
def root(a,b,c):
    if b**2 - 4*a*c< 0:             #허수일 시, 값 출력 X 
        return None, None
    else:
        x1 = (-b +(b**2 - 4*a*c)**0.5) / (2*a)
        x2 = (-b -(b**2 - 4*a*c)**0.5) / (2*a)
        return x1,x2

r1,r2 = root(1,2,3)
print(r1,r2)

#2
def root(a,b,c):
    if b**2 - 4*a*c< 0:             #허수일 시, 값 출력 X 
        return None, None
  
    x1 = (-b +(b**2 - 4*a*c)**0.5) / (2*a)
    x2 = (-b -(b**2 - 4*a*c)**0.5) / (2*a)
    return x1,x2

r1,r2 = root(1,2,1)
print(r1,r2)




#1 = #2   if문에서 return으로 함수가 끝남(허수는 모두 필터링되고 실수만 남음)
