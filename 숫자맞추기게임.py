from random import *

answer = int(random() * 100) + 1
count = 0
while True:
        count += 1
        number = int(input("1 ~ 100 사이의 숫자를 입력해 주세요: "))
        if number == answer:
                print('정답입니다!')
                print(f'시도횟수는 {count}회 입니다!')
                break
        elif number > answer:
                print('정답보다 큰 숫자입니다.')
        elif number < answer:
                print('정답보다 작은 숫자입니다.')
