Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("hello world")
hello world
>>> print(1)
1
>>> print("1")
1
>>> print("I'm zsy")
I'm zsy
>>> print('I'm zsy')
      
SyntaxError: invalid syntax
>>> print('I\'m zsy')
I'm zsy
>>> print('apple'+'4')
apple4
>>> print("apple + 4")
apple + 4
>>> print("'apple'+'4'")
'apple'+'4'
>>> print('apple'+str(4))
apple4
>>> print(1+2)
3
>>> print('1+2')
1+2
>>> print("1+2")
1+2
>>> print('1'+2)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print('1'+2)
TypeError: can only concatenate str (not "int") to str
>>> print(str'1'+2)
SyntaxError: invalid syntax
>>> print(str('1')+2)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(str('1')+2)
TypeError: can only concatenate str (not "int") to str
>>> print(2+1)
3
>>> print('1'+2)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print('1'+2)
TypeError: can only concatenate str (not "int") to str
>>> print(str('1')+2)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(str('1')+2)
TypeError: can only concatenate str (not "int") to str
>>> print(int('1')+2)
3
>>> print('1.2+2')
1.2+2
>>> print()1.2+2
SyntaxError: invalid syntax
>>> print(1.2+2)
3.2
>>> print(int('1.2')+2 )
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(int('1.2')+2 )
ValueError: invalid literal for int() with base 10: '1.2'
>>> print(float('1.2')+2)
3.2
>>> 
