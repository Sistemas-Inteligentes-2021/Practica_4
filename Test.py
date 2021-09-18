import copy

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def crossover(crx,cry):
    copyx=copy.deepcopy(crx)
    copyy=copy.deepcopy(cry)
    halfx1,halfx2 = split_list(copyx)
    halfy1,halfy2 = split_list(copyy)
    crz=[]
    cra=[]
    crz.extend(halfx1)
    crz.extend(halfy2)
    cra.extend(halfy1)
    cra.extend(halfx2)
    return crz,cra

crx=[0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0]
cry=[1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0]

crz,cra = crossover(crx,cry)

print(crx,cry)
print(crz,cra)
