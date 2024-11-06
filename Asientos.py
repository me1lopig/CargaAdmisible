# Cálculo de asientos mediente el método indicado en la ROM 05.05
# datos de entrada

    # E->Móduloi de elasticidad (kPa
    # nu->Coeficiente de poisson
    # P->Carga transmitida por la cimentación (kPa)
    # B-> Dimensión menor de la cimentación (m
    # L-> Dimensión mayor de la cimentación (m)
    # z-> Profundidad de cálculo (m)

 

# librerias

import numpy as np


def asientos (E,nu,P,B,L,z):

    # Cálculos intermedios
    Ac=1-nu**2
    Bc=1-nu-2*nu**2
    m=z/B
    n=L/B
    t=(1+n**2+m**2)**0.5
    f1=(1/np.pi)*(np.log((t+n)/(t-n))+n*np.log((t+1)/(t-1)))
    f2=(m/np.pi)*np.arctan(n/(t*m))

    #print("Valores intermedios")
    #print("A=",Ac)
    #print("B=",Bc)
    #print("m=",m)
    #print("n=",n)
    #print("f1=",f1)
    #print("f2=",f2)

# cálculo del asiento

    return P*B*(Ac*f1-Bc*f2)/(2*E)


# llamada a la función
for z in np.arange(0.001,10,0.5):

    asiento=asientos (15000,0.5,150,1.5,2.5,z)
    print(" El asiento a la profundidad %.2f es %.4f mm "%(z,asiento))

