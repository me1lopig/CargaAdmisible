# Funciones auxiliares

# crea_directorio->Genera un directorio en el que guardar los cálculos
# datos_terreno->Importa los datos incluidos en el archivo datos_terreno.xlsx
# factoresCapacidad->factores de capacidad de carga
# correcciónForma->Coeficientes de corrección por la forma de la cimentación
# correccionTalud-> Coeficientes de corrección por cercanía de la cimentación a un talud
# correccionInclCarga->Coeficientes de correción por inclinación de la carga
# densidad-> Cálculo de la densidad del terreno bajo la base de la cimentación con nivel freático
# tension_rectangular-> cálculo de tensiones bajo la cimentación rectangular
# asientoa-> Calculo de asientos bajo la cimentación


# Importación de librerías
import numpy as np


def factoresCapacidad (cohesion,anguloRozamiento):
     
    anguloRozamientoRad=np.deg2rad(anguloRozamiento)

    if (anguloRozamiento==0):
        Nc=(np.pi+2)
        Nq=1
        Ng=0
    else:
        Nq=((1+np.sin(anguloRozamientoRad))/(1-np.sin(anguloRozamientoRad)))*np.exp(np.pi*np.tan(anguloRozamientoRad))
        Nc=(Nq-1)/np.tan(anguloRozamientoRad)
        Ng=1.5*(Nq-1)*np.tan(anguloRozamientoRad)
    
    return Nc,Nq,Ng


def correccionForma(ancho,largo,anguloRozamiento):

    anguloRozamientoRad=np.deg2rad(anguloRozamiento)
    # factores por influencia de la forma
    sc=1+0.2*ancho/largo
    sq=1+1.5*np.tan(anguloRozamientoRad)*ancho/largo
    sg=1-0.3*ancho/largo

    return sc,sq,sg


def correccionTalud(beta,cohesion,anguloRozamiento):
    # corrección por cercanía de un talud a la cimentación
    # paso de grados a radianes de los ángulos
    betaRad=np.deg2rad(beta)
    anguloRozamientoRad=np.deg2rad(anguloRozamiento)


    if anguloRozamiento>0:
        # calculos de los coeficientes
        tc=np.exp(-2*betaRad*np.tan(anguloRozamientoRad))
        tq=1-np.sin(2*betaRad)
        tg=1-np.sin(2*betaRad)

    else:
        tc=1/(2*betaRad*cohesion)
        tq=tc
        tg=tc

    return tc,tq,tg


def correcionInclCarga(cargaVertical, horizontalB,horizontalL,fi,cohesion,b,l):
    
    # aplicación de la corrección por la inclinación de la carga sobre la cimentación
    # o lo que es lo mismo por el efecto de la exixtencia de fuerzas horizontales
    # datos de entrad, cargas sobre cimentación,parámetros del terreno y dimensiones de la cimentación
    
    fiRadianes=np.deg2rad(fi) # paso a radianes de fi

    horizontal=np.hypot(horizontalB,horizontalL) # resultante de las fuerzas horizontales

    # tangentes en cada lado de la cimentación
    tanSigmaL=horizontalL/cargaVertical
    tanSigmaB=horizontalB/cargaVertical

    nq=factoresCapacidad(cohesion,fi)[1] # se calcula el valor de Nq

    # cálculo de los factores
    iq=np.power((1-0.7*tanSigmaB),3)*(1-tanSigmaL)
    ig=np.power((1-tanSigmaB),3)*(1-tanSigmaL)
    
    if fi==0:
        ic=0.5*(1+np.sqrt(1-horizontal/(b*l*cohesion)))
    else:
        ic=(iq*nq-1)/(nq-1)

    return ic,ig,iq



def densidad(pesoAparente,pesoSaturado,profApoyo,b,zw):
    
    # Cálculo de la densidad bajo cimentación en presencia del nivel freático

    if zw>=b:
        peso=pesoAparente
    if zw<=profApoyo:
        peso=pesoSaturado-9.81
    if profApoyo<zw<b:
        peso=(pesoSaturado-9.81)+(pesoAparente-(pesoSaturado-9.81))*zw/b

    return peso


