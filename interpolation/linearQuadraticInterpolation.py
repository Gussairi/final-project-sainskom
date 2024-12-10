import numpy as np;
import matplotlib.pyplot as plt

def linear_interpolation(x, y, x_new): 
    y_new = []
    for xi in x_new:
        for i in range(len(x) - 1):
            if x[i] <= xi <= x[i + 1]:
                slope = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
                y_new.append(y[i] + slope * (xi - x[i]));
                break

    return np.array(y_new)

def quadratic_interpolation(x, y, x_new):
    y_new = []
    for xi in x_new:
        yi = 0
        for i in range(len(x) - 2):
            if x[i] <= xi <= x[i + 2]:
                L0 = ((xi - x[i + 1]) * (xi - x[i + 2])) / ((x[i] - x[i + 1]) * (x[i] - x[i + 2]))
                L1 = ((xi - x[i]) * (xi - x[i + 2])) / ((x[i + 1] - x[i]) * (x[i + 1] - x[i + 2]))
                L2 = ((xi - x[i]) * (xi - x[i + 1])) / ((x[i + 2] - x[i]) * (x[i + 2] - x[i + 1]))
                yi = L0 * y[i] + L1 * y[i + 1] + L2 * y[i + 2]
                break
        y_new.append(yi)
    return np.array(y_new)


x = np.array([1, 2, 4, 5, 10, 25, 50])
y = np.array([0, 2, 6, 8, 19, 30, 150])

x_graph = np.linspace(min(x), max(x), 100)
y_linear_graph = linear_interpolation(x, y, x_graph)
y_quadratic_graph = quadratic_interpolation(x, y, x_graph)

x_preds = np.array([30]) 
y_pred_linear = linear_interpolation(x, y, x_preds)
y_pred_quadratic = quadratic_interpolation(x, y, x_preds)

print("Menggunakan Interpolasi linear: ")
for xi, yi in zip(x_preds, y_pred_linear):
    print(f"Prediksi y untuk x = {xi} adalah y = {yi}")

print("Menggunakan Interpolasi kuadratik: ")
for xi, yi in zip(x_preds, y_pred_quadratic):
    print(f"Prediksi y untuk x = {xi} adalah y = {yi}")

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Data points', markersize=8)
plt.plot(x_graph, y_linear_graph, '-', label='Linear Interpolation')
plt.plot(x_graph, y_quadratic_graph, '-', label='Quadratic Interpolation')

plt.plot(x_preds, y_pred_linear, 'ro', label='Predicted points (Linear)')
plt.plot(x_preds, y_pred_quadratic, 'ro', label='Predicted points (Quadratic)')


plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Interpolation and Quadratic Interpolation')
plt.grid()
plt.show()