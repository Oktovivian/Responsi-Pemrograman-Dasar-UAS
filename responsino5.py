# soal no 5 (set), buatlah program yang akan menampilkan elemen dari set c yang merupakan hasil a gabung b. program juga akan menampilkan elemen hasil b iris c

'''
c = a gabung b
d = b iris c
'''

set_a = set([int(i) for i in input().split()])
set_b = set([int(i) for i in input().split()])

set_c = set_a | set_b
'''
set_c = set(set_a)
for i in set_b:
    if i not in set_a:
        set_c.add(i)
'''
set_d = set_b & set_c

'''
set_d = set()
for i in set_b:
    if i not in set_c:
        set_d.add(i)
'''
print("gabung", set_c)
print("iris", set_d)



