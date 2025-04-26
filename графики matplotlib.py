import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)

y1 = x
y2 = 2 * x
y3 = 3 * x
y4 = x ** 2
y5 = 2 * x ** 2

plt.figure(figsize=(10, 6))

plt.plot(x, y1, label='y = x', color='blue')
plt.plot(x, y2, label='y = 2*x', color='green')
plt.plot(x, y3, label='y = 3*x', color='red')
plt.plot(x, y4, label='y = x^2', color='orange')
plt.plot(x, y5, label='y = 2*x^2', color='purple')

plt.title('Графики функций')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0, 10)
plt.ylim(0, 100)
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()

plt.show()