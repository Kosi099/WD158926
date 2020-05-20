import numpy as np 
import matplotlib.pyplot as plt

x= np.arange(1,20,1)

plt.plot(x, 1/x, 'g>--' ,label="f(x) = 1/x")
plt.title("Wykres funkcji f(x) dla x[1,20]")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()