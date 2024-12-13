# Operasi Matriks menggunakan Numpy
import numpy as np

def add(A, B):
    if len(A) != len(B):
        raise ValueError("Matriks A dan B harus memiliki ukuran yang sama.")
    hasil = A + B
    return hasil

def substract(A, B):
    if len(A) != len(B):
        raise ValueError("Matriks A dan B harus memiliki ukuran yang sama.")
    hasil = A - B
    return hasil

def mult(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Jumlah kolom A harus sama dengan jumlah baris B.")
    hasil = A.dot(B)
    return hasil

def scalar_mult(A, k):
    hasil = A * k
    return hasil

def transpose(A):
    hasil = np.transpose(A)
    return hasil

def determinant(A):
    hasil = np.linalg.det(A)
    return hasil

def inverse(A):
    hasil = np.linalg.inv(A)
    return hasil

def trace(A):
    hasil = np.trace(A)
    return hasil

# Contoh Penggunaan
A = np.array([[2, 4, 5], 
              [5, -6, 2], 
              [2, 4, -1]])
B = np.array([[9, -3, 2], 
              [3, 6, -1], 
              [-3, 4, 6]])
print("Matriks A:\n", A)
print("Matriks B:\n", B)

# Contoh melakukan penjumlahan matriks
print("\n-- Penjumlahan Matriks --")
print("Hasil A + B:")
print(add(A, B))

# Contoh melakukan pengurangan matriks
print("\n-- Pengurangan Matriks --")
print("Hasil A - B:")
print(substract(A, B))

# Contoh melakukan perkalian matriks
print("\n-- Perkalian Matriks --")
print("Hasil A x B:")
print(mult(A, B))

# Contoh melakukan perkalian skalar
scalar = 3
print("\n-- Perkalian Matriks dengan Skalar --")
print(f"Hasil A x {scalar}:")
print(scalar_mult(A, scalar))
print(f"Hasil B x {scalar}:")
print(scalar_mult(B, scalar))

# Contoh melakukan transpose matriks
print("\n-- Transpose Matriks --")
print("Transpose Matriks A:\n", transpose(A))
print("Transpose Matriks B:\n", transpose(B))

# contoh mencari determinan
print("\n-- Determinan Matriks --")
print("Determinan Matriks A:", determinant(A))
print("Determinan Matriks B:", determinant(B))

# Contoh mencari inverse matriks
print("\n-- Inverse Matriks --")
print("Inverse Matriks A:\n", inverse(A))
print("Inverse Matriks B:\n", inverse(B))

# Contoh mencari trace matriks
print("\n-- Trace Matriks --")
print("Trace Matriks A:", trace(A))
print("Trace Matriks B:", trace(B))
    