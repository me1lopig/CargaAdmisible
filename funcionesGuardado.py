# funciones de guardado de archivo de resultados

def guardadoTexto(prof,pesoEspecificoSup,pesoEspecifico,cohesion,anguloRozamiento,Nc,Ng,Nq,sc,sg,sq,tc,tg,tq,ic,ig,iq):

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


    # envio al archivo de los cálculos
    f.write("B= %.2f m L= %.2f m \n"%(ancho,largo))
    f.write("Nc= %.2f m Nq= %.2f m Ng= %.2f \n"%(Nc,Nq,Ng))
    f.write("sc= %.2f m sq= %.2f m sg= %.2f \n"%(sc,sq,sg))
    f.write("tc= %.2f m tq= %.2f m tg= %.2f \n"%(tc,tq,tg))
    f.write("ic= %.2f m iq= %.2f m ig= %.2f \n"%(ic,iq,ig))
    f.write("qh= %.2f kPa qadm= %.2f kPa \n\n"%(qh,qadm))


    f.close()