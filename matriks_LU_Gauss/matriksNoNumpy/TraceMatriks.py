def trace(A):
    if len(A) != len(A[0]):
        raise ValueError("Trace hanya dapat dihitung untuk matriks persegi.")
    
    hasil = sum(A[i][i] for i in range(len(A)))
    return hasil


A = []

n = int(input("Masukkan ukuran matriks: "))


print("Matriks A: ")
for i in range(n): 
    row = list(map(int, input(f"Masukkan {n} elemen untuk baris {i+1} (pisahkan dengan spasi): ").split()))
    A.append(row)

# Trace
print("\n-- Trace Matriks --")
print("Trace dari Matriks A:", trace(A))
