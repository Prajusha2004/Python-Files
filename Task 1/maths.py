a=int(input("Enter First Number:\n"))
b=int(input("Enter Seccond Number:\n"))
sum=a+b
if (a>b):
  diff=a-b
else:
  diff=b-a
if (a==0 or b==0):
  mult=0
else:
  mult=a*b
if (b!=0):
  div=a//b
  div1=a/b
  div2=a%b
else:
  print("Division is invalid!")