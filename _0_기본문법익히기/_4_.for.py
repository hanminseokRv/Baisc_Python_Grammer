# **range(start, stop, 간격)** => start이상 stop 미만!!!
# Ex) range(0, 4)=> 0, 1, 2, 3, 4
#     range(5, 0, -2) => 5, 3, 1 숫자를 감소시킬 때는 step을 반드시 음수로 해야 한다.
# ***continue와 break => continue는 조건에 맞는 값을 통과, break는 즉시 반복문 탈출    
# ***for도 else를 사용할 수 있는데, for 반복문이 break로 끊길 경우에는 else 부분이 실행되지 않는다.***
    
    
#예제 0
# 1부터 100까지의 정수의 합을 구하시오
result1=0
for x in range(1, 101):
    result1+=x
print(result1)

# 1부터 100까지의 2의 배수의 합을 구하시오
result2=0
for x in range(2, 101, 2):
    result2+=x
print(result2)

#1부터 100까지의 2 혹은 3의 배수의 합을 구하시오
result3=0
for x in range(1, 101):
    if x%2==0 or x%3==0:
        result3+=x
print(result3)
    

#예제1 
# [a, b] 구간의 정수를 차례로 반복하면서 숫자를 출력하다가 7이 포함된 숫자를 만나면 "Lucky 7"을 출력하고 실행을 중지하고,
#그렇지 않으면 "7 not found"를 출력하세요

a=18
b1=30
b2=26

def detect_7 (a, b):
    for n in range(a, b+1):
        print(n)
        if "7" in str(n):
            print("Lucky 7!!")        
            break
        else:
            print(n)
    else:
        print("7 not found")         #이때 else는 if가 아니라 for 반복문에 붙은 else이고, break로 반복문을 탈출하게 되면 for else 부분은 실행되지 않는다.

detect_7(a, b2)


#중첩 반복문 => for 안에 for 반복문이 한 번 더 들어가는 경우

for i in range(3):
    print("Outer loop", i)
    for j in range(3):
        print("\tInner loop", j)
        
# i, j 둘 다 0, 1, 2반복. i의 0, 1, 2 매 번마다 j 012반복됨. 따라서 중첩 반복문을 쓸 때는 i의 반복문부터 구상하고 j가 어떻게 들어갈지 고민하자.

#예제2 
# 2단~9단 중첩 반복문으로 구구단 만들기

for n in range(2, 10):
    print(str(n)+"단")
    for num in range(1, 9):
        print(f"{n}x{num}={n*num}")
        


#예제3
#[a, b]안의 정수 범위에서 소수를 출력하는 코드를 작성해보시오.



a=int(input("Start>>>"))
b=int(input("End>>>"))

for num in range(a, b+1):
    for x in range(2, num):
        if num%x==0:
            break
    else:
        print(num)
            
            
# *** List Comprehension***  한 줄로 for 반복문의 결과를 list로 나타내기!
# [expression for x in 자료형 if condition] => 왼쪽과 같이 표시한다.

list2=[x*2 for x in [1, 2, 3]]
print(list2)

num_list = ['1', '2', '3']

real_list= [int(n) for n in num_list]
print(real_list)
            

        
            
    
