import numpy as np

def gaussElimination(A, b):
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)

    print("Matriks A:")
    print(A)
    print("Vektor b:")
    print(b)

    n = A.shape[0]
    m = A.shape[1]  
    
    for i in range(n):
        if A[i, i] == 0.0:
            raise Exception(f"Pivot di baris {i+1} kolom {i+1} tidak boleh nol!")

        for j in range(i + 1, n):
            if A[j, i] != 0.0:
                print(f"Gunakan elemen di baris {i+1} sebagai pivot untuk mengubah baris {j+1}")
                multiplier = A[j, i] / A[i, i]
                A[j, i:] = A[j, i:] - multiplier * A[i, i:]
                b[j] = b[j] - multiplier * b[i]
                print("Matriks A setelah eliminasi:")
                print(A)
                print("Vektor b setelah eliminasi:")
                print(b)

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        sum = b[i]
        for j in range(i + 1, n):
            sum -= A[i, j] * x[j]
        x[i] = sum / A[i, i]

    return x

A = []
b = []
n = int(input("Masukkan dimensi matriks: "));

for i in range(n): 
    row = list(map(int, input(f"Masukkan {n} elemen untuk baris {i+1} (pisahkan dengan spasi): ").split()))
    A.append(row)

b = list(map(int, input(f"Masukkan {n} elemen sebagai konstanta (pisahkan dengan spasi): ").split()))
    

A = np.array(A)
b = np.array(b)

# A = np.array([[4, 8, 4],
#               [2, 1, -4],
#               [3, -1, 2]])

# b = np.array([80,7,22])

print(A)
print(b)

result = gaussElimination(A, b)
print("Hasil solusi adalah:", result)
