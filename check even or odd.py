def evenOdd(n):
     
    # if remainder is 0 then num is even
    if(n==0):
        return True
       
    # if remainder is 1 then num is odd
    elif(n==1):
        return False
    else:
        return evenOdd(n-2)
       
num=33
 
if(evenOdd(num)):
    print(num,"num is even")
else:
    print(num,"num is odd")