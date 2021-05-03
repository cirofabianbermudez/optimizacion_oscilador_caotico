import subprocess
filename = 'Xout.txt'
line = subprocess.check_output(['tail', '-1', filename])
    
kaplan = line
print(str(kaplan[-9:-1]))
    
    
print(kaplan)
