na = []
gl = "u"
sz = 5
import random
while gl != "t":
    na.clear()
    for i in range (sz):
        na.append(random.randint(1,100))        
    gl = "u"   
    for j in range (sz-1):
        if na[j] < na[j+1]:
            gl = "f"            
        else:
            if gl == "u":
                gl = "t"
na.append(101)
for i in range (sz):
    if na[i] != na[i+1]:
        print(na[i])
