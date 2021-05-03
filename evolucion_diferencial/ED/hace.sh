# Ejecuta 100 veces la evolución diferencial:
#
rm -f sale
touch sale 
for (( i=0; i<100; i=i+1 ))
do
	echo $i
	python ./corre.py >> sale
done
