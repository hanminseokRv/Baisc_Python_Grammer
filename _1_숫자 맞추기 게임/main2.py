import random as rd

answer_random_number=rd.randint(1, 100)
print(answer_random_number)


       

def finish(attempt):
    result=""
    if attempt<=10:
        result+="천재!"          
    elif attempt>10 and attempt<=20:
        result+="똑똑할지도..?"
    elif attempt>20 and attempt<=40:
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