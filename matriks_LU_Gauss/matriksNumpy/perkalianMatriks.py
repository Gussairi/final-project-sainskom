import numpy as np

def mult(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Jumlah kolom A harus sama dengan jumlah baris B.")
    hasil = A.dot(B)
    return hasil

def input_matriks(rows, cols, name):
    print(f"Matriks {name}: ")
    matriks = []
    for i in range(rows):
        while True:
            try:
                row = list(map(int, input(f"Masukkan {cols} elemen untuk baris {i+1} (pisahkan dengan spasi): ").split()))
                if len(row) != cols:
                    raise ValueError(f"Baris harus memiliki tepat {cols} elemen.")
                matriks.append(row)
                break
            except ValueError as e:
                print(f"Input tidak valid: {e}")
    return matriks

while True:
    try:
        rows_A = int(input("Masukkan jumlah baris matriks A: "))
        cols_A = int(input("Masukkan jumlah kolom matriks A: "))
        rows_B = int(input("Masukkan jumlah baris matriks B: "))
        cols_B = int(input("Masukkan jumlah kolom matriks B: "))
        if cols_A != rows_B:
            raise ValueError("Jumlah kolom A harus sama dengan jumlah baris B untuk perkalian matriks.")
        break
    except ValueError as e:
        print(f"Input tidak valid: {e}")

A = input_matriks(rows_A, cols_A, "A")
B = input_matriks(rows_B, cols_B, "B")

A = np.array(A)
B = np.array(B)

print("\n-- Perkalian Matriks --")
print("Hasil A x B:")
print(mult(A, B))
