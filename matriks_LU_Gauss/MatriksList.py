# Operasi Matriks menggunakan List

def add(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matriks A dan B harus memiliki ukuran yang sama.")
    
    hasil = []
    
    for i in range(len(A)):  
        baris = [] 
        for j in range(len(A[0])):
            baris.append(A[i][j] + B[i][j])
        hasil.append(baris) 
    
    return hasil

def substract(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matriks A dan B harus memiliki ukuran yang sama.")
    
    hasil = []
    
    for i in range(len(A)):  
        baris = [] 
        for j in range(len(A[0])):
            baris.append(A[i][j] - B[i][j])
        hasil.append(baris) 
    
    return hasil

def mult(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Jumlah kolom A harus sama dengan jumlah baris B.")
    
    hasil = []
    for i in range(len(A)):
        baris = []
        for j in range(len(B[0])):
            sum_product = 0
            for k in range(len(A[0])):  
                sum_product += A[i][k] * B[k][j]
            baris.append(sum_product)
        hasil.append(baris)
    
    return hasil  

def scalar_mult(A, k):
    hasil = []
    for i in range(len(A)):
        baris = []
        for j in range(len(A[0])):
            baris.append(A[i][j] * k)
        hasil.append(baris)
    
    return hasil

def transpose(A):
    hasil = [list(baris) for baris in zip(*A)]
    return hasil

def determinant(A):
    if len(A) == 2 and len(A[0]) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    
    det = 0
    
    for j in range(len(A[0])):
        minor = [baris[:j] + baris[j+1:] for baris in A[1:]]
        
        det += ((-1) ** j) * A[0][j] * determinant(minor)
    
    return det

def cofactor(A):
    cofactors = []
    for i in range(len(A)):
        baris = []
        for j in range(len(A[0])):
            minor = [baris[:j] + baris[j+1:] for baris in A[:i] + A[i+1:]]
            cofactor_value = ((-1) ** (i + j)) * determinant(minor)
            baris.append(cofactor_value)
        cofactors.append(baris)
    return cofactors

def inverse(A):
    det_A = determinant(A)
    
    if det_A == 0:
        raise ValueError("Matriks tidak memiliki inverse karena determinannya 0.")
    
    cofactors = cofactor(A)
    
    adjoint = transpose(cofactors)

    invers = [[element / det_A for element in baris] for baris in adjoint]
    
    return invers

def trace(A):
    if len(A) != len(A[0]):
        raise ValueError("Trace hanya dapat dihitung untuk matriks persegi.")
    
    hasil = sum(A[i][i] for i in range(len(A)))
    return hasil

# Contoh penggunaan
A = [[2, 4, 6],
     [1, -3, 5],
     [7, 9, 11]]
print("Matriks A:")
for baris in A:
    print(baris)

B = [[1, 0, 2],
     [3, 1, 4],
     [-5, 2, 6]]
print("\nMatriks B:")
for baris in B:
    print(baris)

# Penjumlahan
print("\n-- Penjumlahan Matriks --")
print("Hasil A + B:")
hasil = add(A, B)
for baris in hasil:
    print(baris)

# Pengurangan
print("\n-- Pengurangan Matriks --")
print("Hasil A - B:")
hasil = substract(A, B)
for baris in hasil:
    print(baris)

# Perkalian
print("\n-- Perkalian Matriks --")
print("Hasil A x B:")
hasil = mult(A, B)
for baris in hasil:
    print(baris)

# Perkalian Skalar
scalar = 4
print("\n-- Perkalian Matriks dengan Skalar --")
print(f"Hasil A x {scalar}:")
hasil = scalar_mult(A, scalar)
for baris in hasil:
    print(baris)
print(f"Hasil B x {scalar}:")
hasil = scalar_mult(B, scalar)
for baris in hasil:
    print(baris)

# Transpose
print("\n-- Transpose Matriks --")
print("Transpose Matriks A:")
hasil = transpose(A)
for baris in hasil:
    print(baris)
print("Transpose Matriks B:")
hasil = transpose(B)
for baris in hasil:
    print(baris)

# determinan
print("\n-- Perkalian Matriks --")
print("Determinan Matriks A:", determinant(A))
print("Determinan Matriks B:", determinant(B))

# inverse
print("\n-- Inverse Matriks --")
print("Inverse Matriks A:")
hasil = inverse(A)
for baris in hasil:
    print(baris)
print("Inverse Matriks B:")
hasil = inverse(B)
for baris in hasil:
    print(baris)

# Trace
print("\n-- Trace Matriks --")
print("Trace dari Matriks A:", trace(A))
print("Trace dari Matriks B:", trace(B))
