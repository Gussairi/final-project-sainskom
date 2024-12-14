import numpy as np


def transpose(A):
    hasil = np.transpose(A)
    return hasil

A = []

n = int(input("Masukkan ukuran matriks: "))


print("Matriks A: ")
for i in range(n): 
    row = list(map(int, input(f"Masukkan {n} elemen untuk baris {i+1} (pisahkan dengan spasi): ").split()))
    A.append(row)

A = np.array(A)

print("\n-- Transpose Matriks --")
print("Transpose Matriks A:\n", transpose(A))