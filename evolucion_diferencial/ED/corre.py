# coding: utf-8
# Fraga 12/06/2015
import ed
import pandas as pd

Datos = ed.ED()

# Argumentos:
# Tamaño de poblacion
# Generaciones
# Número de variables
# Constante de diferencias
# Constante de recombinacion
Datos.PoneParametros(10, 70, 10, 0.9, 0.5)
Datos.PoneLimites( [0.01, 0.01, 0.01, 0.01], [1.0, 1.0, 1.0, 1.0] )

Datos.Inicializa( ) 
Datos.EvaluaPoblacion( ) 

i=0
while i<Datos._gen :
    j=0
	while j<Datos._pop :
            Datos.GeneraNuevo( j )      # Generar el nuevo individuo
            Datos.EvaluaNuevo( )        # Evaluarlo
            Datos.ComparaNuevo( j )     # Compararlo con el padre y si es mejor se sustituye
            j += 1
    i += 1

Datos.ImprimeMejor()
