import sys

#print (sys.argv)

filename, num1, op, num2 = sys.argv

num1, num2 = int(num1), int(num2)

if op == "+":
    print (num1 + num2)
'''
elif op == "-":
    print (num1 - num2)
'''
