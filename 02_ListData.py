cities = ["서울", "부산", "인천", "대구", "대전", "광주", "울산", "수원"]

# (시작지점):(끝지점):(index+)
print(cities[0:6], " AND ", cities[-9:]) # 0부터 5까지, 끝에서부터 9개를 순차적으로
print(cities[:])    # 처음부터 끝까지
print(cities[-50:50])   # 끝에서부터 50번째 부터 끝까지 (최대 범위만큼)
print(cities[::2], " AND ", cities[::-1])   # 2칸 단위로, 역으로 슬라이싱

# + 배열 합치기
print(cities + cities)

# len() 배열의 크기
print(len(cities))

# (var) in (list)
print("인천" in cities)   # 해당 list에 "인천"이 있는지 검사

# .append()
cities.append("독도") # list 에 값 추가
print(cities)

# .extent()
cities.extend(["red", "blue"])    # list 에 새로운 list 추가
print(cities)

# .insert()
cities.insert(0, "new서울")   # 해당 index에 새로운 값 추가 (바꾸는거 아님)
print(cities)

# .remove()
cities.remove("서울") # 해당 값을 list에서 지우기
print(cities)

# del
del cities[9:11]    # list의 해당 index 삭제
print(cities)

# 하나의 list 안에 다양한 DataType이 들어갈 수 있다.
cities.sort()   # list를 재정렬하는 명령어
print(cities)

# list는 주소값을 가리킨다.
a = [1,2,3,4,5]
b = [1,2,3,4,5]
print(a == b)       # 값이 같은지 검사
print(a is b)       # 타입(주소)까지 같은지 검사 (같은 요소인지 검사)
