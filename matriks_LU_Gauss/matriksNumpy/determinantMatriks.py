import numpy as np


def determinant(A):
    hasil = np.linalg.det(A)
    return hasil


A = []
B = []

n = int(input("Masukkan ukuran matriks: "))


print("Matriks A: ")
for i in range(n): 
    row = list(map(int, input(f"Masukkan {n} elemen untuk baris {i+1} (pisahkan dengan spasi): ").split()))
    A.append(row)

A = np.array(A)

print("\n-- Determinan Matriks --")
print("Determinan Matriks A:", determinant(A))
