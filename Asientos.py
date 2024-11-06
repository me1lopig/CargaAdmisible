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


# cálculo del asiento

    return P*B*(Ac*f1-Bc*f2)/(2*E)
