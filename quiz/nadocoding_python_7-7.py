# 나도코딩 파이썬 강의(https://youtu.be/kWiCuklohdY?t=8917) 7-7 퀴즈 풀이
def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21


height, gender = input("키(cm)와 성별(남자, 여자)을 입력해 주세요: ").split()
standard_weight = std_weight(int(height) / 100, gender)
print(f"키 {height}cm {gender}의 표준 체중은 {standard_weight:.2f}입니다.")
