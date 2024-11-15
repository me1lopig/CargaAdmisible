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
import funcionesGuardado as fg


# importación de los datos del terreno
espesor,cotas,az,nivel_freatico,pe_aparente,pe_saturada,E,poisson,cohesion,anguloRozamiento =fd.datos_terreno()

anguloRozamientoRad=np.deg2rad(anguloRozamiento) # paso a radianes

# iimportación de las características de la cimentación
b,l,forma,empotramiento,pendiente,axil,hb,hl,fs,numeroCalculos,incremento=fd.datos_cimentacion()

print(b,l,forma,empotramiento,pendiente,axil,hb,hl,fs,numeroCalculos,incremento)

print(espesor,cotas,az,nivel_freatico,pe_aparente,pe_saturada,E,poisson,cohesion,anguloRozamiento)




# cálculo de la carga admisible por hundimiento
#fc.CargaBrinch_Hansen(cohesion,anguloRozamiento,pesoEspecificoSup,pesoEspecificoInf,b,l,prof,numeroCalculos,incremento,fs)

# envío de datos al archivo de texto
#fg.guardadoDatos(prof,pesoEspecificoSup,pesoEspecificoInf,cohesion,anguloRozamiento)


