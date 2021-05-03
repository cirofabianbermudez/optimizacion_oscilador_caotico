# coding: utf-8
import numpy
import random
import evalua

def Inicializa1( self ) :
	i = 0
	while i<self._pop :
		j = 0
		while j<self._nv :
			k = random.random( )
			v = self.Limites[0][j] + k * self.vamplitud[j]
			self.Pop[i][j] = v
			j += 1
		i += 1

def PoneParametros1( self, pop, gen, nv, cf, cr ) :
	self._pop = pop
	self._gen = gen
	self._nv  = nv
	self._cf = cf
	self._cr = cr
	self.Pop = numpy.zeros( (pop, nv+1) )
	self.vnuevo = numpy.zeros( nv+1 )

def PoneLimites1( self, vmin, vmax ) :
	n = len( vmin )
	if n != self._nv :
		print( "ERROR: el vector de minimos es diferente que el número de variables" )

	n = len( vmax )
	if n != self._nv :
		print( "ERROR: el vector de maximos es diferente que el número de variables" )

	self.Limites = numpy.zeros( (2, self._nv) )
	self.vamplitud = numpy.zeros( self._nv )
	i = 0
	while i < self._nv :
		self.Limites[0][i] = vmin[i]
		self.Limites[1][i] = vmax[i]
		self.vamplitud[i] = vmax[i] - vmin[i]
		i += 1

def EvaluaPoblacion1( self ) :
	i = 0
	while i<self._pop :
		v = evalua.Evalua( self._nv, self.Pop[i] )
		self.Pop[i][self._nv] = v
		i += 1 

def GeneraNuevo1( self, indice ) :
	# Generamos tres nnumeros aleatorios enteros
	# en la población

	r1 = random.randint( 0, self._pop-1 )
	r2 = random.randint( 0, self._pop-1 )
	while r2==r1 :
		r2 = random.randint( 0, self._pop-1 )

	r3 = random.randint( 0, self._pop-1 )
	while r3==r1 or r3==r2 :
		r3 = random.randint( 0, self._pop-1 )


	irand = random.randint( 0, self._nv )

	i = 0
	# generamos el nuevo individuo
	while i < self._nv :
		if random.random() < self._cr or i==irand :
			d = self._cf*( self.Pop[r1][i] - self.Pop[r2][i] )
			self.vnuevo[i] = self.Pop[r3][i] + d

			# checar los límites
			if self.vnuevo[i] < self.Limites[0][i] :
				n = self.Limites[0][i] + random.random() * self.vamplitud[i]
				self.vnuevo[i] = n
	
			if self.vnuevo[i] > self.Limites[1][i] :
				n = self.Limites[0][i] + random.random() * self.vamplitud[i]
				self.vnuevo[i] = n
		else :
			self.vnuevo[i] = self.Pop[indice][i]

		i += 1
	

class ED:
	def __init__( self ) :
		self._pop = 0   # Tamaño de la población
		self._gen = 1   # Número de generaciones
		self._nv = 0    # Número de variables
		self._cf = 0.5  # Constante de deferencias
		self._cr = 1.0  # Constante de recombinación	

	PoneParametros = PoneParametros1 
	PoneLimites = PoneLimites1 
	Inicializa =  Inicializa1
	EvaluaPoblacion = EvaluaPoblacion1
	GeneraNuevo = GeneraNuevo1

	def EvaluaNuevo( self ) :
		self.vnuevo[self._nv] = evalua.Evalua( self._nv, self.vnuevo )

	def ComparaNuevo( self, indice ) :
		i = self._nv
		if self.vnuevo[i] < self.Pop[indice][i] :
			j = 0
			while j<=self._nv :
				self.Pop[indice][j] = self.vnuevo[j]
				j += 1

	def ImprimeMejor( self ) :
		v = self._nv
		miminimo = self.Pop[0][v]
		i = 1
		k = 0
		if self.Pop[i][v] < miminimo :
			miminimo = self.Pop[i][v]	
			k = i

		i = 0
		while i <= v :
			print( self.Pop[k][i], end=' ' )
			i += 1
		# print self.Pop[k]
		
		print( self.Pop[1][10])
