# soal 6, buatlah program yang baris pertama menerima sebuah kalimat dan baris keduanya menerima beberapa kata. hitunglah banyaknya frekuensi tiap kata tersebut pada kalimat tadi. jika kata tidak ada outputkan "None"

kalimat = input().split()
kata = input().split()

dict6 = {}

for word in kalimat:
    if word in dict6:
        dict6[word] += 1
    else:
        dict6[word] = 1

for i in kata:
    print(dict6.get(i), end=" ")