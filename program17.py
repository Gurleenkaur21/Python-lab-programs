 #WAP to print Division Exception Handling

try:
 a=int(input())
 b=int(input())
 print(a/b)
except ZeroDivisionError:
 print("Cannot divide by zero")