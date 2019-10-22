from threading import *
import time

n = int(input("masukkan angka: "))
awal = 1
lalu = 1
first = 5
second = 8
_first = 13
_second = 21
hasil = []

class fibo(Thread):
	def run(self):
		global awal, lalu 
		for i in range(n):
			if awal < 5:
				print("thread1", awal)
				hasil.append(awal)				
				jml = awal
				awal = lalu
				lalu = jml+lalu
			else:
				print("to thread2")
				break

class fibo_2(Thread):
	def run(self):
			global first, second
			if n > 4:
				for i in range(n):
					if first < 11:
						print("thread2", first)
						hasil.append(first)
						temp = first
						first = second
						second = temp+second
					else:
						print("to thread3")
						break


class fibo_3(Thread):
	def run(self):
		global first, second, _first, _second
		if n > 4:
			if first > 8:
				for i in range(n-6):
					print("thread3", _first)
					hasil.append(_first)
					_temp = _first
					_first = _second
					_second = _temp+_second
			else:
				print("number not enough")


t1 = fibo()
t2 = fibo_2()
t3 = fibo_3()


t1.start()
time.sleep(1)
t2.start()
time.sleep(1)
t3.start()
time.sleep(1)

print(hasil)
