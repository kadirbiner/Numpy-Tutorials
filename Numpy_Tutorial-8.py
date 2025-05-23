# -*- coding: utf-8 -*-
"""Numpy-Dersleri

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1R8Z1AV_J82hdj_hoXOZcsYxUAfURTaNM

#ones() , zeros() & full() Matris oluşturma Methodları
"""

import numpy as np

np.zeros(5)

np.zeros((2,3))

np.ones(7)

np.full((4,4),18)

"""#Numpy eye() diag() & idendity() Metotları"""

np.identity(5) #köşegeni 1lerden oluşan kare matirs.

np.eye(5,k=3) #k yani birim köşegeni 3 birim öteledi.

np.eye(5,k=-1)

np.diag([1,1,1,1,1])

np.diag([1,2,3,2,1]) #bu şekilde kullanırsam bir matris oluşturu ve veridğim değerleri o matirsin köşegeni yapar.

r=np.random.randint(1,10,(5,5))
print(r)

np.diag(r) #var olan bir matrisin köşegenini alır.

np.diag(np.diag(r))