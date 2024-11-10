# Funciones de cálculo de carda admisible 

# CargaBrinch_Hansen-> Cálculo de la carga admisible mediente la fórmula de BrinchHansen

# imprtacion de librerias externas
import numpy as np

# importación de librerías de usuario
import funcionesFacCTE as fcte
import funcionesGuardado as fg


def CargaBrinch_Hansen(cohesion,anguloRozamiento,pesoEspecificoSup,pesoEspecifico,b,l,prof,numeroCalculos,incremento,fs):


#Parametros de capacidad de carga para loa casos de situacion no drenada y drenada

    [Nc,Nq,Ng]=fcte.factoresCapacidad(cohesion,anguloRozamiento)


    # Factores de correción por proximidad de talud
    print("Datos proximidad a talud")
    beta=float(input("Angulo de la pendiente[º]="))
    betaRadianes=np.deg2rad(beta)

    if beta>=anguloRozamiento/2:
        print('El valor de beta[º]= %.2f es mayor que la mitad del ángulo de rozamiento[º]= %.2f'%(beta,anguloRozamiento))
        print('Se requiere estudio especial')
        print('Cálculo interrumpido')
        exit() # se termina el programa
    else:    
        [tc,tq,tg]=fcte.correccionTalud(beta,cohesion,anguloRozamiento)


# corrección por inclinación de la carga sobre la cimentación
    pregunta=input("Se considera efecto de inclinación de la carga [S/N] ")
    if (pregunta=='S' or pregunta=='s'):
        print('Datos de las cargas sobre cimentación')
        cargaV=float(input('Carga vertical N[kN]='))
        cargaHb=float(input('Carga horizontal Hb[kN]='))
        cargaHl=float(input('Carga horizontal HL[kN]='))
    else:
        ic=1
        iq=1
        ig=1

    # envío de datos al archivo de texto
    fg.guardadoDatos(prof,pesoEspecificoSup,pesoEspecifico,cohesion,anguloRozamiento)


    for ancho in np.arange(b,b+numeroCalculos,incremento):
        for largo in np.arange(l,l+numeroCalculos*incremento,incremento):
            if (ancho<=largo):
            # factores por influencia de la forma

                [sc,sq,sg]=fcte.correccionForma(ancho,largo,anguloRozamiento)

                if (pregunta=='S' or pregunta=='s'):
                    [ic,iq,ig]=fcte.correcionInclCarga(cargaV,cargaHb,cargaHl,anguloRozamiento,cohesion,ancho,largo)
    

            # valor de la carga de hundimiento
                qh=cohesion*Nc*sc*tc*ic+pesoEspecificoSup*prof*Nq*sq*tq*iq+0.5*ancho*pesoEspecifico*Ng*sg*tg*ig
                qadm=qh/fs

                # envio al archivo de los cálculos
                fg.guardadoCalculos(ancho,largo,Nc,Ng,Nq,sc,sg,sq,tc,tg,tq,ic,ig,iq,qh,qadm)






