age = (2019 - int(input("당신이 태어난 년도를 입력하세요 : ")))

if 26 <= age:
    print("성인")
elif 20 <= age and age <= 26:
    print("대학생")
elif 17 <= age and age <= 20:
    print("고등학생")
elif 14 <= age and age <= 17:
    print("중학생")
else:
    print("초등학생 이하")
