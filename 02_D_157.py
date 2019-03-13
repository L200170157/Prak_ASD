"""1"""
class Pesan(object):
	def __init__(self, sebuahString):
		self.teks = sebuahString
	def cetakIni(self):
		print (self.teks)
	def cetakPakaiHurufKapital(self):
		print(str.upper(self.teks))
	def cetakPakaiHurufKecil(self):
		print(str.lower(self.teks))
	def jumKar(self):
		return len(self.teks)
	def cetakJumlahKarakterku(self):
		print ("Kalimatku mempunyai ", len(self.teks),"karakter")
	def perbarui(self, stringBaru):
		self.teks = stringBaru

	"""a"""
	def apakahTerkandung(self, kata):
		if kata in self.teks:
			return True
		else:
			return False

	"""b"""
	def hitungKonsonan(self):
		vokal = "aiueo"
		counter = 0
		for i in self.teks:
			if i.lower() not in vokal:
				counter+=1
		return counter

	"""c"""
	def hitungVokal(self):
		vokal = "aiueo"
		counter = 0
		for i in self.teks:
			if i.lower() in vokal:
				counter+=1
		return counter

"""2"""
class Manusia(object):
	keadaan = "lapar"
	def __init__(self, nama):
		self.nama = nama
	def ucapkanSalam(self):
		print("Salam, namaku ", self.nama)
	def makan(self, s):
		print("Saya baru saja makan ", s)
	def olahraga(self, k):
		print("Saya baru saja latihan ", k)
		self.keadaan = "lapar"
	def mengalikanDenganDua(self, n):
		return n*2
	    
class Mahasiswa(Manusia):
	def __init__(self,nama,nim,kota,us):
		self.nama = nama
		self.nim = nim
		self.kota = kota
		self.us = us
	def __str__(self):
		s=self.nama+ ", NIM " + str(self.nim)\
		   + " . Tinggal di " + self.kota \
		   + " . Uang saku Rp " +str(self.us)\
		   + " tiap bulannya."
		return s
	def ambilNama(self):
		return self.nama
	def ambilnim(self):
		return self.nim
	def ambilUangSaku(self):
		return self.us
	def makan(self,s):
		print("Saya baru saja makan ", s, "sambil belajar.")
		self.keadaan = "kenyang"
	"""a"""
	def ambilKotaTinggal(self):
		return self.kota
	"""b"""
	def perbaruiKotaTinggal(self, baru):
		self.kota = baru
	"""c"""
	def tambahUangSaku(self, tambah):
		self.us = self.us + tambah
mhs1=Mahasiswa("Naya",222,"Surakarta",500000)
print(mhs1.ambilKotaTinggal())
print(mhs1.perbaruiKotaTinggal("Yogyakarta"))
print(mhs1.ambilKotaTinggal())
print(mhs1.ambilUangSaku())
print(mhs1.tambahUangSaku(100000))
print(mhs1.ambilUangSaku())

"""3"""
class Mahasiswa(Manusia):
	def __init__(self,nama,nim,kota,us):
		self.nama = nama
		self.nim = nim
		self.kota = kota
		self.uang = us
	def __str__(self):
		s=self.nama+ ", NIM " + str(self.nim)\
		   + " . Tinggal di " + self.kota \
		   + " . Uang saku Rp " +str(self.us)\
		   + " tiap bulannya."
		return s
	def ambilNama(self):
		return self.nama
	def ambilnim(self):
		return self.nim
	def ambilUangSaku(self):
		return self.uangSaku
	def makan(self,s):
		print("Saya baru saja makan ", s, "sambil belajar.")
		self.keadaan = "kenyang"
	def ambilKotaTinggal(self):
		return self.kota
	def perbaruiKotaTinggal(self, baru):
		self.kota = baru
	def tambahUangSaku(self, tambah):
		self.us = self.us + tambah
	a = input("Masukkan Nama : ")
	b = input("Masukkan NIM : ")
	c = input("Masukkan Kota Tinggal : ")
	d = input("Masukkan Uang Saku : ")


"""4"""
class Manusia(object):
	keadaan = "lapar"
	def __init__(self, nama):
		self.nama = nama
	def ucapkanSalam(self):
		print("Salam, namaku ", self.nama)
	def makan(self, s):
		print("Saya baru saja makan ", s)
	def olahraga(self, k):
		print("Saya baru saja latihan ", k)
		self.keadaan = "lapar"
	def mengalikanDenganDua(self, n):
		return n*2
class Mahasiswa(Manusia):
	def __init__(self,nama,nim,kota,us, lk = []):
		self.nama = nama
		self.nim = nim
		self.kota = kota
		self.us = us
		self.listkuliah = lk
	def __str__(self):
		s=self.nama+ ", NIM " + str(self.nim)\
		   + " . Tinggal di " + self.kota \
		   + " . Uang saku Rp " +str(self.uangSaku)\
		   + " tiap bulannya."
		return s
	def ambilNama(self):
		return self.nama
	def ambilnim(self):
		return self.nim
	def ambilUangSaku(self):
		return self.uangSaku
	def makan(self,s):
		print("Saya baru saja makan ", s, "sambil belajar.")
		self.keadaan = "kenyang"
	def ambilKotaTinggal(self):
		return self.kota
	def perbaruiKotaTinggal(self, baru):
		self.kota = baru
	def tambahUangSaku(self, tambah):
		self.us = self.us + tambah
	def ambilKuliah(self, ambil):
		self.listkuliah.append(ambil)

m1 = Mahasiswa('Jamil', 234, 'Surakarta', 250000)
print(m1.listkuliah)
print(m1.ambilKuliah("Matematika Diskrit"))

"""5"""
class Mahasiswa(Manusia):
	def __init__(self,nama,nim,kota,us, lk = []):
		self.nama = nama
		self.nim = nim
		self.kota = kota
		self.us = us
		self.listkuliah = lk
	def __str__(self):
		s=self.nama+ ", NIM " + str(self.nim)\
		   + " . Tinggal di " + self.kota \
		   + " . Uang saku Rp " +str(self.uangSaku)\
		   + " tiap bulannya."
		return s
	def ambilNama(self):
		return self.nama
	def ambilnim(self):
		return self.nim
	def ambilUangSaku(self):
		return self.uangSaku
	def makan(self,s):
		print("Saya baru saja makan ", s, "sambil belajar.")
		self.keadaan = "kenyang"
	def ambilKotaTinggal(self):
		return self.kota
	def perbaruiKotaTinggal(self, baru):
		self.kota = baru
	def tambahUangSaku(self, tambah):
		self.us = self.us + tambah
	def ambilKuliah(self, ambil):
		self.listkuliah.append(ambil)
	def hapusListKuliah(self, hapus):
		for x in self.listkuliah:
			if hapus in self.listkuliah:
				self.listkuliah.remove(hapus)
			else:
				print("Maaf mata kuliah tidak ada ada dalam list mata kuliah yang diambil.")

"""6"""
from datetime import date
class Manusia(object):
	keadaan = "lapar"
	def __init__(self, nama):
		self.nama = nama
	def ucapkanSalam(self):
		print("Salam, namaku ", self.nama)
	def makan(self, s):
		print("Saya baru saja makan ", s)
	def olahraga(self, k):
		print("Saya baru saja latihan ", k)
		self.keadaan = "lapar"
	def mengalikanDenganDua(self, n):
		return n*2
class siswaSMA(Manusia):
	def __init__(self, nama, nis, umur, us):
		self.nama = nama
		self.nis = nis
		self.umur = umur
		self.us = us
	def _str_(self):
		s = self.nama + ", NIS " +str(self.nis)\
		    +". Berumur " + str(self.umur)\
		    +". Uang saku Rp. "+str(self.us)\
		    +". tiap harinya."
		return s
	def tahunlahir(self):
		sekarang=date.today().year
		tl = sekarang-self.umur
		return tl

s1=siswaSMA("Sora", 123, 16, 15000)
print(s1.tahunlahir())

"""7"""
class MhsTIF(Mahasiswa):
	"""Class MhsTIF yang dibangun dari class Mahasiswa"""
	def katakanPy(self):
		print("Pyhton is cool")

m4=MhsTIF("Janu", 123, "Sragen", 230000)
print(m4.katakanPy())
print(m4.keadaan)
print(m4.makan("Nasi Goreng"))
print(m4.keadaan)
print(m4.ucapkanSalam())
print(m4.ambilKotaTinggal())
