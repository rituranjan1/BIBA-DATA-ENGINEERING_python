n= int(input("enter a number"))
m=n
rev=0
while (n >0):
   r= n%10

   n=n//10
   rev=rev*10+r

if m==rev:
    print("number is palindrome")
else:
    print("number is not palindrome")

