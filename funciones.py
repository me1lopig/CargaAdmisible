# Funciones auxiliares

# factoresCapacidad->factores de capacidad de carga
# correcciónForma->Coeficientes de corrección por la forma de la cimentación
# correccionTalud-> Coeficientes de corrección por cercanía de la cimentación a un talud


import numpy as np


def factoresCapacidad (cohesion,anguloRozamiento):
     
    anguloRozamientoRad=np.deg2rad(anguloRozamiento)

    if (cohesion==0):
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


def correccionTalud(beta,anguloRozamiento):
    
    beta=float(input("pendiente[º]="))

    if beta<=anguloRozamiento/2:

        # paso de grados a radianes
        betaRadianes=np.deg2rad(beta)
        anguloRozamientoRad=np.deg2rad(anguloRozamiento)

        # calculos de los coeficientes
        tc=np.exp(-2*betaRadianes*np.tan(anguloRozamientoRad))
        tq=1-np.sin(2*betaRadianes)
        tg=1-np.sin(2*betaRadianes)

    return tc,tq,tg



