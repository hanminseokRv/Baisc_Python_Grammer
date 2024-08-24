import random as rd

answer_random_number=rd.randint(1, 100)
attempt=1

def real_game():
    check_answer(private_number, answer_number):
    
    

def case():
    if attempt<=10:
        return "천재!"
    elif attempt>10 and attempt<=20:
        return "똑똑할지도..?"
    elif attempt>20 and attempt<=30:
        return "보통"
    elif attempt>30 and attempt<=50:
        return "아쉽네요.."
    else:
        return "바보"

    


def check_answer(private_number, answer_number)
    private_number=int(input(f"{attempt}번째 시도! 숫자를 맞혀보아요!>>>"))
    answer_number=answer_random_number
    case=case()
    if private_number==answer_number:
        print(f"정답입니다~~!! {attempt}번만에 통과한 당신은 {case}")
    else:
        print("땡!")
        attempt+=1


real_game()