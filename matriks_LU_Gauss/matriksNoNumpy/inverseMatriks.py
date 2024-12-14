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

A = []

n = int(input("Masukkan ukuran matriks: "))

print("Matriks A: ")
for i in range(n): 
    row = list(map(int, input(f"Masukkan {n} elemen untuk baris {i+1} (pisahkan dengan spasi): ").split()))
    A.append(row)

print("\n-- Inverse Matriks --")
print("Inverse Matriks A:")
hasil = inverse(A)
for baris in hasil:
    print(baris)