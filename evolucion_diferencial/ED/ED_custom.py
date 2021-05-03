# Librerias
import numpy as np
import random as rand
import pandas as pd
import subprocess
import os


def check_infy(lim_L, lim_H) :
    data = pd.read_csv('gl_output.txt', sep = '\t', header = None)
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
            if state >= factor:
                break
            if abs(t-told) < tolerance : #tolerance
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

def lyap_spec()
    command = 'time ./lyap_spec gl_output.txt -x30000 -m3,1 -k50 -oXout.txt'
    os.system(command)
    return 0

def tisean_eval():
    with open('Xout.txt') as f:
        f_contents = f.readlines()
    
    kaplan = f_contents[5]
    v = -float(kaplan[-9:-1])
    return v


def func(X) :
    n = len(X)
    f = 0.0
    # Rosenbrock function
   # for i in range(n-1) :
   #     f  = f + 100.0*( X[i,0]*X[i,0] - X[i+1,0])**2 + (1.0 - X[i,0])**2;


    for i in range(n) :
        f = f + (X[i,0])**2

    return f

# Control parameters
D = 4             # dimension of problem
NP = 10             # size of population 
F = 0.9             # differentiation constant
CR = 0.5            # crossover constant
GEN = 10          # number of generations

#L = -2.048          # Low boundary constraint
#H = 2.048           # high boundary constraint

L = 0.01          # Low boundary constraint
H = 1.0           # high boundary constraint

# Algorithms variables
X = np.zeros((D,1))             # Trial vector
Pop = np.zeros((D,NP))          # Population
Fit = np.zeros((1,NP))          # Fitness of population
iBest = 0                       # index of the best solution
r = np.zeros((3,1), dtype=int)  # randomly selected indices

# Create population
j = 0
while j < NP :
    Pop[:,j:j+1] = L + (H-L)*np.random.random((D,1))
    # Calcular comando de GL
    command = './gl '
    for k in range(D):
        if k == D-1 :
            command = command + str(Pop[k][j])
        else:
            command = command + str(Pop[k][j]) + ' '
    #print(command)
    # comprobar que es oscilador es candidato con GL
    os.system(command)
    t1 = check_infy(-50.0,50.0)
    t2 = check_stable(100,1e-6)
    #print('El oscilador: ' + str(t))
    if t1 == 0 and t2 == 0:
        print('\tBUEN OSCILADOR')
        #Fit[0,j] = func(Pop[:,j:j+1])
        lyap_spec()
        Fit[0,j] = tisean_eval() 
        print(Fit[0,j])
        j += 1
    else:
        print('\tMAL OSCILADOR, REPITE')

#Optimization
for g in range(GEN) :       # for each individual
    for j in range(NP) :      # for each individual
        # choose three random individuals from population,
        # mutually different and different from j
        r[0][0] = rand.randint(0, NP -1)
        while r[0][0] == j :
            r[0][0] = rand.randint(0, NP -1)

        r[1][0] = rand.randint(0, NP -1)
        while (r[1][0]==r[0][0]) or (r[1][0]==j)  :
            r[1][0] = rand.randint(0, NP -1)

        r[2][0] = rand.randint(0, NP -1)
        while (r[2][0]==r[1][0]) or (r[2][0]==r[0][0])  or (r[2][0]==j)  :
            r[2][0] = rand.randint(0, NP -1)
        # Create trial individual
        # in which at least one parameter is changed
        Rnd = rand.randint(0, D)
        for i in range(D) :
            if rand.random() < CR or Rnd == i :
                #X[i,0] = Pop[i,r[2,0]] + F * (Pop[i,r[0,0]] - Pop[i,r[1,0]] )
                X[i][0] = Pop[i][r[2][0]] + F * (Pop[i,r[0][0]] - Pop[i,r[1][0]] )
            else :
                X[i][0] = Pop[i][j]

        # verify boundary contraints
        for i in range(D) :
            if X[i][0] < L or X[i][0] > H :
                X[i][0] = L + (H-L)*rand.random()
        
        # select the best individual
        # between trial an current ones
        # calculate fitness of trial individual
        f = func(X)
        # if trial is better or equal than current
        if f <= Fit[0][j] :
            Pop[:,j:j+1] = X
            # replace current by trial
            Fit[0][j] = f;
            # if trial is better than the best
            if f <= Fit[0][iBest] :
                iBest = j

# Results
f = Fit[0][iBest]
X = Pop[:,iBest:iBest+1]
print(X)
print(f)
