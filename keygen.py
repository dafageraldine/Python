from cryptography.fernet import Fernet

keyF = Fernet.generate_key()
# keyF = open('code.key','r').read()
# print (keyF)
with open('keyenc.txt','w') as f:
	f.write(keyF.decode('utf-8'))