with open('Xout.txt') as f:
    f_contents = f.readlines()
    
kaplan = f_contents[5]
v = kaplan[-9:-1]
t = -float(v) 
print(t)
    
    
