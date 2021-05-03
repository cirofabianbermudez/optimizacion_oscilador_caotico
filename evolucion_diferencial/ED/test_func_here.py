# Librerias
import numpy as np
import pandas as pd
import random as rand
import os
import sys

# Parametros para ED
D = 4				# dimension del problema
NP = 10			# tamanio de poblacion				NP >= 4
GEN = 10			# numero de generaciones
F = 0.9			# constante de diferencias			[0,2]
CR = 0.5 		# constante de recombinacion		[0,1]

# Son globales para todas las variables de entrada
# Rosenbrocks function
L = 0.01;    
H = 1.0;    
# Sphere function
# ~ L = -5.12			# limite inferior
# ~ H = 5.0				# limite superior

#Variables para el algoritmo
	# La ultima columna se usa para la evaluacion
# ~ Pop = np.zeros( (NP, D +1) )			# Matriz de la poblacion,

	
# ~ def evalua(d, xi) :

	# ~ with open("KYout.txt") as f:
		# ~ f_contents = f.readlines()
	
	# ~ kaplan = f_contents[5]
	# ~ v = -float(kaplan[-9:-1])
	# ~ return v
# ~ # +++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ~ def lyap_spec(filename) :
	
	# ~ command = "./lyap_spec " + filename + " -x30000 -m3,1 -k50 -oKYout.txt"
	# ~ print(command)
	# ~ os.system(command)
	# ~ return 0
	
# ~ def evalua_poblacion() :
	# ~ i = 0
	# ~ while i < NP :
		# ~ filename = "gl_Pop" + str(i) + ".txt" 
		# ~ os.system("rm -f -- " + "KYout.txt")		# Borrar tisean antiguo
		# ~ lyap_spec(filename)								# Generamos salida tisean
		# ~ v = evalua( D, Pop[i])							# Leemos salida tisean
		# ~ print(v)
		# ~ Pop[i][D] = v										# La escribimos
		# ~ i += 1

# ~ outname = "gl_Pop0.txt"
# ~ t1 = check_inf(-50.0,50.0,outname)	   # Comprobar que no infinita
# ~ t2 = check_stable(100,1e-6,outname)	# Comprobar que no sea estable
# ~ evalua_poblacion()


flag = 0
j = 0
while j < 10 :
	i = 0
	while i < 20:
		print(i)
		if input("ingresa valor: ") == "1":
			i += 1
		else :
			continue
	print(j)
	j += 1		
	

