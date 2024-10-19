# calculo de los factores de corrección por proximidad a un talud
# beta es la pendiente con respeto a la horizontal
# si beta es mayor de fi/2 se require un estudio de estabilidad especial

import numpy as np

anguloRozamiento=float(input("fi[º]="))
anguloRozamientoRad=np.deg2rad(anguloRozamiento)

beta=float(input("pendiente[º]="))
if beta<=anguloRozamiento/2:

    betaRadianes=np.deg2rad(beta)

    tc=np.exp(-2*betaRadianes*np.tan(anguloRozamientoRad))
    tq=1-np.sin(2*betaRadianes)
    tg=1-np.sin(2*betaRadianes)

    print("beta= %.2f tc=%.3f tq=%.3f tg=%.3f"%(beta,tc,tq,tg))
else:
    print("Se requere estudio de estabilidad de taludes")


