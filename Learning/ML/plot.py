import numpy as np
import matplotlib.pyplot as plt

#x_train jest zmienną wchodzącą (rozmiar w 1000 stóp kwadratowych)
#y_train jest celowym wynikiem (cena w 1000 dolarach)

x_train = np.array([1.0,2.0])
y_train = np.array([300.0, 500.0])

print(f"x_train = {x_train}")
print(f"y_train = {y_train}")

#m jest ilośćią próbek treningowych

print(f"x_train.shape: {x_train.shape}")

m = x_train.shape[0]
print(f"Ilość próbek treningowych: {m}")

i = 0
x_i = x_train[i]
y_i = y_train[i]
print(f"x^({i}), y^({i}) = ({x_i},{y_i})")



w = 200
b = 100

print(f"w: {w}")
print(f"b: {b}")

def compute_model_output(x,w,b):
    """
    Oblicza przewidywany liniowy model
    """
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w*x[i]+b
    return f_wb

line = compute_model_output(x_train, w, b)

plt.plot(x_train, line, c = 'b', label="Our Prediction")
plt.scatter(x_train, y_train, marker = 'x', c='r', label = 'Actual Values')

plt.title("Housing Price")
plt.ylabel("Price (in 1000s of dollars)")
plt.xlabel("Size (1000 sqft)")
plt.legend()
plt.show()
x_i = 3.0
cost_1200sqft = w*x_i+b
print(f"1200 sqft house will cost: ${cost_1200sqft:.0f}")