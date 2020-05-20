import numpy as np 
import matplotlib.pyplot as plt

x= np.arange(0,30,0.1)

plt.plot(x, np.sin(x), label = "Sinus")
plt.plot(x, np.cos(x+1.60)+2, label = "Cosinus")
plt.title("Funkcja sinus i cosinus")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(title="Legenda")
plt.show()