#-*-coding:cp949
# http://learnpythonthehardway.org/book/ex6.html
x = "There are %d types of people." % 10
# %d 는 정수부분 표시
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
# #s 는 문자열 표시

print x
print y

print "I said: %r." % x
# %r 은...
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
