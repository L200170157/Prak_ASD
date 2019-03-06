"""1"""
def cetakSiku(x):
	for i in range (1,x+1):
		print ("*"*i)

cetakSiku(5)

"""2"""
def gambarSegiempat(x,y):
	for i in range (x):
		if i==0 or i==x-1:
			print ("@"*y)
		else:
			print ("@"+" "*(y-2)+"@")

gambarSegiempat(4,5)

"""3.a"""
def jumlahHurufVokal(a):
	vokal = 'aiueo'
	counter = 0
	for i in a:
		if i.lower() in vokal:
			counter+=1
	print ((len(a), counter))

jumlahHurufVokal("Surakarta")

"""3.b"""
def jumlahHurufKonsonan(b):
	vokal = 'aiueo'
	counter = 0
	for i in b:
		if i.lower() not in vokal:
			counter+=1
	print ((len(b), counter))

jumlahHurufKonsonan("Surakarta")

"""4"""
def rerata(c):
	counter = 0
	for i in c:
		counter+=i
	return counter/len(c)

print(rerata([1,2,3,4,5]))

"""5"""
from math import sqrt as sq
def apakahPrima(n):
	n=int(n)
	assert n>=0
	primakecil=[2, 3, 5, 7, 11]
	bukanprima=[0, 1, 4, 6, 8, 9, 10]
	if n in primakecil:
		return True
	elif n in bukanprima:
		return False
	else:
		for i in range(2,int(sq(n))+1):
			 if(n%i==0):
				 return False
	return True

print(apakahPrima(17))
print(apakahPrima(97))
print(apakahPrima(123))

"""6"""
def cetakPrima():
	prima=list()
	for i in range(2,1000):
		a=True
		for iter in prima:
			if(i%iter==0):
				a=False
				break
		if(a):
			print(i)
			prima.append(i)
		
cetakPrima()

"""7"""
def faktorPrima(f):
	prima=list()
	for i in range (2,f):
		a=True
		for iter in prima:
			if (i%iter==0):
				a=False
				break
		if a and f%i==0:
			prima.append(i)
	return prima

print(faktorPrima(10))
print(faktorPrima(120))
print(faktorPrima(19))

"""8"""
def apakahTerkandung(a,b):
	return a.lower() in b.lower()

h = "Indonesia tanah air beta"
print(apakahTerkandung('pusaka',h))
print(apakahTerkandung('Indonesia', 'Indonesia Raya Merdeka'))

"""9"""
for i in range (1,101):
	if i%3==0 and i%5==0:
		print ("Python UMS")
	elif i%3==0:
		print ("Python")
	elif i%5==0:
		print ("UMS")
	else:
		print (i)

"""10"""
def selesaikanABC(a,b,c):
	a=float(a)
	b=float(b)
	c=float(c)
	D=(b**2)-(4*a*c)
	if D<0:
		    return "Determinan negatif"
	return "Determinan positif"

print(selesaikanABC(1,2,3))

"""11"""
def tahunKabisat(k):
	if (k%4==0 & k%100==0 & k%400==0):
		return True
	else:
		return False

print(tahunKabisat(2004))
print(tahunKabisat(1896))
print(tahunKabisat(2019))

"""12"""
import random
def tebakAngka():
	a=random.randrange(0,100)
	while(True):
		b=int(input("Masukkan angka: "))
		if (b>a):
			print("Terlalu besar, coba lagi")
		elif(b<a):
			print ("Terlalu kecil, coba lagi")
		else:
			print ("Benar")
			break

print(tebakAngka())

"""13"""
def katakan(a):
	b={"0":"","1":"Se","2":"Dua","3":"Tiga","4":"Empat",
	   "5":"Lima","6":"Enam","7":"Tujuh","8":"Delapan","9":"Sembilan"}
	c={-1:"",-2:"puluh",-3:"ratus",-4:"ribu",
	   -5:"puluh",-6:"ratus",-7:"juta",-8:"puluhjuta",}
	d=str(a)
	e=""
	i=-1
	while i>=-len(d):
		e=b[d[i]]+c[i]+e
		i-=1
	return e

print(katakan(25))

"""14"""
def formatRupiah(n):
	hasil = ""
	x = 0
	for i in str(n)[::-1]:
		if (x<3):
			hasil += i
			x += 1
		else:
			 hasil = hasil +"."+i
			 x = 1
	return "Rp "+hasil[::-1]

			 
print(formatRupiah(45000))
