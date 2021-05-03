clear;
close;
clc;

%% Utilizacion de FDE12.m
alpha = 1; t0 = 0; tfinal = 1000; h = 0.01;
y0 = [0.3 0.4 0.5]'; 
[t, y_fde12] = fde12(alpha,'SNLF',t0,tfinal,y0,h) ;

figure(1)
plot(y_fde12(1,:), y_fde12(2,:) ) ;
xlabel('y1') ; ylabel('y2') ;
title('FDE solved by the FDE12.m code') ;



