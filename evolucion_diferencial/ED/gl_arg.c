#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <errno.h>
#include <limits.h>

// Parametros de GL
// Cambiar ENABLE una vez calculados K y M
#define ENABLE	1	// 1 ejecuta GL, 0 ejecuta calculo de parametros K y M
#define K	50000	// Numero de iteraciones
#define M	40000	// Ventana de memoria en iteraciones

// Comprobacion de parametros de entrada
void conversion(char *str, double *x){
  char *endptr = NULL;
  errno = 0;
  *x = strtod(str, &endptr);
  //printf("endprt = %d, errno = %d\n", *endptr, errno);
  if(*endptr!=0 || errno){		// Cuando no hay error *endprt es cero
    if(errno==ERANGE){
      printf("Conversion our of range!\n");
      exit(1);
    }
      printf("Error ocurred at %s\n",endptr);
      exit(1);
  }

}

int max(int tam, double arr[]){
  int i;
  double max = arr[0];
  for(i = 1; i < tam; i++){
    if(arr[i] > max)
      max = arr[i];
  }
  return max;
}

int min(int tam, double arr[]){
  int i;
  double min = arr[0];
  for(i = 1; i < tam; i++){
    if(arr[i] > min)
      min = arr[i];
  }
  return min;
}

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

double z_state(double x, double y, double z, double a, double b, double c, double d){
  double m;
  //double a, b, c, d, m;
  //a = 0.7;
  //b = 0.7;
  //c = 0.7;
  //d = 0.7;
  m = 0.1;
  return(-a*x - b*y - c*z + d*sat_fun_k(x,m,2.0,1.0));
}


// Variables globales inicializadas todas en cero
  double x[K+1] = {0};
  double y[K+1] = {0};
  double z[K+1] = {0};
  double Cj[K+1] = {0};


int main(int argc, char **argv){
  clock_t tic = clock();	// iniciar cuenta de tiempo
  
  // Comprobacion de numero de parametros
  if(argc != 6){
	printf("5 arguments needed, last is the output filename.\n");
	exit(1);
  }

  // Conversion y prueba de parametros de entrada
  double a,b,c,d;
  conversion(argv[1],&a);
  conversion(argv[2],&b);
  conversion(argv[3],&c);
  conversion(argv[4],&d);
  printf("Output file: %s\n",argv[5]);
  printf("Input parameters:\na = %lf, b = %lf, c = %lf, d = %lf\n", a,b,c,d);

  // Parametros de GL
  double tn = 500;		// Tiempo
  double h = 0.01;		// Paso de integracion
  double k = round(tn/h);	// Numero de iteraciones
  double alpha = 1.0;		// Orden fraccionario
  double lm = tn*0.8;		// Tamanio de memoria en porcentaje
  double m = lm/h;		// Ventana de memoria en iteraciones
  printf("tn: time, h: int_step, k: num_iter, lm: win_time, m: num_iter_win\n");
  printf("tn = %lf, h = %lf, k = %lf, lm = %lf, m = %lf\n", tn, h, k, lm, m);

  if(ENABLE == 0){
    printf("Modifica ENABLE a 1 e ingresa los pametros de K y M, despues ejecuta make.\n");
    exit(0);
  }

  // Variables auxiliares
  int i, j, v;
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
    z[i] = z_state(x[i-1],y[i-1],z[i-1],a,b,c,d)*pow(h,alpha) - zt;
  } 

  //Comprobar si atractor convergue
 // double max_value = max(K+1,x);
 // double min_value = min(K+1,x);
 // if(max_value > 50.0 || min_value < -50.0){
 //   printf("El atractor no converge!.\n");
 //   exit(1);
 // }


  // Archivo de texto
  FILE *fpointer = fopen(argv[5],"w");


 // Pasar datos a archivo de texto 
  for(i = 0; i < K+1; i++){
    fprintf(fpointer,"%.6lf\t%.6lf\t%.6lf\n",x[i], y[i], z[i]);
  }

  fclose(fpointer);
  clock_t toc = clock();
  printf("Elapsed: %f seconds\n", (double)(toc - tic) / CLOCKS_PER_SEC);

  return 0;
}
