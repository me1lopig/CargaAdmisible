
# Funciones de manejo de datos


# crea_directorio->Genera un directorio en el que guardar los cálculos
# datos_terreno->Importa los datos incluidos en el archivo datos_terreno.xlsx
# datos_cimentacion->Importa los datos incluidos en el archivo datos_cimentacion.xlsx

# Importación de librerías
import numpy as np
import openpyxl
import os
from datetime import datetime


def datos_terreno():

    libro = openpyxl.load_workbook('datos_terreno.xlsx')
    hoja = libro.active
    
    # geometría de las capas
    espesor=[]
    cotas=[]
    # valores físicos
    pe_aparente=[]
    pe_saturado=[]
    # valores elásticos
    E=[]
    poisson=[]
    # valores de resistencia
    cohesion=[]
    fi=[]

    # tipos de datos
    tipo_datos=[]
   
    for row in hoja.iter_rows():
        espesor.append(row[0].value)
        espesor[0]=0
        az=sum(espesor) # vector de espesores
        nivel_freatico=hoja.cell(row=2, column=2).value
        pe_aparente.append(row[2].value)
        pe_aparente[0]=0
        pe_saturado.append(row[3].value)
        pe_saturado[0]=0
        E.append(row[4].value)
        E[0]=0
        poisson.append(row[5].value)
        poisson[0]=0
        cohesion.append(row[6].value)
        cohesion[0]=0
        fi.append(row[7].value)
        fi[0]=0


    for i in np.arange(len(espesor)):
        cotas.append(sum(espesor[0:i+1]))
    
    # se toman los datos de la cabecera
    for filas in hoja.iter_cols():
        tipo_datos.append(filas[0].value)

    return espesor,cotas,az,nivel_freatico,pe_aparente,pe_saturado,E,poisson,cohesion,fi




def datos_cimentacion():

    libro = openpyxl.load_workbook('datos_cimentacion.xlsx')
    hoja = libro.active
    
    # geometría de las capas
    espesor=[]
    cotas=[]
    # valores físicos
    pe_aparente=[]
    pe_saturado=[]
    # valores elásticos
    E=[]
    poisson=[]
    # valores de resistencia
    cohesion=[]
    fi=[]

    # tipos de datos
    tipo_datos=[]
   
    for row in hoja.iter_rows():
        espesor.append(row[0].value)
        espesor[0]=0
        az=sum(espesor) # vector de espesores
        nivel_freatico=hoja.cell(row=2, column=2).value
        pe_aparente.append(row[2].value)
        pe_aparente[0]=0
        pe_saturado.append(row[3].value)
        pe_saturado[0]=0
        E.append(row[4].value)
        E[0]=0
        poisson.append(row[5].value)
        poisson[0]=0
        cohesion.append(row[6].value)
        cohesion[0]=0
        fi.append(row[7].value)
        fi[0]=0


    for i in np.arange(len(espesor)):
        cotas.append(sum(espesor[0:i+1]))
    
    # se toman los datos de la cabecera
    for filas in hoja.iter_cols():
        tipo_datos.append(filas[0].value)

    return espesor,cotas,az,nivel_freatico,pe_aparente,pe_saturado,E,poisson,cohesion,fi