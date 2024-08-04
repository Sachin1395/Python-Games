s ="the sky is blue"
x = s.split()

x.reverse()
print(x)
p=""
for item in x :
    p+= " "+item
print(p.strip())