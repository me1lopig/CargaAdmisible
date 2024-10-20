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
pesoEspecifico=float(input("peso especifico[m]="))
cohesion=float(input("c[kPa]="))
anguloRozamiento=float(input("fi[º]="))
anguloRozamientoRad=np.deg2rad(anguloRozamiento)


# Factores de correción por proximidad de talud
print("Datos proximidad a talud")
beta=float(input("Angulo de la pendiente[º]="))
betaRadianes=np.deg2rad(beta)

tc=np.exp(-2*betaRadianes*np.tan(anguloRozamientoRad))
tq=1-np.sin(2*betaRadianes)
tg=1-np.sin(2*betaRadianes)


#Parametros de capacidad de carga para loa casos de situacion no drenada y drenada

if (cohesion==0):
    Nc=(np.pi+2)
    Nq=1
    Ng=0
else:
    Nq=((1+np.sin(anguloRozamientoRad))/(1-np.sin(anguloRozamientoRad)))*np.exp(np.pi*np.tan(anguloRozamientoRad))
    Nc=(Nq-1)/np.tan(anguloRozamientoRad)
    Ng=1.5*(Nq-1)*np.tan(anguloRozamientoRad)


f=open('calculos.txt','w') # archivo para guardado de los resultados


for ancho in np.arange(b,b+numeroCalculos,incremento):
    for largo in np.arange(l,l+numeroCalculos*incremento,incremento):
        if (ancho<=largo):
            # factores por influencia de la forma
            sc=1+0.2*ancho/largo
            sq=1+1.5*np.tan(anguloRozamientoRad)*ancho/largo
            sg=1-0.3*ancho/largo


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