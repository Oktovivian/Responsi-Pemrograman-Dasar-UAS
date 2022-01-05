# program akan terus meminta inputan, kemudian program meminta 2 bil bulat a dan b, outputnya adalah potongan tuple dari indeks ke a hingga ke b

tuple = tuple([i for i in input().split()])

a = int(input())
b = int(input())

#b+1 karena python hanya akan melihat dari b-1
slicing_tuple = tuple[a:b+1]
print(slicing_tuple)