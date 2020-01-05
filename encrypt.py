message=input('Enter the message:')
alphabet=('abcdefghijklmnopqrstuvwxyz0123456789+-*/!@#$%^&')
key=5
encrypt=''
decrypt=''


for i in message:
    position=alphabet.find(i)
    newposition=(position+5)%47
    encrypt+=alphabet[newposition]
print(encrypt)


for i in encrypt:
    pos=alphabet.find(i)
    newpos=(pos-5)%47
    decrypt+=alphabet[newpos]
print(decrypt)