import random as rd

answer_random_number=rd.randint(1, 100)



       

def finish(attempt):
    result=""
    if attempt<=8:
        result+="천재!"          
    elif attempt>8 and attempt<=15:
        result+="똑똑할지도..?"
    elif attempt>15 and attempt<=20:
        result+="보통입니다."
    else:
        result+="실망이군요.."
    print(f"축하합니다~~! {attempt}번의 시도 끝에 맞추셨군요! 당신은 {result}") 

def game():
    attempt=1   #while 반복문 안에 말고 함수와 반복문 사이에 놓은 이유는 반복되면서 attempt +1을
    while True: #해줘야 하는 것과, attempt=1이라는 것이 서로 충돌하여 오류는 내는 것 같음.
        private_number=int(input(f"{attempt}번째 시도! 숫자를 맞혀보세요!"))
        
        if private_number==answer_random_number:
            finish(attempt)     #함수에서 나온 로컬 변수의 값을 다른 함수로 넘겨줄 때, 옆과 같이 넘겨주고자 하는 함수의 파라미터에
                                #넘겨주면 된다. 
            break
        elif private_number<answer_random_number:
            print("땡! UP!")
        elif private_number>answer_random_number:
            print("땡! DOWN!")
        attempt+=1
              

    
game()


# ***교훈***
# 1. 작업을 진행하기 전에는 항상 코드를 짜기 이전에 노트가 태블릿에 전체적인 개요를 짜놓고 들어가자
# => 그렇지 않으면 코드가 꼬이고, 전역변수와 로컬변수간의 경계가 불분명해지면서 어디서 오류가 생기고 있는지조차 파악하기 힘들다.

# 2. 로컬변수는 함수 안에서, 전역 변수는 함수 밖에서 주로 사용.
#     아직 까지는 전역 변수는 값을 웬만하면 바꾸지 않는 쪽으로 개발해보자.
#     바뀌는 값들을 사용할 때는 로컬변수끼리 파라미터로 받는 것을 고려.
