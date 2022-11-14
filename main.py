import random

lettersAndSymbols = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','!','@','#','$']

password = ""

for x in range(16):
    password = password + random.choice(lettersAndSymbols)[0]
    
print("Your password is:", password)
