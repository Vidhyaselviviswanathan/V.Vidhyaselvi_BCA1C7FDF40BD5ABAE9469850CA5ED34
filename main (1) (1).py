def factorial (n):
   if n==1:
     return 1
   else: 
     return n * factorial(n-1)
num=int(input("enter any number:"))
if num<0:
  print("the factorial does not exist for negative number")
elif num ==0:
  print("the factorial of 0 is 1")
else:
  print("the factorial of ",num,"is ", factorial (num))
  