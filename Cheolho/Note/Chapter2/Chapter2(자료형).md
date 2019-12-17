## 2-1 숫자형

숫자형 선언

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



사칙연산

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



## 2-2 문자열 자료형

문자열 선언

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



문자열 연산

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



문자열 인덱싱과 슬라이싱

