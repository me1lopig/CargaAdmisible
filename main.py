# Cálculo de la carga admisible para una cimantación superficial

# Datos
    # ancho de la cimentación->B
    # largo de la cimentación->L
    # peso especifico de terreno bajo la cimentación
    # cohesión-> c
    # angulo de rozamiento->fi


import numpy as np

# entrada de los datos de las dimensiones de la cimentación
print("Datos de la geometría de la cimentación")
b=float(input("B[m]="))
l=float(input("L[m]="))

# entrada de los datos del terreno
pesoEspecifico=float(input("peso especifico[m]="))
cohesion=float(input("c[kPa]="))
anguloRozamiento=float(input("fi[º]="))

anguloRozamientoRad=np.deg2rad(anguloRozamiento)

#Parametros de capacidad de carga
Nq=((1+np.sin(anguloRozamientoRad))/(1-np.sin(anguloRozamientoRad)))*np.exp(np.pi*np.tan(anguloRozamientoRad))
Nc=(Nq-1)/np.tan(anguloRozamientoRad)
Ng=1.5*(Nq-1)*np.tan(anguloRozamientoRad)

print("Factores de capacidad de carga")
print("Nc= ",Nc)
print("Nq= ",Nq)
print("Ng= ",Ng)


# factores por influencia de la forma
sc=1+0.2*b/l
sq=1+1.5*np.tan(anguloRozamientoRad)*b/l
sg=1-0.3*b/l

print("Factores de correcion por forma de la cimentación")
print("sc= ",sc)
print("sq= ",sq)
print("sg= ",sg)

