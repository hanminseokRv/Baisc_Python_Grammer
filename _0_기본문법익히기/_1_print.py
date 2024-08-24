# 줄바꿈 넣는 방법

# 1. print() => 한 줄 띄우기 역할
# 2. print('''하고 싶은말을   => 내가 적은 대로 줄바꿈 적용.
#          적어보아요''' )    
# 3. \n 이용
# Ex)
# print("Hello world!\nNice to meet you") 

# =>    Hello wordl!
#       Nice to meet you


# f-string=>print(f"~")

# 내가 작성한 그대로 print 할 수 있는 방법
# 변수를 넣으려면 {}안에 넣어야 함.

# 숫자팁
# 1. {num:,} => ,는 천 단위마다 쉼표 삽입
# 2. {num:.1f} => .숫자f는 ~번째까지 반올림할 것인가

# 폭 지정 및 0채우기
# 1. {n:숫자} => 숫자만큼의 공백을 만들고 우측 정렬
# 2. {n:0숫자} => 숫자만큼의 공백에 우측 정렬 후 남은 공백 
#                 자리에 0대입

num=1234.5678

print(f"num is {num:,}")
print(f"num is {num:,.1f}")
print(f"num is {num:,.2f}")
