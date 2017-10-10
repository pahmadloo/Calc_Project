"""
Simple python calculator
"""
import sys

#print (sys.argv)

filename, num1, op, num2 = sys.argv

num1, num2 = int(num1), int(num2)

if op == "+":
    print (num1 + num2)

elif op == "-":
    print (num1 - num2)

elif op == "x":
    #in bash (for git) * means all files, so cannot
    print (num1 * num2)

elif op == "/":
    print (num1 - num2)

else:
    print ("Error in input")
    break

print ("Done")

#End of file
#New end of file
