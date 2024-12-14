import numpy as np


def substract(A, B):
    if len(A) != len(B):
        raise ValueError("Matriks A dan B harus memiliki ukuran yang sama.")
    hasil = A - B
    return hasil

A = []
B = []

n = int(input("Masukkan ukuran matriks: "))


print("Matriks A: ")
for i in range(n): 
    row = list(map(int, input(f"Masukkan {n} elemen untuk baris {i+1} (pisahkan dengan spasi): ").split()))
    A.append(row)

print("Matriks B: ")
for i in range(n): 
    row = list(map(int, input(f"Masukkan {n} elemen untuk baris {i+1} (pisahkan dengan spasi): ").split()))
    B.append(row)

A = np.array(A)
B = np.array(B)


print("\n-- Pengurangan Matriks --")
print("Hasil A - B:")
print(substract(A, B))
