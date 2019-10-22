
from cryptography.fernet import Fernet
keyF = open('code.txt','r')
key = keyF.read()
keyF.close()

#starting to decrypting
with open('000.enc','r') as e:
	data = e.read()
caesar = Fernet(key)
dec = caesar.decrypt(data)

#saving file
with open('000.mp4','w') as f:
	f.write(dec)
print'done decrypting the file'