# http://learnpythonthehardway.org/book/ex13.html
#-*-coding:cp949

from sys import argv
#sys ���(���̽� ��ũ��Ʈ�� ���޵� ����� �Ű����� ���)���� argv( �� �����ٰ� ���� ��

print("argv = " + str(argv))
script, first, second, third = argv

print ("The script is called: %s" % script)
print ("Your first variable is: %s" % first)
print ("Your second variable is: %s" % second)
print ("Your third variable is: %s" % third)