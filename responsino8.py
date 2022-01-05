# soal no 8, menghilangkan kata-kata yang disingkat, menghilangkan huruf vokal

kalimat = input().split()
vokal = ['a','i','u','e','o','A','I','U','E','O']

kalimat_baru = []

for kata in kalimat:
    kata_baru = kata
    for huruf in kata:
        if huruf in vokal:
            kata_baru = kata_baru.replace(huruf, "")
    kalimat_baru.append(kata_baru)

print(kalimat_baru)
print(" ".join(kalimat_baru)) #dipisahkan spasi