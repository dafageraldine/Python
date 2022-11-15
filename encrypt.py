from cryptography.fernet import Fernet

keyF = open('keyenc.txt','r')
key = keyF.read()
keyF.close()

filez = input("file to encrypt : ")

#starting to encrypt the file
print ('---------reading file---------')
with open(filez,'rb') as k:
	data = k.read()
print ('---------done reading file------')

print ('---------encrypting file-------')
caesar = Fernet(key)
encrypted = caesar.encrypt(data)
print ('--------done encrypting--------')

out = input("output encyrpt file : ")

print ('--------saving encrypted file--------')
with open(out,'w') as j:
	j.write(encrypted.decode('utf-8'))

print ('--------done saving the encrypted file-------')