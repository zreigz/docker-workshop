# Python program to find the factorial of a number using recursion

def recur_factorial(n):
   """Function to return the factorial
   of a number using recursion"""
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)


while(1):
   for i in range (1, 200):
      print("The factorial of",i,"is",recur_factorial(i))
