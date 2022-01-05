#soal no 1, menghitung rata-rata dengan pembulatan tiga angka

#input dan casting
bilangan = input().split()
jumlah = 0
for angka in bilangan:
    intangka = int(angka)
    jumlah += intangka

#banyaknya item
rerata = jumlah / len(bilangan)
print("{:.3f}".format(rerata))