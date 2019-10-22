from sys import stdin
for expression in stdin:
    print('%0.2f' % eval(expression))