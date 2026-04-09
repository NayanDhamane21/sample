n=int(input("enter first number"))
n2=int(input("enter second number"))
operator=input("enter operator ( +. -. *, /, )")
if(operator=="+"):
  print(n+n2)
elif(operator=="-"):
  print(n-n2)
elif(operator=="*"):
  print(n*n2)
elif(operator=="/"):
  print(n/n2)
else:
  print("invalid input")
