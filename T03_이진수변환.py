decimal = int(input("변환하고자 하는 십진수 : "))
result = ''
while (decimal > 0):
    remainder = decimal % 2
    decimal = decimal // 2
    result = str(remainder) + result
print(result)
