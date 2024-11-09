# Cálculo de tensiones funciones
    # asientoSteimbrennercálculo de asientos en funcion de z
    # asientoBoussinesq cálculo de asientos para semiespacio elastico

# datos de entrada

    # E->Módulo de elasticidad (kPa
    # nu->Coeficiente de poisson
    # q->Carga transmitida por la cimentación (kPa)
    # b-> Dimensión menor de la cimentación (m
    # l-> Dimensión mayor de la cimentación (m)
    # z-> Profundidad de cálculo (m)


# librerias

import numpy as np


# funciones de asientos

def asientoSteimbrenner (q,b,l,z,E,nu):
    # segun la ROM 05.05 para cargas extensas tipo losa
    # calcula al asiento a una profundidad determinada

    # Cálculos intermedios
    Ac=1-nu**2
    Bc=1-nu-2*nu**2
    m=z/b
    n=l/b
    t=(1+n**2+m**2)**0.5
    f1=(1/np.pi)*(np.log((t+n)/(t-n))+n*np.log((t+1)/(t-1)))
    f2=(m/np.pi)*np.arctan(n/(t*m))


# cálculo del asiento

    return q*b*(Ac*f1-Bc*f2)/(2*E)



def asientoBoussinesq(q,b,l,E,nu):
    # cálculo de asientos en un semiespacio infinito elastico

    # cálculos intermedios
    n=l/b
    k=0.3069*np.log(n)+0.5548

    # cálculo del asiento
    asiento=k*q*b*(1-nu**2)/E

    return asiento


for z in np.arange(0.001,15):
    asientoS=asientoSteimbrenner(300,1.5,2.5,z,25000,0.30)
    asientoB=asientoBoussinesq(300,1.5,2.5,25000,0.30)
    print("z[%.2f]  asiento Steimbrenner = %.4f asiento Bussinesq = %.4f" %(z,asientoS,asientoB))