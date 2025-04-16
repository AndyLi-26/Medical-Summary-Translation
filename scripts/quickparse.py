s='''
0.685745816	0.744072695	0.7118488173	0.7059234392	0.7325217087
0.5493715543	0.6054525741	0.6129926929	0.5861539087	0.625168901
0.4652498297	0.4787032853	0.539867683	0.5221585821	0.574383188
'''
opt=s.strip().split("\n")
opt=[i.split("\t") for i in opt]

print("value1=[")
for i in opt:
    print("[",end="")
    for j in i:
          if j == i[-1]:
            print(j,end="")
          else:
            print(j,end=", ")
    if i == opt[-1]:
        print("]")
    else:
        print("],")
print("]")
