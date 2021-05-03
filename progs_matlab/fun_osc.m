function R = fun_osc(x)
     
    a = 0.7;
    b = 0.7;
    c = 0.7;
    d = 0.7;
    m = 0.1;
    f1_dot = x(2);
    f2_dot = x(3);
    f3_dot = -a*x(1) -b*x(2) -c*x(3)+ d*sat_fun_k(x(1),m,2,1); 
    R = [f1_dot f2_dot f3_dot];
end
