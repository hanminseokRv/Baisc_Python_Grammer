# input()은 사용자가 입력한 값을 직접 받을 수 있는 함수.
# input()값을 변수로 받아 자주 이용한다.

# a= input("어근>>")
# b=input("접사+조사>>")
# print(f"'안녕하세요'에서 어근은 {a}이고, 접사 및 조사는 {b}입니다.")

answer='zebra'
print("Which animal has strips of white and black color in Africa savana?")


while True:
    word=input("Answer>>>")
    if answer==word:
        print("Correct!")
        break
    else:
        print("Wrong!")

