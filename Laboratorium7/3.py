import numpy as np
mac = np.random.randint(low=0, high=51, size=(5, 5))
print(mac)
print(f"Największa liczba:{mac.max()}")
print(f"Najmniejsza liczba:{mac.min()}")
print(f"Największa liczba w wierszach :{mac.max(axis=1)}")
print(f"Najmniejsza liczba w kolumnach:{mac.min(axis=0)}")
print(f"Suma liczb każdego wierszu:{mac.sum(axis=1)}")
