from cryptography.fernet import Fernet

keyF = open('code.txt','r')
key = keyF.read()
keyF.close()

#starting to encrypt the file
with open('zadig.mp4','r') as k:
	data = k.read()
caesar = Fernet(key)
encrypted = caesar.encrypt(data)
print 'done encrypting'
with open('000.enc','w') as j:
	j.write(encrypted)
print 'done saving the encrypted file'

with open('000.enc','r') as e:
	data = e.read()
caesar = Fernet(key)
dec = caesar.decrypt(data)

#saving file
with open('000.mp4','w') as f:
	f.write(dec)
print'done decrypting the file' 