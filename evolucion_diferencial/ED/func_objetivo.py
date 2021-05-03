import math
import os
import subprocess
import pandas as pd
#f = os.popen('date')
#now = f.read()
#print("Hola" + now)
#p = subprocess.Popen(["date"], stdout=subprocess.PIPE)
#output, err = p.communicate()

#os.system("ls");
#a = 0.7
#command = "./gl " + str(a) + " " + str(a) + " " + str(a) + " " + str(a)
#os.system(command);
data = pd.read_csv('gl_output.txt',sep = "\t", header = None)
print(data)
#print(data[2][0])         # Tiene el formato de [columa][renglon]
rows, columns = data.shape

# i = 0
# state = 0
# print(rows)
# print(columns)
# print("\n")
# while i < columns:
	# j = 0
	# while j < rows:
		# t = data[i][j]
		# print(t)
		# if t > 50.0 or t < -50:
			# state = 1
			# break
		# j += 1
	# if state == 1:
		# break
	# i += 1

# if state == 1:
	# print('Fuera de los rangos')
	


def check_stable(factor,tolerance):
	data = pd.read_csv('gl_output.txt', sep = '\t', header = None)
	rows, columns = data.shape
	told = data[0][0] + 1
	state = 0
	i = 0
	while i < columns:
		j = 0
		state = 0
		while j < rows:
			t = data[i][j]
			#print(t)
			if state >= factor:
				break
			if abs(t-told) < tolerance : #tolerance
				print(told)
				print(t)
				print(abs(t-told))
				print(state)
				state += 1
			else:
				state = 0
			told = t
			j += 1
		if state >= factor:
			break
		i += 1
	if state != factor:
		state = 0
	else:
		state = 1
	return state


print(check_stable(100,1e-6))
