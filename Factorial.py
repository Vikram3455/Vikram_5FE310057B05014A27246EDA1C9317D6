#factorial
def fact(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact(n-1)
num=int(input("ENTER A NUMBER OF YOUR FACTORIAL : "))
result=fact(num)
print("THE FACTORIAL OF {} IS {}".format(num,result))