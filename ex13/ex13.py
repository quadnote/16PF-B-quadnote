# http://learnpythonthehardway.org/book/ex13.html
#-*-coding:cp949

from sys import argv
#sys 모듈(파이썬 스크립트에 전달된 명령행 매개변수 목록)에서 argv( 를 가져다가 쓰는 것

print("argv = " + str(argv))
script, first, second, third = argv

print ("The script is called: %s" % script)
print ("Your first variable is: %s" % first)
print ("Your second variable is: %s" % second)
print ("Your third variable is: %s" % third)