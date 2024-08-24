# 10이하의 양의 짝수 리스트
num_list=[]
for n in range(10,0,-2):
    num_list.append(n)
print(num_list)

list1=[1, 2, 3, 'apple']
list1.append(4)
print(list1)

score_list=[90, 70, 80]

for index, score in enumerate(score_list):
    score_list[index]+=5
print(score_list)

# ***zip() => 2개 이상의 시퀀스(순서가 있는 자료형 ex) 문자열, 리스트 ..))를 하나의 객체로 묶기 보통은 변수=list(zip())으로 리스트로 만든 것을 변수에 담아 사용한다.
names = ["kim", "lee", "park"]
years = [2000, 1998, 2001]

people_list=list(zip(names, years))
print(people_list)

fruit_list = ["Apple ", " cherry ", "KIWI FRUIT\n"]

real_fruit_list=[n.lower().strip() for n in fruit_list]
print(real_fruit_list)