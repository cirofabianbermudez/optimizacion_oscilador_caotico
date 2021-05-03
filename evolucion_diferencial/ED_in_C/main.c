#include <stdio.h>
#include "rand.h"		// random number generator
#include "function.h"		// objective function (fitness)

// ** CONTROL PARAMETERS ** //
#define D	10		// dimension of problem
#define NP 	60		// size of population
#define F 	0.9		// differentiation constant
#define CR 	0.5		// crossover constant
#define GEN 	10000		// number of generations
#define L 	-2.048		// low boundary constraint
#define H 	2.048		// high boundary constraint

int main(void) {
//***************************//
//** ALGORITHM’S VARIABLES **//
//***************************//

double X[D];			// trial vector
double Pop[D][NP];		// population
double Fit[NP];			// fitness of the population
double f;			// fitness of the trial individual
int iBest = 0;			// index of the best solution
int i,j,g;			// loop variables
int Rnd;			// mutation parameter
int r[3];			// randomly selected indices

//****************************//
//** CREATION OF POPULATION **//
//****************************//

ini_rand(654987654UL);		// initialize rand
for(j=0; j<NP; j++){		// initialize each individual
  for(i=0; i<D; i++)		// within boundary constraints
    Pop[i][j] = X [i] = L + (H-L)*rand() ;
  Fit[j] = fnc(D,X); 		// and evaluate fitness function
}

//******************//
//** OPTIMIZATION **//
//******************//

for(g=0; g<GEN; g++){		// for each generation

  for (j=0; j<NP; j++){		// for each individual
				// choose three random individuals from population,
				// mutually different and also different from j
    r[0] = (int) (rand()*NP);
    while(r[0]==j)
      r[0] = (int) (rand()*NP);

    r[1] = (int) rand()*NP;
    while((r[1]==r[0])||(r[1]==j))
      r[1] = (int) (rand()*NP);

    r[2] = (int) (rand()*NP);
    while((r[2]==r[1])||(r[2]==r[0])||(r[2]==j))
      r[2] = (int) (rand()*NP);
    // create trial individual
    // in which at least one parameter is changed
    Rnd = (int)(rand()*D);

    for(i=0; i<D; i++){
      if( (rand()<CR) || (Rnd == i) )
	X[i] = Pop[i][r[2]] + F * (Pop[i][r[0]] - Pop[i][r[1]]);
      else
	X[i] = Pop[i][j];
    }
    // verify boundary constraints
    for(i=0; i<D; i++)
      if((X[i]<L)||(X[i]>H))
	X[i] = L + (H-L)*rand();
    // select the best individual
    // between trial and current ones
    // evaluate fitness of trial individual
    f = fnc(D,X) ;
    // if trial is better or equal than current
    if(f <= Fit[j]){
      // replace current by trial
      for(i=0; i<D; i++)
	Pop[i][j] = X[i];
      Fit[j] = f;

      // if trial is better than the best
      if(f <= Fit[iBest])
	iBest = j;	// update the best’s index
    }
  }
}

//*************//
//** RESULTS **//
//*************//

printf("OPTIMUM : \n");
for(i=0; i<D; i++)
  printf("%g\n",Pop[i][iBest]);
printf("Fobj = %g\n",Fit[iBest]);

scanf("%hd",&i);
return 0;
}
