############################this project is a python version 2
import socket,zlib,sys
from cryptography.fernet import Fernet

############################connect to server
ip = '127.0.0.1'
port = 3128
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,port))
print'connected to the server'

############################encrypting
#get the key from keygen.py
keyF = open('code.txt','r')
key = keyF.read()
keyF.close()

#starting to encrypt the file
with open('a.jpeg','r') as k:
	data = k.read()
caesar = Fernet(key)
encrypted = caesar.encrypt(data)
print 'done encrypting'

#saving encrypted file
with open('xxx.enc','w') as j:
	j.write(encrypted)
print 'done saving the encrypted file' 

############################compressing
file = open('xxx.enc','r').read()
print 'Raw size : ',sys.getsizeof(file)
compressed = zlib.compress(file,9)
print 'compressed size :',sys.getsizeof(compressed)
print 'done compressing'

#saving compressed file
save = open('xxxenc.zip','w')
save.write(compressed)
save.close()
print'done saving the compressed file'

############################sending the file to server
files = open('xxxenc.zip','r')
file_data = files.read(1500)
while (file_data):
	s.send(file_data)
	file_data = files.read(1500)
print 'data has been transmitted succesfully'
s.close()