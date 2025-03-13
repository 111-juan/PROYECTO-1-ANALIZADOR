import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de valores para x
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

# Calcular cos(x)
y = np.cos(x)

# Crear la gráfica
plt.plot(x, y, label="cos(x)", color='r')

# Etiquetas y título
plt.xlabel("x")
plt.ylabel("cos(x)")
plt.title("Gráfica de cos(x)")
plt.legend()

# Mostrar la gráfica
plt.show()
