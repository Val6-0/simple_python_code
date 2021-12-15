
f = open("input.txt")
x = list(map(int,f.readlines()))
#print (x)
old = -1
measurement = 0
for e in x :
    if old == -1 :
        old = e
        continue
    if e > old :
        #print ("increased")
        measurement += 1
    else :
        #print ("decreased")
        pass
    old = e
print(measurement)
