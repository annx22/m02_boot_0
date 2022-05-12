#invocamos las funciones antes de definirlas
#funciones = {
    #'max': maxi,
   # 'min': mini,
  #  'med': media
 #   }
def normal(i):
    return i

def cuadrado(x):
    return x * x

def cubo(x):
    return x **3

def maxi(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for ix in range(1, len(1)):
        if l[ix] > m:
            m = l[ix]
    return m

def mini(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    
    for ix in range(1, len(1)):
        if l[ix] < m:
            m = l[ix]
    return m

def media(*l):
    if len(1) == 0:
        return 0
    
    suma = 0
    for valor in l:
        suma += valor
    
    return suma / len(l)
    
def returnF(nombre):
    nombre = nombre.lower()
    if nombre in funciones.keys():
        return funciones[nombre]
    
    return None