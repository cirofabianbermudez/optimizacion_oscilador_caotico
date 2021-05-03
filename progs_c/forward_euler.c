#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define SIZE 1000000	// es necesario cambiarlo dependiendo del calculo de tam

// Funcion de saturacion
double fo(double x, double m, double h, double k){
  double R;
  if( x < -m )
    R = -1.0*k;
  else if( -m<=x && x<=m )
    R = (x/m)*k;
  else 
    R = 1.0*k;

  return R;
}

double fh(double x, double m, double h, double k){
  double R;
  if( x > h+m )
    R = 2.0*k;
  else if( -m+h<=x && x<=m+h )
    R = ( (x-h)/m + 1.0)*k;
  else 
    R = 0.0;

  return R;
}

double f_h(double x, double m, double h, double k){
  double R;
  if( x > h+m )
    R = 0.0;
  else if( -m+h<=x && x<=m+h )
    R = ( (x-h)/m - 1.0)*k;
  else 
    R = -2.0*k;

  return R;
}

double sat_fun_k(double x, double m, double s, double k){
  double R = 0.0, f = 0.0;
  int sub;
  for(int i = 0; i<=s-2; i++){
    sub = 2*i-s+2;
    if(sub == 0)
      f = fo(x,m,sub,k);
    else if(sub > 0)
      f = fh(x,m,sub,k);
    else
      f = f_h(x,m,sub,k);

    R = R + f;
  }
  return R;
}

// Descripcion de ODE
double x_state(double x, double y, double z){
  return y;
}

double y_state(double x, double y, double z){
  return z;
}

double z_state(double x, double y, double z){
  double a, b, c, d, m, temp;
  a = 0.7;
  b = 0.7;
  c = 0.7;
  d = 0.7;
  m = 0.1;
  return(-a*x - b*y - c*z + d*sat_fun_k(x,m,2.0,1.0));
}




// Variables globales inicializadas todas en cero
  double x[SIZE+1] = {0};
  double y[SIZE+1] = {0};
  double z[SIZE+1] = {0};

int main(void){
  clock_t tic = clock();
  int i;
  double inicio = 0.0;
  double fin = 1000.0;
  double paso = 0.001;
  int tam = (fin - inicio)/paso + 1;	// Poner este valor en el #define de SIZE
  printf("num_iter = %d\n", tam);
  
  // Archivo de texto
  FILE *fpointer = fopen("fwe_output.txt","w");

  // Condiciones iniciales
  x[0] = 0.3;
  y[0] = 0.4;
  z[0] = 0.5;

  // Algoritmo Forward Euler
  for(i = 1; i < SIZE; i++){
    x[i] = x[i-1] + x_state(x[i-1],y[i-1],z[i-1])*paso;
    y[i] = y[i-1] + y_state(x[i-1],y[i-1],z[i-1])*paso;
    z[i] = z[i-1] + z_state(x[i-1],y[i-1],z[i-1])*paso;
  }

  
  // Imprimir datos
  for(i = 0; i < SIZE; i++){
    fprintf(fpointer,"%.6lf\t%.6lf\t%.6lf\n",x[i], y[i], z[i]);
  }

  fclose(fpointer);
  clock_t toc = clock();
  printf("Elapsed: %f seconds\n", (double)(toc - tic) / CLOCKS_PER_SEC);
  return 0;
}
