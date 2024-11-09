# funciones de cálculo de variación de tensiones en el terreno

# datos de entrada

    # E->Módulo de elasticidad (kPa
    # nu->Coeficiente de poisson
    # q->Carga transmitida por la cimentación (kPa)
    # b-> Dimensión menor de la cimentación (m
    # l-> Dimensión mayor de la cimentación (m)
    # z-> Profundidad de cálculo (m)

# tension21-> calculo de disipaciónd de tensiones segun el método dos uno
# tensionWestergaard-> calculo de disipaciónd de tensiones segun el método de Westergaard

import numpy as np


def tension21(q,b,l,z):

    # cálculo del incremento de presiones en el centro de la cimentación rectangular

    incrTensionz=q*b*l/((b+z)*(l+z))

    return incrTensionz


def tensionWestergaard(q,b,l,z,nu):

    # cálculo del incremento de presiones según el método de Westergaard
    # se calcula en la esquina, la función da el valor en el centro

    n=l*0.5/z
    m=b*0.5/z
    c=np.sqrt((1-2*nu)/(2*(1-nu)))

    incrTensionz=(q*np.atan(m*n/np.sqrt(c**2+n**2+m**2)))/(2*np.pi)

    return incrTensionz*4



for z in np.arange(0.0001,10,0.5):
    tensionM=tension21(150,1.5,1.5,z)
    tensionW=tensionWestergaard(150,1.5,1.5,z,0.30)
    print("z[%.2f] presion21=%.3f presionWe=%.3f"%(z,tensionM,tensionW))
    print("q/incr M %.3f q/incr W %.3f"%(tensionM/150,tensionW/150))


