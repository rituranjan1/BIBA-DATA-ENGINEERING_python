s = 'geeksforgeeks'
# Using for loop 
for letter in s: 
  
    print(letter) 
    if letter == 'e' or letter == 's': 
        break
  
print("Out of for loop") 
print() 
  
i = 0
  
# Using while loop 
while True: 
    print(s[i]) 
    if s[i] == 'e' or s[i] == 's': 
        break
    i += 1
  
print("Out of while loop")
