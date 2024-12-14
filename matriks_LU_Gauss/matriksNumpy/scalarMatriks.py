import numpy as np

def scalar_mult(A, k):
    hasil = A * k
    return hasil


A = []

n = int(input("Masukkan ukuran matriks: "))


print("Matriks A: ")
for i in range(n): 
    row = list(map(int, input(f"Masukkan {n} elemen untuk baris {i+1} (pisahkan dengan spasi): ").split()))
    A.append(row)

A = np.array(A)


scalar = int(input("Masukkan nilai skalar: "))
print("\n-- Perkalian Matriks dengan Skalar --")
print(f"Hasil A x {scalar}:")
print(scalar_mult(A, scalar))