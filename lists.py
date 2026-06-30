print("\033c\033[47;31m\lists\n")
maxs=20
l=[]
for a in range(maxs-1):
    b=maxs-a
    l.append([b,a])
l.sort()
print(l)