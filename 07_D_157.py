import re
print("NOMOR 1")

tes = open("Indonesia.txt", "r")
teks = tes.read()
tes.close()

print(re.findall(r'me\w+', teks.lower()))

print("NOMOR 2")

tes = open("Indonesia.txt", "r")
teks = tes.read()
tes.close()

print(re.findall(r'di\w+', teks.lower()))

print("NOMOR 3")

tes = open("Indonesia.txt", "r")
teks = tes.read()
tes.close()

print(re.findall(r'di \w+', teks.lower()))

print("NOMOR 4")

tes = open('berkas.html', 'r', encoding='latin1')
teks = tes.read()
tes.close()

cari = re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>', teks)
list = []
for i in cari:
    a = (i[0],float(i[4]))
    list.append(a)
print(list)
