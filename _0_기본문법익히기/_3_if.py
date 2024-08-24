#근무 시간에 따른 급료 계산 코드
#기본 시급 시간 당 10,000원 
# 10시간 이후 시급 시간 당 15,000원

Mark_work_hour=17
Sally_work_hour=9

basic_salary=10000
exced_salary=15000

def cal_salary(work_hour, basic_salary, exced_salary):
    if work_hour<=10:
        return work_hour * basic_salary
    else:
        return 10*basic_salary + (work_hour-10)*exced_salary
    
Mark_salary = cal_salary(Mark_work_hour, basic_salary, exced_salary)
Sally_salary = cal_salary(Sally_work_hour, basic_salary, exced_salary)
print(f"Mark의 이번 주 월급은 {Mark_salary:,}원입니다.")
print(f"Sally의 이번 주 월급은 {Sally_salary:,}원입니다.")




# 주어진 연도의 윤년 여부를 출력하는 코드

# 윤년의 조건
# 1. 연도가 4로 나누어 떨어지는 해는 윤년으로 한다.
# 2. 이 중에서 100으로 나누어떨어지는 해는 평년으로 한다.
# 3. 그 중에 400으로 나누어 떨어지는 해는 다시 윤년으로 둔다.



def leap_year():
    year=int(input("Type year>>>"))
    if (year%4==0 and not year%100==0) or year%400==0:
        print("Leap Year!!")
    else:
        print("Just a year")
        
leap_year()