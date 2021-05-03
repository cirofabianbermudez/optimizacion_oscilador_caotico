%% 
clear all;
close all;
clc;
tic                              %Medir tiempo de ejecucion
%% Variables 
ini_cond = [0.3 0.4 0.5]';       % Condiciones iniciales
tn = 1000;                       % Tiempo 
h = 0.01;                        % Paso de integracion
k = round(tn/h);                 % Numero de iteraciones
alpha = 1;                       % Orden fraccionario
lm = (tn*0.8);                   % Tamanio de memoria
M =  lm/h;                       % Ventana de memoria
%% Inicializacion de vectores
x = zeros(k + 1, 1);
y = zeros(k + 1, 1);
z = zeros(k + 1, 1);
Cj = zeros(k + 1, 1);
A = zeros(3,1);
%% Primer elemento de los vectores
x(1) = ini_cond(1);
y(1) = ini_cond(2);
z(1) = ini_cond(3);
Cj(1) = 1;
%% Calculo coeficientes Cj
for j=1:M                               % Modificar k o M sin y con memoria corta
    Cj(j+1) = ( 1 - (alpha+1)/(j) ) * Cj(j);
end
for i=1:k
    A(:) = 0;
    %% Principio de memoria corta
    if i < M
        v = i;
    else
        v = M;
    end
    %% Sin memoria corta
%     v = i;
    for j=1:v
        A(1) = A(1) + Cj(j+1)*x(i+1-j);
        A(2) = A(2) + Cj(j+1)*y(i+1-j);
        A(3) = A(3) + Cj(j+1)*z(i+1-j);
    end
    x(i+1) = x_state(x(i),y(i),z(i))*h^(alpha) - A(1);
    y(i+1) = y_state(x(i),y(i),z(i))*h^(alpha) - A(2);
    z(i+1) = z_state(x(i),y(i),z(i))*h^(alpha) - A(3);
end
toc                              % Mostrar tiempo de ejecucion
%% Ver en R#
% plot3(x,y,z);
% xlabel('x(t)');
% ylabel('y(t)');
% zlabel('z(t)');

%% Ver grafica
plot(x,y);
grid on;
grid minor;
xlabel('x_1');
ylabel('x_2');
title('Oscilador caotico SNLF de 3 enrollamientos');

%% Mostrar en latex
% f = figure;
% p = 700;
% f.Position = [200 200 p p*(3/4)];
% plot(x,y,'k','LineWidth',1.5);
% grid on;
% grid minor;
% title('Oscilador ca\''otico SNLF de 3 enrollamientos','Interpreter','latex','FontSize',14);
% xlabel('$x_{1}$','Interpreter','latex','Color','black','FontSize',12);
% ylabel('$x_{2}$','Interpreter','latex','Color','black','FontSize',12);
% set(gca,'TickLabelInterpreter','latex', 'FontSize', 12);

%% Escribir a archivo de Excel CSV
% t = (0:h:tn).';
% data = [t x y z];
% csvwrite('GL_data1.csv',data);

%% Escribir a archivo de texto
% fileID = fopen('gl_output.txt','w');
% for i= 1:length(x)
% fprintf(fileID,'%5.8f %5.8f %5.8f\n',x(i),y(i),z(i));
% end
% fclose(fileID);
%% Funciones oscilador caotico
function R = x_state(x,y,z)
    R = y;
end

function R = y_state(x,y,z)
    R = z;
end

function R = z_state(x,y,z)
    a = 0.8;
    b = 0.5;
    c = 0.6;
    d = 0.7;
    m = 0.1;
    R = -a*x -b*y -c*z+ d*sat_fun_k(x,m,2,1);
end