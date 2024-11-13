# -*- coding: utf-8 -*-

# Cálculo de la carga admisible para una cimentación superficial

# Datos
    # ancho de la cimentación->B
    # largo de la cimentación->L
    # peso especifico de terreno bajo la cimentación
    # cohesión-> c kPa
    # angulo de rozamiento->fi º

# correcciones de la fórmula general
    # por la forma de la cimentación
    # por proximidad a un talud
    # por inclinación de la carga


import numpy as np
import funcionesDatos as fd
import funcionesCalculo as fc

# entrada de los datos de las dimensiones de la cimentación
#print("Datos iniciales de la geometría de la cimentación")
#b=float(input("B[m]="))
#l=float(input("L[m]="))
#numeroCalculos=int(input("Numero de calculos por ancho de B="))
#incremento=float(input("Incremento de dimensión[m]="))


# entrada de datos terreno por encima de la cimentación
print("Datos del terreno por encima del plano de cimentación")
prof=float(input("Profundidad de apoyo de la cimentación [m]="))
pesoEspecificoSup=float(input("peso especifico sup[m]="))


# entrada de los datos del terreno bajo cimentacion
print("Datos del terreno bajo cimentación ")
pesoEspecifico=float(input("peso especifico inf[m]="))
cohesion=float(input("c[kPa]="))
anguloRozamiento=float(input("fi[º]="))

anguloRozamientoRad=np.deg2rad(anguloRozamiento) # paso a radianes


# valor del coeficiente de seguridad
#fs=float(input("FS= "))

# importación de los datos del terreno
espesor,cotas,az,nivel_freatico,pe_aparente,pe_saturada,E,poisson,cohesion,fi=fd.datos_terreno()

# iimportación de las características de la cimentación
b,l,forma,empotramiento,pendiente,axil,hb,hl,fs,numeroCalculos,incremento=fd.datos_cimentacion()

# cálculo de la carga admisible por hundimiento
fc.CargaBrinch_Hansen(cohesion,anguloRozamiento,pesoEspecificoSup,pesoEspecifico,b,l,prof,numeroCalculos,incremento,fs)


