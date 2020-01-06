message=input('Enter the message:')
letters=('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-*/!@#$%^&<>?')
key=5
encrypt=''
decrypt=''


for letter in message:
    if letter in letters:
          
        
        position=letters.find(letter)
        newposition=(position+5)%76
        encrypt+=letters[newposition]
    else:
        encrypt += letter
print(encrypt)


for letter in encrypt:
     if letter in letters:
        
        pos=letters.find(letter)
        newpos=(pos-5)%76
        decrypt += letters[newpos]
     else:
        decrypt += letter

print(decrypt)