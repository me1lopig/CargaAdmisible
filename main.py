# Cálculo de la carga admisible para una cimantación superficial

# Datos
    # ancho de la cimentación->B
    # largo de la cimentación->L
    # peso especifico de terreno bajo la cimentación
    # cohesión-> c
    # angulo de rozamiento->fi


import numpy as np
import openpyxl

# entrada de los datos de las dimensiones de la cimentación
print("Datos iniciales de la geometría de la cimentación")
b=float(input("B[m]="))
l=float(input("L[m]="))
numeroCalculos=int(input("Numero de calculos="))
incremento=float(input("Incremento de dimensión[m]="))


# valor del coeficiente de seguridad
fs=float(input("FS= "))


# entrada de datos por encima de cimentación
print("Datos del terreno por encima del plano de cimentación")
prof=float(input("Profundidad de apoyo de la cimentación [m]="))
pesoEspecificoSup=float(input("peso especifico[m]="))


# entrada de los datos del terreno bajo cimentacion
print("Datos del terreno bajo cimentación ")
pesoEspecifico=float(input("peso especifico[m]="))
cohesion=float(input("c[kPa]="))
anguloRozamiento=float(input("fi[º]="))

anguloRozamientoRad=np.deg2rad(anguloRozamiento)

#Parametros de capacidad de carga para loa casos de situacion no drenada y drenada

if (cohesion==0):
    Nc=(np.pi+2)
    Nq=1
    Ng=0
else:
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

# valor de la carga de hundimiento
qh=cohesion*Nc*sc+pesoEspecificoSup*prof*Nq*sq+0.5*b*pesoEspecifico*Ng*sg
qadm=qh/fs



print("Carga de hundimiento[kPa]= ",qh)
print("Carga admisible[kPa]= ",qadm)
