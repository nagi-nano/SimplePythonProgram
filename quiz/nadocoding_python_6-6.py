# 나도코딩 파이썬 강의(https://youtu.be/kWiCuklohdY?t=8917) 6-6 퀴즈 풀이
from random import randint

customer_time = [randint(5,50) for i in range(50)]
customer_count = 0
for i in range(50):
    if 5 <= customer_time[i] <= 15:
        customer_count += 1
        customer_text = 'O'
    else:
        customer_text = ' '

    print(f'[{customer_text}] {i+1}번째 손님 (소요시간 : {customer_time[i]}분)')

print(f"총 탑승 승객 : {customer_count} 분")
