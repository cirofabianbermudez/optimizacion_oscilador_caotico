%%
clear;
close;
clc;

%% Comprobacion de GL numerico
alpha = 1;
t0 = 0;
tfinal = 1000;
h = 0.01;
y0 = [0.3 0.4 0.5]'; 

[t, y_fde12] = fde12(alpha,'SNLF',t0,tfinal,y0,h) ;
x = y_fde12(1,:);
y = y_fde12(2,:);
z = y_fde12(3,:);

%% Graficar
plot(y,x);
grid on;
grid minor;
xlabel('x_1'); 
ylabel('x_2');
title('FDE solved by the FDE12.m code') ;


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
% data = [t.' y_fde12.'];
% csvwrite('FDE12_data1.csv',data);

%% Escribir a archivo de texto
% fileID = fopen('gl_output.txt','w');
% for i= 1:length(x)
% fprintf(fileID,'%5.8f %5.8f %5.8f\n',x(i),y(i),z(i));
% end
% fclose(fileID);
