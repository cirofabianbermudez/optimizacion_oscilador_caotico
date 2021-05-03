import numpy as np
import pandas as pd
import random as rand
import os
import sys

# Parametros para ED
D = 10				# dimension del problema
NP = 60			# tamanio de poblacion				NP >= 4
GEN = 5000			# numero de generaciones
F = 0.9			# constante de diferencias			[0,2]
CR = 0.5 		# constante de recombinacion		[0,1]

# Son globales para todas las variables de entrada
# Rosenbrocks function
L = -2.048;    
H = 2.048;    
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
	f = 0
	i = 0
	# Sphere function
	# ~ while i < d:
		# ~ f = f + ( xi[i] )**2
		# ~ i += 1
	
	# Rosenbroks function
	while i < d-1:
		f = f + 100.0*( xi[i]*xi[i] - xi[i+1] )**2 + (1.0 - xi[i])**2
		i += 1
	
	return f

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
		while j < D :
			v = limites[0][j] + rand.random()*vamplitud[j]
			Pop[i][j] = v
			j += 1
		i += 1
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++	
def evalua_poblacion() :
	i = 0
	while i < NP :
		v = evalua( D, Pop[i])
		Pop[i][D] = v
		i += 1
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
def evalua_individuo() :
	V[D] = evalua(D, V)
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
poner_limites([L,L,L,L,L,L,L,L,L,L],[H,H,H,H,H,H,H,H,H,H])
inicializa()
evalua_poblacion()
i = 0
while i < GEN :							# por cada generacion
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
		while k < D :																# (Columna de Pop)
			if rand.random() < CR or irand == k :
				V[k] = Pop[r3][k] + F*( Pop[r2][k] - Pop[r1][k] )		# Mutacion
				# Checar limites
				if V[k] < limites[0][k] or V[k] > limites[1][k]:  		# limite inferior o limite superior
					V[k] = limites[0][k] + rand.random()*vamplitud[k]
			else:
					V[k] = Pop[j][k]		
			k += 1
			
		# Evaluar individuo de prueba
		evalua_individuo() 
		
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

