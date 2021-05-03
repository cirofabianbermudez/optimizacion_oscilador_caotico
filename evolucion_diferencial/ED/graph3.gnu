reset

unset key
set grid xtics ytics ls 3 lw 1 lc rgb 'gray'

#filename = 'gl_output.txt'
stats filename using 2 nooutput name 'Y_'
stats filename using 1 every ::Y_index_min::Y_index_min nooutput
X_min = STATS_min
stats filename using 1 every ::Y_index_max::Y_index_max nooutput
X_max = STATS_max

#set xrange[X_min:X_max]
#set yrange[Y_min:Y_max]
set xlabel 'x_{1}'
set ylabel 'x_{2}'
set zlabel 'x_{3}'
set title "Oscilador SNLF"
splot filename u ($1):($2):($3) t "Grafica" w l lc -1 lw 1
pause -1


