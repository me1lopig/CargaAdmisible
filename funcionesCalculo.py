# Funciones de cálculo de carda admisible 

# CargaBrinch_Hansen-> Cálculo de la carga admisible mediente la fórmula de BrinchHansen

# imprtacion de librerias externas
import numpy as np

# importación de librerías de usuario
import funcionesFacCTE as fcte
import funcionesGuardado as fg


def CargaBrinch_Hansen(cohesion,anguloRozamiento,pesoEspecificoSup,pesoEspecificoinf,b,l,prof,beta,N,Hb,Hl,numeroCalculos,incremento,fs):


#Parametros de capacidad de carga para loa casos de situacion no drenada y drenada

    [Nc,Nq,Ng]=fcte.factoresCapacidad(anguloRozamiento)


    # Factores de correción por proximidad de talud
    #print("Datos proximidad a talud")
    #beta=float(input("Angulo de la pendiente[º]="))
    betaRadianes=np.deg2rad(beta)

    if beta>=anguloRozamiento/2:
        print('El valor de beta[º]= %.2f es mayor que la mitad del ángulo de rozamiento[º]= %.2f'%(beta,anguloRozamiento))
        print('Se requiere estudio especial')
        print('Cálculo interrumpido')
        exit() # se termina el programa
    else:    
        [tc,tq,tg]=fcte.correccionTalud(beta,cohesion,anguloRozamiento)



 


    for ancho in np.arange(b,b+numeroCalculos,incremento):
        for largo in np.arange(l,l+numeroCalculos*incremento,incremento):
            if (ancho<=largo):
            # factores por influencia de la forma

                [sc,sq,sg]=fcte.correccionForma(ancho,largo,anguloRozamiento)

                if (N!=0 and Hl!=0):
                    [ic,iq,ig]=fcte.correcionInclCarga(N,Hb,Hl,anguloRozamiento,cohesion,ancho,largo)
                else:
                    ic=1
                    iq=1
                    ig=1
                    
    

            # valor de la carga de hundimiento
                qh=cohesion*Nc*sc*tc*ic+pesoEspecificoSup*prof*Nq*sq*tq*iq+0.5*ancho*pesoEspecificoinf*Ng*sg*tg*ig
                qadm=qh/fs

                # envio al archivo de los cálculos
                fg.guardadoCalculos(ancho,largo,Nc,Ng,Nq,sc,sg,sq,tc,tg,tq,ic,ig,iq,qh,qadm)






