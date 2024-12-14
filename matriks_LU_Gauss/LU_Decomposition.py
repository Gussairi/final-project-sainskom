import numpy as np

def lu_decomposition(A):
    n = len(A)
    Lower = np.zeros((n, n))
    Upper = np.zeros((n, n))

    for i in range(n):
        #Upper triangular matriks
        for k in range(i, n):
            sum_u = sum(Lower[i][j] * Upper[j][k] for j in range(i))
            Upper[i][k] = A[i][k] - sum_u

        #Lower triangular matriks
        for k in range(i, n):
            if i == k:
                Lower[i][i] = 1
            else:
                sum_l = sum(Lower[k][j] * Upper[j][i] for j in range(i))
                Lower[k][i] = (A[k][i] - sum_l) / Upper[i][i]

    return Lower, Upper

# Contoh Penggunaan
# A = np.array([[4, 1, 2, 9],
#             [6, 3, 6, 4],
#             [1, 5, 3, 2],
#             [2, 4, 8, 0]])

A = []
n = int(input("Masukkan dimensi matriks: "));

for i in range(n): 
    row = list(map(int, input(f"Masukkan {n} elemen untuk baris {i+1} (pisahkan dengan spasi): ").split()))
    A.append(row)


Lower, Upper = lu_decomposition(A)
print("Matriks A:")
print(A)
print("\nLower Triangular Matriks L:")
print(Lower)
print("\nUpper Triangular Matriks U:")
print(Upper)

# verivikasi A = L x U
print("\nRekonstruksi Matriks A (L * U):")
print(np.dot(Lower, Upper))
