# 문자열을 표현하는 4가지 방법
str1 = "hello"
str2 = 'hello'
str3 = """hello"""
str4 = '''hello'''

# 문자열 내 따옴표 쓸 경우 백슬래쉬를 이용
str5 = "\"do you know \'bts\'?\""

# 문자열 더하기(Concatenation)
head = "Python"
tail = " is fun!"
plus = head + tail

# 문자열 곱하기(반복)
multiply = head*2

# 문자열 길이(length)
length = len(head)

# 문자열 인덱싱
a = "Lfie is too short, you need Python"
    ### a[0] : 'L'    -> 맨 처음 문자
    ### a[12] : 's'
    ### a[-1] : 'n'   -> 맨 마지막 문자
    ### a[-0] : 'L'   -> 맨 처음 문자

#문자열 슬라이싱
a = "Lfie is too short, you need Python"
    ### b = a[0] + a[1] + a[2] + a[3] : 'Life'
    ### b = a[0:4] : 'Life'
    ### b = a[19:] : 'You need Python'     -> 끝 번호 생략하면 끝까지


# 파이썬에서 문자열은 변경 불가능(immutable)
# 적절히 슬라이싱을 이용해서 바꿔야함
# 아래 'i' 를 'y'를 바꾸는 방법
a = "Pithon"
b = a[:1] + 'y' + a[2:]


# 문자열 포매팅(포맷코드)
a = 'i am %dyears old' % 27     # %d, %s, %f 포매팅
a = ' %d + %s = %d ' %(1,"2",3) # 다중 포매팅
a = "%0.6f" % 3.141234          # 여섯 째자리

# 문자열 포매팅(format 함수)
a = "{0} plus {1} = {2}".format("1",2,1+2)
a = "i am {name} and {age}".format(name="chulmin", age = 27)


# 문자열 정렬
a = "{0:<10}".format("hi")      #'hi        '
a = '{0:>10}'.format("hi")      #'        hi'
a = '{0:^10}'.format("hi")      #'    hi    '
a = '{0:=^10}'.format("hi")     #'====hi===='


#문자열 관련 함수들
a = 'apple is delicious'
a.count('p')    # 'p'의 개수 리턴
a.find('p')     # 'p'의 첫 등장 위치 리턴(0시작, 없으면 -1)
a.index('p')    # find와 동일, 찾는 문자 없으면 오류 발생
",".join(a)     # a문자열 각각 문자 사이에 ',' 삽입 -> 'a,p,p,l,e'
a.upper()       # 대문자로 변환된 문자열 리턴
a.lower()       # 소문자로 변환된 문자열 리턴
a.lstrip()      # 왼쪽 공백 지움('  hi' -> 'hi')
a.rstrip()      # 오른쪽 공백 지움 문자열 리턴
a.strip()       # 양쪽 공백 지운 문자열 리턴
a.replace('apple','cherry') # (바뀔, 바꿀, [바꿀횟수]) 바꿀 횟수 미지정시 모두 바꾼 후 리턴

a.split()
p = "ching,chang,chong".split(',')
# 인자 없을 경우 공백(스페이스, 탭, 엔터 등)으 기준으로 문자열을 나누어 준다
# 인자 있을 경우 그 문자열을 기준으로 나누어 리스트 형태로 리턴!
# ['apple', 'is', 'delicious'] -> 문자열 리스트가 만들어진 것임!
# p[0] : 'ching', p[1] : 'chang'


