######################################################
# 함수 선언은 [ def 함수명(parameter) : ] 로 선언한다.
# global 변수를 사용하기 위해서는 변수명 앞에 global을 붙여준다.
######################################################
def f():
    global s
    s = "I love London!"
    print(s)
s = "I love Paris"
print(s)
f()
print(s)
