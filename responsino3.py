#soal 3. menerima input sebuah tuple yg berisi bilangan bulat dan program akan meghitung berapa banyak bil positif dan negatif

#buat tuple jadi inputan dan otomatis jadi integer
tup = tuple([int(i) for i in input().split()])

positif = 0
negatif = 0

for i in tup:
    if i > 0:
        positif += 1
    elif i < 0:
        negatif += 1
    else:
        positif += 0
        negatif += 0

print("Positif :, {}\nNegatif : {}".format(positif, negatif))

# atau bisa jadi kaya gini

print("Positif :", positif)
print("Negatif :", negatif)
