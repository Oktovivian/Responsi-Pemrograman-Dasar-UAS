# soal no 7, program otomatis membuat email, baris pertama merupakan nilai N yang menyatakan banyaknya pegawai, baris berikutnya adalah nama depan, nama belakang, dan kode unik, dengan akhiran email adalah @informatika.com
N = int(input())
domain = "@informatika.com"

for i in range(N):
    masukan = input().split() #[0] nama depan, [1] nama belakang, [2] kode unik
    
    email = ""
    for i in range(len(masukan)):
        email = email + masukan[i].lower()
    
    email = email + domain

    print(email)
