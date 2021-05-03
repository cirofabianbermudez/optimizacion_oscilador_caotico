#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define K	50000	// Numero de iteraciones totales
#define M    	5000	// Ventana de memoria

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
  double x[K+1] = {0};
  double y[K+1] = {0};
  double z[K+1] = {0};
  double Cj[K+1] = {0};


int main(void){
  clock_t tic = clock();
  int i, j, v;
  double tn = 500;		// Tiempo
  double h = 0.01;		// Paso de integracion
  double k = round(tn/h);	// Numero de iteraciones
  double alpha = 1.0;		// Orden fraccionario
  double lm = tn*0.1;		// Tamanio de memoria en porcentaje
  double m = lm/h;		// Ventana de memoria en iteraciones
  printf("tn = %lf, h = %lf,k = %lf,lm = %lf,m = %lf\n", tn, h, k, lm, m);

  // Variables auxiliares
  double xt, yt, zt;

  // Condiciones iniciales
  x[0] = 0.3;
  y[0] = 0.4;
  z[0] = 0.5;

  // Calculo de parametros Cj
  Cj[0] = 1;
  for(j = 1; j <= M; j++){		// sin memoria corta K, con memoria corta M
   Cj[j] = (1.0 - (alpha + 1.0)/(j)) * Cj[j-1];
  } 

  // Algoritmo de GL
  for(i = 1; i <= K; i++){
    xt = 0.0;
    yt = 0.0;
    zt = 0.0;

    // Principio de memoria corta
    if(i < M)
      v = i;
    else
      v = M;

    //printf("v = %d\n",v);
    
    // sin memoria corta
    //v = i;

    for(j = 1; j <= v; j++){
      xt = xt + Cj[j]*x[i-j];
      yt = yt + Cj[j]*y[i-j];
      zt = zt + Cj[j]*z[i-j];
    }

    x[i] = x_state(x[i-1],y[i-1],z[i-1])*pow(h,alpha) - xt;
    y[i] = y_state(x[i-1],y[i-1],z[i-1])*pow(h,alpha) - yt;
    z[i] = z_state(x[i-1],y[i-1],z[i-1])*pow(h,alpha) - zt;

  } 

  // Archivo de texto
  FILE *fpointer = fopen("gl_output.txt","w");


 // Pasar datos a archivo de texto 
  for(i = 0; i < K+1; i++){
    fprintf(fpointer,"%.6lf\t%.6lf\t%.6lf\n",x[i], y[i], z[i]);
  }

  fclose(fpointer);
  clock_t toc = clock();
  printf("Elapsed: %f seconds\n", (double)(toc - tic) / CLOCKS_PER_SEC);

  return 0;
}
