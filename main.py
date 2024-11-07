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
import funcionesHundimiento as fn

# entrada de los datos de las dimensiones de la cimentación
print("Datos iniciales de la geometría de la cimentación")
b=float(input("B[m]="))
l=float(input("L[m]="))
numeroCalculos=int(input("Numero de calculos="))
incremento=float(input("Incremento de dimensión[m]="))


# valor del coeficiente de seguridad
fs=float(input("FS= "))


# entrada de datos por encima de cimentación
print("Datos del terreno por encima del plano de cimentación")
prof=float(input("Profundidad de apoyo de la cimentación [m]="))
pesoEspecificoSup=float(input("peso especifico sup[m]="))


# entrada de los datos del terreno bajo cimentacion
print("Datos del terreno bajo cimentación ")
pesoEspecifico=float(input("peso especifico inf[m]="))
cohesion=float(input("c[kPa]="))
anguloRozamiento=float(input("fi[º]="))

anguloRozamientoRad=np.deg2rad(anguloRozamiento) # paso a radianes


#Parametros de capacidad de carga para loa casos de situacion no drenada y drenada

[Nc,Nq,Ng]=fn.factoresCapacidad(cohesion,anguloRozamiento)


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
    [tc,tq,tg]=fn.correccionTalud(beta,cohesion,anguloRozamiento)


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


f=open('calculos.txt','w') # archivo para guardado de los resultados

# envío de datos al archivo de texto
f.write("Profundidad de apoyo de la cimentación %.2f m\n"%(prof))
f.write("\n\nParámetros físicos del terreno\n")
f.write("peso específico terreno por encima del plano de cimentación %.2f kN/m3 \n"%(pesoEspecificoSup))
f.write("peso específico terreno por debajo del plano de cimentación %.2f kN/m3 \n"%(pesoEspecifico))
f.write("\n\nParámetros de corte del terreno \n")
f.write("Cohesión %.2f kPa\n"%(cohesion))
f.write("Fricción %.2f º\n"%(anguloRozamiento))
f.write("\n\nResultado de los cálculos\n\n")


for ancho in np.arange(b,b+numeroCalculos,incremento):
    for largo in np.arange(l,l+numeroCalculos*incremento,incremento):
        if (ancho<=largo):
            # factores por influencia de la forma

            [sc,sq,sg]=fn.correccionForma(ancho,largo,anguloRozamiento)

            if (pregunta=='S' or pregunta=='s'):
                [ic,iq,ig]=fn.correcionInclCarga(cargaV,cargaHb,cargaHl,anguloRozamiento,cohesion,ancho,largo)
    

            # valor de la carga de hundimiento
            qh=cohesion*Nc*sc*tc*ic+pesoEspecificoSup*prof*Nq*sq*tq*iq+0.5*ancho*pesoEspecifico*Ng*sg*tg*ig
            qadm=qh/fs

            # impresión en pantalla de los cálculos
            #print("B= %.2f m L= %.2f m "%(ancho,largo))
            #print("Nc= %.2f m Nq= %.2f m Ng= %.2f "%(Nc,Nq,Ng))
            #print("sc= %.2f m sq= %.2f m sg= %.2f "%(sc,sq,sg))
            #print("qh= %.2f kPa qadm= %.2f kPa "%(qh,qadm))


            # envio al archivo de los cálculos
            f.write("B= %.2f m L= %.2f m \n"%(ancho,largo))
            f.write("Nc= %.2f m Nq= %.2f m Ng= %.2f \n"%(Nc,Nq,Ng))
            f.write("sc= %.2f m sq= %.2f m sg= %.2f \n"%(sc,sq,sg))
            f.write("tc= %.2f m tq= %.2f m tg= %.2f \n"%(tc,tq,tg))
            f.write("ic= %.2f m iq= %.2f m ig= %.2f \n"%(ic,iq,ig))
            f.write("qh= %.2f kPa qadm= %.2f kPa \n\n"%(qh,qadm))


f.close()