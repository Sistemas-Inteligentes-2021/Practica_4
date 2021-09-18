def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def crossover(crz,cra):
    halfz1,halfz2 = split_list(crz)
    halfa1,halfa2 = split_list(cra)
    crz=[]
    cra=[]
    crz.extend(halfz1)
    crz.extend(halfa2)
    cra.extend(halfa1)
    cra.extend(halfz2)
    return crz,cra

crx=[0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0]
cry=[1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0]

crz,cra = crossover(crx,cry)

print(crx,cry)
print(crz,cra)
