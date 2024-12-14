def determinant(A):
    if len(A) == 2 and len(A[0]) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    
    det = 0
    
    for j in range(len(A[0])):
        minor = [baris[:j] + baris[j+1:] for baris in A[1:]]
        
        det += ((-1) ** j) * A[0][j] * determinant(minor)
    
    return det


A = []

n = int(input("Masukkan ukuran matriks: "))


print("Matriks A: ")
for i in range(n): 
    row = list(map(int, input(f"Masukkan {n} elemen untuk baris {i+1} (pisahkan dengan spasi): ").split()))
    A.append(row)


print("\n-- Perkalian Matriks --")
print("Determinan Matriks A:", determinant(A))
