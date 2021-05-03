%%
clear;
close;
clc;

h = 0.001;
t = 0:h:1000;
x = zeros(size(t));
y = zeros(size(t));
z = zeros(size(t));

%% asignacion de condicion inicial
ini_cond = [0.3 0.4 0.5]';         % Condiciones iniciales
x(1) = ini_cond(1);
y(1) = ini_cond(2);
z(1) = ini_cond(3);

for i = 2:length(x) 
    x(i) = x(i-1) + x_state(x(i-1),y(i-1),z(i-1))*h;
    y(i) = y(i-1) + y_state(x(i-1),y(i-1),z(i-1))*h;
    z(i) = z(i-1) + z_state(x(i-1),y(i-1),z(i-1))*h;
end

plot(x,y)
grid on; grid minor;

%% Funciones oscilador caotico
function R = x_state(x,y,z)
    R = y;
end

function R = y_state(x,y,z)
    R = z;
end

function R = z_state(x,y,z)
    a = 0.7;
    b = 0.7;
    c = 0.7;
    d = 0.7;
    m = 0.1;
    R = -a*x -b*y -c*z+ d*sat_fun_k(x,m,2,1);
end
