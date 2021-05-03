# Librerias
import numpy as np
import pandas as pd
import random as rand
import os
import sys

# Parametros para ED
D = 4				# dimension del problema
NP = 10			# tamanio de poblacion				NP >= 4
GEN = 15			# numero de generaciones
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
Pop = np.zeros( (NP, D +1) )			# Matriz de la poblacion,
V = np.zeros( D+1)						# Vector donador (mutacion)
limites = np.zeros( (2, D) )			# [0][] -> vmin 	[1][] -> vmax
vamplitud = np.zeros( D )				# [] -> vmax - vmin
iBest = 0									# indice del mejor

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++	
# +++++++++++++++++ Funcion objetivo ++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++	
def evalua(d, xi) :

	with open("KYout.txt") as f:
		f_contents = f.readlines()
	
	kaplan = f_contents[5]
	v = -float(kaplan[-9:-1])
	return v
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
def lyap_spec(filename) :
	
	command = "./lyap_spec " + filename + " -x30000 -m3,1 -k100 -oKYout.txt"
	print(command)
	os.system(command)
	return 0
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
def poner_limites(vmin, vmax) :
	n = len( vmin )
	if n != D :
		print( "ERROR: el vector de minimos es diferente que el numero de variables" )
		sys.exit(1)

	n = len( vmax )
	if n != D :
		print( "ERROR: el vector de maximos es diferente que el numero de variables" )
		sys.exit(1)
		
	# ~ limites = np.zeros( (2, D) )
	# ~ vamplitud = np.zeros( D )
		
	i = 0
	while i < D :
		limites[0][i] = vmin[i]
		limites[1][i] = vmax[i]
		vamplitud[i] = vmax[i] - vmin[i]
		i += 1
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++	
def inicializa() :
	i = 0
	while i < NP :
		j = 0
		command = './gl '
		while j < D :									# Generar D valores aleatorios
			v = limites[0][j] + rand.random()*vamplitud[j]
			Pop[i][j] = v
			# Generar comando de GL
			command += str(v)	+ " "
			# ~ if j == D-1 :
				# ~ command += str(v)
			# ~ else:
				# ~ command += str(v)	+ " "
			j += 1
		outname = "gl_Pop" + str(i) + ".txt" 
		os.system("rm -f -- " + outname)				# Borrar antiguo
		command = command + outname
		#print(command)
		os.system(command)							# Generar serie de tiempo
		t1 = check_inf(-50.0,50.0,outname)	   # Comprobar que no infinita
		t2 = check_stable(100,1e-6,outname)	# Comprobar que no sea estable
		if t1 == 0 and t2 == 0 :
			print("\tBUEN OSCILADOR ...............................")
			i += 1
		elif t1 == 1 :
			print("\tMAL OSCILADOR, INFINITO ......................")
		else	:
			print("\tMAL OSCILADOR, ESTABLE .......................")
		#i += 1
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++	
def check_inf(lim_L, lim_H, filename) :
	data = pd.read_csv(filename, sep = '\t', header = None)
	rows, columns = data.shape
	state = 0
	i = 0
	while i < columns:
		j = 0
		while j < rows:
			t = data[i][j]
			#print(t)
			if t > lim_H or t < lim_L:
				state = 1
				break
			j += 1
		if state == 1:
			break
		i += 1
	return state
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def check_stable(num_rep,tolerance,filename):
	data = pd.read_csv(filename, sep = '\t', header = None)
	rows, columns = data.shape
	told = data[0][0] + 1
	state = 0
	i = 0
	while i < columns:
		j = 0
		state = 0
		while j < rows:
			t = data[i][j]
			if state >= num_rep:
				break	
			elif abs(t-told) < tolerance : #tolerance
				state += 1
			else:
				state = 0
				
			told = t
			j += 1
		if state >= num_rep:
			break
		i += 1
	if state != num_rep:
		state = 0
	else:
		state = 1
	return state
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
def evalua_poblacion() :
	i = 0
	while i < NP :
		filename = "gl_Pop" + str(i) + ".txt" 
		os.system("rm -f -- " + "KYout.txt")		# Borrar tisean antiguo
		lyap_spec(filename)								# Generamos salida tisean
		v = evalua( D, Pop[i])							# Leemos salida tisean
		print(v)
		Pop[i][D] = v										# La escribimos
		i += 1
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
def evalua_individuo(filename) :
	os.system("rm -f -- " + "KYout.txt")
	lyap_spec(filename)
	V[D] = evalua(D, V)
	print(V[D])
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
def imprime_ressultados() :
	print("xi: ")
	i = 0
	while i < D :
		print(Pop[iBest][i])
		i += 1
	print("f(x1, x2, ... xi) = ", end = '')	
	print(Pop[iBest][D])
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
def minimo() :
	i = 1
	minimo = Pop[0][D]
	while i < NP :
		if Pop[i][D] < minimo :
			minimo = Pop[i][D]
		i += 1
	print(minimo)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++        Principal    +++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
poner_limites([L,L,L,L],[H,H,H,H])
inicializa()
evalua_poblacion()
print(Pop)
i = 0
while i < GEN :							# por cada generacion
	print("+++++++++++++++++++++++++++++++++++++++++++++")
	print("Generacion: " + str(i))
	print("+++++++++++++++++++++++++++++++++++++++++++++")
	j = 0
	while j < NP :							# por cada individio (renglon de Pop)
		
		# generar 3 indices aleatorios diferentes entre ellos y diferentes a j
		r1 = rand.randint(0, NP-1)
		while r1 == j :
			r1 = rand.randint(0, NP-1)
		
		r2 = rand.randint(0, NP-1)
		while r2 == r1 or r2 == j :
			r2 = rand.randint(0, NP-1)
			
		r3 = rand.randint(0, NP-1)
		while r3 == r2 or r3 == r1 or r3 == j :
			r3 = rand.randint(0, NP-1)
		
		# Crear individuo de prueba
		irand = rand.randint(0, D-1)
		k = 0
		# Recombinacion
		command = './gl '
		while k < D :																# (Columna de Pop)
			if rand.random() < CR or irand == k :
				V[k] = Pop[r3][k] + F*( Pop[r2][k] - Pop[r1][k] )		# Mutacion
				# Checar limites
				if V[k] < limites[0][k] or V[k] > limites[1][k]:  		# limite inferior o limite superior
					V[k] = limites[0][k] + rand.random()*vamplitud[k]
			else:
					V[k] = Pop[j][k]		
			command += str(V[k])	+ " "											# Generar comando GL
			k += 1
		outname = "gl_Trial" + str(j) + ".txt"
		os.system("rm -f -- " + outname)
		command = command + outname
		os.system(command)
		t1 = check_inf(-50.0,50.0,outname)	   # Comprobar que no infinita
		t2 = check_stable(100,1e-6,outname)	# Comprobar que no sea estable
		if t1 == 0 and t2 == 0 :
			print("\tBUEN OSCILADOR ...............................")
		elif t1 == 1 :
			print("\tMAL OSCILADOR, INFINITO ......................")
			continue
		else	:
			print("\tMAL OSCILADOR, ESTABLE .......................")
			continue

		# Evaluar individuo de prueba
		evalua_individuo(outname) 
		
		# Seleccion
		if V[D] < Pop[j][D] :
			k = 0
			while k <= D :
				Pop[j][k] = V[k]
				k += 1
				
			if V[D] <=  Pop[iBest][D] :
				iBest = j
				
		j += 1
		
	i += 1


imprime_ressultados()


# NOTAS:
# ~ arr[renglon][columna]

