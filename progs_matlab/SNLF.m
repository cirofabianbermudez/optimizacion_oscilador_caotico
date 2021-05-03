function xdot = SNLF(t,x)
%     m = 3;
%     n = 1;
%     xdot(1) = (-m/4)*sin(5*n*x(3));
%     xdot(2) = -8*x(1)^2 - x(2);
%     a = 8/5;
%     b = 7/5;
%     xdot(3) = a/5 + (4*b*x(1))/(5) + (2*x(2))/(5);
    
    a = 0.7;
    b = 0.7;
    c = 0.7;
    d = 0.7;
    m = 0.1;
    xdot(1) = x(2);
    xdot(2) = x(3);
    xdot(3) = -a*x(1) -b*x(2) -c*x(3)+ d*sat_fun_k(x(1),m,2,1);
    xdot = xdot';

end