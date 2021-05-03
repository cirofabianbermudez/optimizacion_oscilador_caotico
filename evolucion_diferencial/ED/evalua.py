import math
import os
import subprocess



# def Evalua( _n, vpar ) :
	# suma = 0
	# for i in range(_n):
		# suma = suma +  (vpar[i]-2)*(vpar[i]-5) + math.sin( 1.5*math.pi*vpar[i])
		# v = 0.1*suma
	# return v


def Evalua( _n, vpar ) :
	a = vpar[0]
	b = vpar[1]
	c = vpar[2]
	d = vpar[3]
	command = './gl ' + str(a) + ' '+  str(b) + ' ' + str(c) + ' ' + str(d);
	os.system(command)
	command = 'time ./lyap_spec3 gl_output.txt -x30000 -m3,1 -k30 -oXout.txt'
	os.system(command)
	#command = 'tail -n 1 Xout.txt '
	#s = os.system(command)
	
	with open('Xout.txt') as f:
		f_contents = f.readlines()
		kaplan = f_contents[-1]
    
	return -float(kaplan[-9:-1])

# incluir parametro k
a = Evalua(4,[0.7,0.7,0.7,0.7])
print(a)
