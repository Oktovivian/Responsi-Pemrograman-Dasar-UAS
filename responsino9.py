# soal no 9
'''
penulisan tanpa spasi, namun setiap awal kata harus kapital
huruf A diganti 4
huruf I diganti 1
huruf U diganti |_|
huruf E diganti 3
huruf O diganti 0

note : buatlah beberapa fungsi untuk mempermudah
'''
#tatib awal kata pakai kapital
def tatib_ubah_ke_kapital(kalimat):
    new = []
    for kata in kalimat:
        new.append(kata.replace(kata[0], kata[0].upper())) #ini mengubah index pertama jadi kapital
    return new

def tatib_tanpa_spasi(kalimat):
    return "".join(kalimat)

def tatib_ganti_huruf(kalimat):
    new = []
    for kata in kalimat:
        for huruf in kata:
            if huruf == "A" or huruf == "a":
                kata = kata.replace(huruf, "4")
            elif huruf == "I" or huruf == "i":
                kata = kata.replace(huruf, "1")
            elif huruf == "U" or huruf == "u":
                kata = kata.replace(huruf, "|_|")
            elif huruf == "E" or huruf == "e":
                kata = kata.replace(huruf, "3")
            elif huruf == "O" or huruf == "o":
                kata = kata.replace(huruf, "0")
        
        new.append(kata)
    return new

#main program
kalimat = input().split()
tatib1 = tatib_ubah_ke_kapital(kalimat)
tatib2 = tatib_ganti_huruf(tatib1)
tatib3 = tatib_tanpa_spasi(tatib2)

print(tatib3)