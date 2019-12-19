### 2-1 숫자형

#### 숫자형 선언

~~~python
>>> a = 123
>>> a = -178
>>> a = 0

>>> a = 1.2
>>> a = -3.45

>>> a = 4.24E10
>>> a = 4.24e-10

>>> a = 0o177
>>> a = 0x8ff
>>> b = 0xABC
~~~



#### 사칙연산

~~~
>>> a + b
>>> a * b
>>> a / b

제곱을 나타내는 연산자
>>> a ** b
>>> 7 % 3
>>> 7 / 4

몫을 반환하는 연산자
>>> 7 // 4

~~~



### 2-2 문자열 자료형

#### 문자열 선언

~~~python
# 문자열 안에 '가 포함될 때 사용
>>> food = "Python's favorite food is perl"
>>> food = 'Python\'s favorite food is perl'

# 문자열 안에 "가 포함될 때 사용
>>> say = '"Python is very easy." he says.'
>>> say = "\"Python is very easy.\" he says."

# 줄바꿈을 위해 \n 사용
>>> multiline = "Life is too short\nYou need python"
# 줄바꿈을 위해 ''' 혹은 """ 사용
>>> multiline = '''
Life is too short
You need python
'''
~~~

- 널 문자: \000



#### 문자열 연산

```python
>>> head = "Python"
>>> tail = " is fun!"
>>> head + tail
'Python is fun!'

>>> print("=" * 50)
>>> head * 2
>>> print("=" * 50)
==================================================
'pythonpython'
==================================================

>>> len(head)
6
```



#### 문자열 인덱싱

파이썬에서 문자열 인덱싱은 C와 크게 다르지 않지만 -1의 경우 circular처럼, 맨뒤로 간다는 점이 다름.

```python
>>> a = "Life is too short, You need Python"
>>> a[0]
'L'
>>> a[12]
's'
>>> a[-1]
'n'
```



#### 문자열 슬라이싱

a[시작 번호:끝 번호] 형태로 나타내며, 그 의미는 시작 <= a < 끝를 뜻하니 주의해야함.

```
>>> a = "Life is too short, You need Python"
>>> a[0:4]
'Life'
>>> a[19:]
'You need Python'
>>> a[:17]
'Life is too short'
>>> a[19:-7]
'You need'
```



#### 문자열 포매팅

문자열 안에 어떤 값을 삽입하는 방법을 뜻함. printf 문법과 많이 비슷함.

```python
>>> "I eat %d apples." % 3
'I eat 3 apples.'

>>> number = 10
>>> day = "three"
>>> "I ate %d apples. so I was sick for %s days." % (number, day)
'I ate 10 apples. so I was sick for three days.'
```

문자열 포맷 코드는 C문법과 같음.

| 코드 | 설명                     |
| ---- | ------------------------ |
| %s   | 문자열                   |
| %c   | 문자 1개                 |
| %d   | 정수                     |
| %f   | 부동소수                 |
| %o   | 8진수                    |
| %x   | 16진수                   |
| %%   | % 문자를 쓰고 싶을 때 씀 |

좌우 공백을 다음과 같이 입력 가능함.

```python
>>> "%10s" % "hi"
'        hi'
>>> "%-10sjane." % 'hi'
'hi        jane.'
```



##### format 함수

```python
#인덱스 항목 사용
>>> "I eat {0} apples".format(3)
'I eat 3 apples'

# 이름 형태
>>> number = 10
>>> day = "three"
>>> "I ate {0} apples. so I was sick for {1} days.".format(number, day)
'I ate 10 apples. so I was sick for three days.'

# 두개 이상
>>> "I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
'I ate 10 apples. so I was sick for 3 days.'

#혼용
>>> "I ate {0} apples. so I was sick for {day} days.".format(10, day=3)
'I ate 10 apples. so I was sick for 3 days.'

#정렬
>>> "{0:<10}".format("hi")
'hi        '
>>> "{0:>10}".format("hi")
'        hi'
>>> "{0:^10}".format("hi")
'    hi    '

#공백 채우기
>>> "{0:=^10}".format("hi")
'====hi===='
>>> "{0:!<10}".format("hi")
'hi!!!!!!!!'
```



##### f 문자열 포매팅

파이썬 3.6 버전부터 생긴 기능으로, 문자열 앞에 f를 붙임으로써 포매팅 기능을 사용함을 명시해주면 아래와 같이 기존 format 함수와 유사하게 사용이 가능함.

```python
>>> age = 30
>>> f'나는 내년이면 {age+1}살이 된다.'
'나는 내년이면 31살이 된다.'
```



#### 문자열 함수

```python
# 문자 세기
>>> a = "hobby"
>>> a.count('b')
2

# 해당 인자 값이 처음 나오는 인덱스 값을 반환, 없을 땐 -1
>>> a = "Python is the best choice"
>>> a.find('b')
14
>>> a.find('k')
-1
# 위와 동일한 기능이지만, 없을 경우 오류를 발생시킴
>>> a = "Life is too short"
>>> a.index('t')
8
>>> a.index('k')

# 문자열 삽입
>>> ",".join('abcd')
'a,b,c,d'

# 대문자
>>> a = "hi"
>>> a.upper()
'HI'

# 소문자
>>> a = "HI"
>>> a.lower()
'hi'

# 공백 지우기
>>> a = " hi "
>>> a.lstrip()
'hi '
>>> a= " hi "
>>> a.rstrip()
' hi'
# 양쪽에 한 칸 이상의 공백을 모두 지움
>>> a = " hi "
>>> a.strip()
'hi'

# 문자열 바꾸기
>>> a = "Life is too short"
>>> a.replace("Life", "Your leg")
'Your leg is too short'

# 문자열 나누기
>>> a = "Life is too short"
>>> a.split()
['Life', 'is', 'too', 'short']
>>> b = "a:b:c:d"
>>> b.split(':')
['a', 'b', 'c', 'd']
```

