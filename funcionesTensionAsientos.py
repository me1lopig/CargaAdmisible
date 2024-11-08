# Cálculo de tensiones funciones
    # tensionHarr-> Caĺculo de tensiones en el terreno mediente la formulación de Harr 1966


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

def asientoHarr(q,b,l,z,E,nu):

    # Calculo de tensiones según el método de Harr 1966
    # calcula las tensiones en la esquina de la cimentacion

    # Calculos intermedios
    m1=l/b
    n1=z/b

    factor=1+m1**2+n1**2

    # valores A y B

    A=(np.log((np.sqrt(factor)+m1)/(np.sqrt(factor)-m1))+m1*np.log((np.sqrt(factor)+1)/(np.sqrt(factor)-1)))/(2*np.pi)
    B=(n1/(2*np.pi))*np.arctan(m1/(n1*np.sqrt(factor)))

    # valor de la tension 
    asientoz=(q*b/E)*(1-nu**2)*(A-(1-2*nu)*b/(1-nu))

    return asientoz


def asientoSteimbrenner (q,b,l,z,E,nu):
    # segun la ROM 05.05 para cargas extensas tipo losa 

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


for z in np.arange(0,15):
    asientoH=asientoHarr(300,1.5,1.5,z,15000,0.30)
    asientoS=asientoSteimbrenner(300,1.5,1.5,z,15000,0.30)
    print("z[%.2f] asiento Harr =%.4f asiento Steimbrenner = %.4f"%(z,asientoH,asientoS))