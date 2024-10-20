# Cálculo de la carga admisible para una cimentación superficial

# Datos
    # ancho de la cimentación->B
    # largo de la cimentación->L
    # peso especifico de terreno bajo la cimentación
    # cohesión-> c
    # angulo de rozamiento->fi

# correcciones
    # por la forma de la cimentación
    # por proximidad a un talud


import numpy as np
import funciones as fn

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
    [tc,tq,tg]=fn.correccionTalud(beta,anguloRozamiento)


f=open('calculos.txt','w') # archivo para guardado de los resultados


for ancho in np.arange(b,b+numeroCalculos,incremento):
    for largo in np.arange(l,l+numeroCalculos*incremento,incremento):
        if (ancho<=largo):
            # factores por influencia de la forma

            [sc,sq,sg]=fn.correccionForma(ancho,largo,anguloRozamiento)

            # valor de la carga de hundimiento
            qh=cohesion*Nc*sc*tc+pesoEspecificoSup*prof*Nq*sq*tq+0.5*ancho*pesoEspecifico*Ng*sg*tg
            qadm=qh/fs

            # impresión en pantalla de los cálculos
            #print("B= %.2f m L= %.2f m "%(ancho,largo))
            #print("Nc= %.2f m Nq= %.2f m Ng= %.2f "%(Nc,Nq,Ng))
            #print("sc= %.2f m sq= %.2f m sg= %.2f "%(sc,sq,sg))
            #print("qh= %.2f kPa qadm= %.2f kPa "%(qh,qadm))

            # envio al archivo de los cálculos
            f.write("B= %.2f m L= %.2f m \n"%(ancho,largo))
            #f.write("Nc= %.2f m Nq= %.2f m Ng= %.2f \n"%(Nc,Nq,Ng))
            #f.write("sc= %.2f m sq= %.2f m sg= %.2f \n"%(sc,sq,sg))
            #f.write("tc= %.2f m tq= %.2f m tg= %.2f \n"%(tc,tq,tg))
            f.write("qh= %.2f kPa qadm= %.2f kPa \n"%(qh,qadm))

f.close()