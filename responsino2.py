#soal no 2, mencari pemenang dari suatu pemilihan ketua kelas 
# baris pertama adalah n, baris selanjutnya adalah berisi suara, jika ada lebih dari 1 pemenang, maka outputkan voting ulang

peserta_suara = int(input())
suara = input().split()

pemenang = []
for i in range(n+1):
    pemenang.append(0)
