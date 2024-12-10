import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def input_persamaan():
    persamaan = input("Masukkan persamaan (gunakan x sebagai variabel, contoh: x*exp(-x) + 1): ")
    x = sp.symbols('x')
    persamaan = sp.sympify(persamaan)
    return persamaan, x

def persamaan_ke_fungsi(persamaan, x):
    f_lambdified = sp.lambdify(x, persamaan, "numpy")
    return f_lambdified

def metode_biseksi(f, a, b, tol=1e-5, max_iter=20):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    
    iterations = []
    for _ in range(max_iter):
        c = (a + b) / 2
        iterations.append(c)
        if abs(b - a) < tol:
            return c, iterations
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2, iterations

def visualisasi(f, a, b):
    x_vals = np.linspace(a - 1, b + 1, 400)
    y_vals = f(x_vals)
    
    plt.plot(x_vals, y_vals, label="f(x) = x * exp(-x) + 1", color='blue')
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)

    plt.title('Metode Biseksi: Proses Iterasi')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    persamaan, x = input_persamaan()
    f = persamaan_ke_fungsi(persamaan, x)
    
    print("\nMetode Biseksi: Proses Mencari Akar")
    a = float(input("Masukkan nilai a: "))
    b = float(input("Masukkan nilai b: "))
    tol = float(input("Masukkan toleransi error (contoh: 0.0001): "))
    
    root, iterations = metode_biseksi(f, a, b, tol)
    print(f"Akar persamaan (Metode Biseksi): {root:.6f}")

    visualisasi(f, a, b, iterations)

if __name__ == "__main__":
    main()