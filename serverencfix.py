############################this project is a python version 2
import socket,zlib,sys
from cryptography.fernet import Fernet

############################making server
ip = '192.168.43.46'
port = 3128
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((ip, port))
s.listen(5)
file = open('recvxxxenc.zip','w')

#############################receiving file from client
conn,addr = s.accept()
print("get connection with ",addr)
file_data = conn.recv(1500)
while(file_data):
	file.write(file_data)
	file_data = conn.recv(1500)
file.close()
print 'file has been received'

#############################decompressing
files = open('recvxxxenc.zip','r').read()
decomp = zlib.decompress(files)

#saving file
save = open('recvxxx.enc','w')
save.write(decomp)
save.close()
print'done decompressing the file'

#############################decrypting
#get the key from keygen.py
keyF = open('code.txt','r')
key = keyF.read()
keyF.close()

#starting to decrypting
with open('recvxxx.enc','r') as e:
	data = e.read()
caesar = Fernet(key)
dec = caesar.decrypt(data)

#saving file
with open('recvxxx.py','w') as f:
	f.write(dec)
print'done decrypting the file'
