import random as rd

answer_random_number=rd.randint(1, 100)
print(answer_random_number)

attempt=1

    
def case():
    global attempt
    if attempt<=10:
        print("천재!")
    elif attempt>10 and attempt<=20:
        print("똑똑할지도..?")
    elif attempt>20 and attempt<=30:
        print("보통")
    elif attempt>30 and attempt<=50:
        print("아쉽네요..")
    else:
        print("바보")



def real_game(attempt):
    while True:
        private_number=int(input("숫자를 맞혀보아요!>>>"))
        
        if private_number!=answer_random_number:
            print("땡! 다시 입력하세요!")
            attempt+=1
        else:
            case()
            return attempt



real_game(attempt)