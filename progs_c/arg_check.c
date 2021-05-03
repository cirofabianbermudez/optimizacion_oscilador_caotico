#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <errno.h>
#include <limits.h>

#define tn	1000.0			// Tiempo
#define	h	0.01			// Paso de integracion
#define k 	round(tn/h)		// Numero de iteraciones
#define alpha	1.0			// Orden fraccionario
#define	lm	tn*0.5			// Tamanio de memoria en porcentaje
#define m	lm/h			// Ventana de memoria en iteraciones

void conversion(char *str, double *x){
  char *endptr = NULL;
  errno = 0;
  *x = strtod(str, &endptr);
  printf("endprt = %d, errno = %d\n", *endptr, errno);
  if(*endptr!=0 || errno){		// Cuando no hay error *endprt es cero
    if(errno==ERANGE){
      printf("Conversion our of range!\n");
      exit(1);
    }
      printf("Error ocurred at %s\n",endptr);
      exit(1);
  }

}

int main(int argc, char **argv){
  
  if(argc != 5){
	printf("4 arguments needed\n");
	exit(1);
  }

  double a,b,c,d;

  conversion(argv[1],&a);
  conversion(argv[2],&b);
  conversion(argv[3],&c);
  conversion(argv[4],&d);


 // a = strtod(argv[1], NULL);
 // b = strtod(argv[2], NULL);
 // c = strtod(argv[3], NULL);
 // d = strtod(argv[4], NULL);
  
 // a = atof(argv[1]);
 // b = atof(argv[2]);
 // c = atof(argv[3]);
 // d = atof(argv[4]);

  printf("a = %lf, b = %lf, c = %lf, d = %lf\n", a,b,c,d);
  int i, j, v;
  printf("tn = %lf, h = %lf, k = %lf, lm = %lf, m = %lf\n", tn, h, k, lm, m);




  return 0;
}
