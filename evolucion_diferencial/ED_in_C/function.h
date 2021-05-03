double fnc(int D, double* X){
  double f = 0;
  int i;
  for (i=0; i<D-1; i++)
    f += 100*(X[i]*X[i]-X[i+1])*(X[i]*X[i]-X[i+1]) + (1-X[i])*(1-X[i]);
  return f;
}
