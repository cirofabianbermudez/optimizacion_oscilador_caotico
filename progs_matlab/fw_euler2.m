%%
clear;
close;
clc;

inicio = 0;
final = 1000;
h = 1e-3;
t = (inicio:h:final).';
y = zeros(max(size(t)),3);
y(1,:) =  [0.3 0.4 0.5];
for i = 2:length(t)
   y(i,:) = y(i-1,:) + h*fun_osc(y(i-1,:));  
end

%%
plot(y(:,1),y(:,2));
grid on;
grid minor;

