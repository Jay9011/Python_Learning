########################################################################
# if-else 문은 괄호 없이 조건문, 문장 실행은 콜론(:)
########################################################################
age = int(input("Tell me your age?"))
if age > 20:
    print("Welcome")
    pass
else:
    print("Bye")
########################################################################
# python 에서는 True False 는 대문자로 시작한다.
# python 에서는 not 구문은 not으로 쓴다.
########################################################################
if not(True):
    print("not true")
else:
    print("not false")
########################################################################
# if-elif-else
########################################################################
score = int(input("Write your score?"))
if score >= 90:
    print("over 90")
elif score >= 80:
    print("over 80")
elif score >= 70:
    print("over 70")
########################################################################