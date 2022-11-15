
from cryptography.fernet import Fernet

keyF = open('keyenc.txt','r')
key = keyF.read()
keyF.close()

files = input('file to decrpyt : ')
print("******************reading file*********************")
#starting to decrypting
with open(files,'rb') as e:
	data = e.read()
print("******************done reading file*********************")

print("******************decrypting file*********************")
caesar = Fernet(key)
dec = caesar.decrypt(data)
print("******************done decrypting file*********************")

out = input('decrypted file name : ')
print("******************saving decrypted file*********************")
#saving file
with open(out,'wb') as f:
	f.write(dec)
print("******************done saving decrypted file*********************")