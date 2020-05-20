import numpy as np 
import matplotlib.pyplot as plt

x= np.arange(1,20,1)

plt.plot(x, 1/x, label="Kwadratowa")
plt.title("Funkcja")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()