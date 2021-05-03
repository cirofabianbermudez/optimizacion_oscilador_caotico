# Librerias
import numpy as np
import random as rand
import os
import pandas as pd

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
D = 10              # dimension of problem
NP = 60             # size of population 
F = 0.9             # differentiation constant
CR = 0.5            # crossover constant
GEN = 5000          # number of generations

#L = -2.048          # Low boundary constraint
#H = 2.048           # high boundary constraint

L = -5.12          # Low boundary constraint
H = 5.12           # high boundary constraint

# Algorithms variables
X = np.zeros((D,1))             # Trial vector
Pop = np.zeros((D,NP))          # Population
Fit = np.zeros((1,NP))          # Fitness of population
iBest = 0                       # index of the best solution
r = np.zeros((3,1), dtype=int)  # randomly selected indices

# Create population
#for j in range(NP) : 
while j < NP
    Pop[:,j:j+1] = L + (H-L)*np.random.random((D,1))
    command = './gl '
    for k in range(D) :
        if k == D-1 :
            command = command + str(Pop[k][j])
        else :
            command = command + str(Pop[k][j]) + ' '

    os.system(command)

    Fit[0,j] = func(Pop[:,j:j+1])

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
