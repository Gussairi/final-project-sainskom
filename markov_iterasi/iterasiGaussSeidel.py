import numpy as np

# Fungsi untuk metode iterasi Gauss-Seidel
def gauss_seidel(A, b, x0, tolerance=1e-10, max_iterations=100):
    n = len(A)
    x = x0.copy()
    for k in range(max_iterations):
        x_new = x.copy()
        print(f"\nIterasi {k+1}:")
        for i in range(n):
            sum_before = sum(A[i][j] * x_new[j] for j in range(i))
            sum_after = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - sum_before - sum_after) / A[i][i]
            print(f"x[{i+1}] = ({b[i]} - {sum_before:.4f} - {sum_after:.4f}) / {A[i][i]} = {x_new[i]:.4f}")
        # Cek konvergensi
        if np.linalg.norm(x_new - x, ord=np.inf) < tolerance:
            print(f"\nConverged after {k+1} iterations.")
            return x_new
        x = x_new
    print("\nMax iterations reached.")
    return x

# Input sistem persamaan linear
n = int(input("Masukkan ukuran matriks (n x n): "))
print("Masukkan elemen matriks A (baris per baris):")
A = np.array([list(map(float, input().split())) for _ in range(n)])

print("Masukkan elemen vektor b:")
b = np.array(list(map(float, input().split())))

# Nilai awal (initial guess)
x0 = np.zeros(len(b))

# Toleransi dan iterasi maksimum
tolerance = float(input("Masukkan toleransi: "))
max_iterations = int(input("Masukkan jumlah iterasi maksimum: "))

# Jalankan metode Gauss-Seidel
print("\nMetode Gauss-Seidel:")
x_gauss_seidel = gauss_seidel(A, b, x0, tolerance, max_iterations)
print("\nSolusi Akhir:", x_gauss_seidel)
