import numpy as np
import matplotlib.pyplot as plt

def newton_divided_difference(x, y):
    n = len(x)
    coef = np.array(y, dtype=float)
    
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coef[i] = (coef[i] - coef[i-1]) / (x[i] - x[i-j])
    
    return coef

def newton_interpolation(x, y, x_new):
    coef = newton_divided_difference(x, y)
    n = len(x)
    
    y_new = np.zeros_like(x_new)
    
    for i, xi in enumerate(x_new):
        result = coef[-1]
        for j in range(n-2, -1, -1):
            result = coef[j] + (xi - x[j]) * result
        y_new[i] = result
    
    return y_new


print("Masukkan data x (pisahkan dengan spasi):")
x = np.array(list(map(float, input().split())))

print("Masukkan data y (pisahkan dengan spasi, sesuai jumlah x):")
y = np.array(list(map(float, input().split())))

print("Masukkan nilai x untuk prediksi (pisahkan dengan spasi):")
x_preds = np.array(list(map(float, input().split())))


# x = np.array([0, 1, 2, 3, 4])
# y = np.array([0, 1, 4, 9, 16])#y = x^2
# x_preds = np.array([2.5, 3.5]) 


x_new = np.linspace(min(x), max(x), 100)

y_new = newton_interpolation(x, y, x_new)

y_preds = newton_interpolation(x, y, x_preds)

for xi, yi in zip(x_preds, y_preds):
    print(f"Prediksi y untuk x = {xi} adalah y = {yi}")

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Data points', markersize=8)
plt.plot(x_new, y_new, '-', label="Newton's Interpolation")
plt.plot(x_preds, y_preds, 'ro', label='Predicted points')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title("Newton's Polynomial Interpolation")
plt.grid()
plt.show()
