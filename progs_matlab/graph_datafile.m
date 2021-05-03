clear;
close;
clc;

file_name = 'gl_output.txt';
data = load(file_name);

t = data(:,1);
x = data(:,2);
y = data(:,3);
z = data(:,4);

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
