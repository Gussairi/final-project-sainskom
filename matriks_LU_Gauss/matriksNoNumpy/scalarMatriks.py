def scalar_mult(A, k):
    hasil = []
    for i in range(len(A)):
        baris = []
        for j in range(len(A[0])):
            baris.append(A[i][j] * k)
        hasil.append(baris)
    
    return hasil

A = []

n = int(input("Masukkan ukuran matriks: "))


print("Matriks A: ")
for i in range(n): 
    row = list(map(int, input(f"Masukkan {n} elemen untuk baris {i+1} (pisahkan dengan spasi): ").split()))
    A.append(row)



scalar = int(input("Masukkan nilai skalar"))
print("\n-- Perkalian Matriks dengan Skalar --")
print(f"Hasil A x {scalar}:")
hasil = scalar_mult(A, scalar)
for baris in hasil:
    print(baris)