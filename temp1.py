import numpy as np
import pylab as pl
#Crea un  vector (arreglo)con los valores del eje X
x = [1,2,3,4,5]
#Crea un  vector (arreglo)con los valores del eje y para cada valor del eje X
y = [1,2,3,4,5]
#Grafia el vector x contra el vector y
pl.plot (x,y)
#Guarda la grafica en formato png
pl.savefig('temp1.png')
