#from random import seed
from random import randint

#seed(1)

def generate_random_cromosome(Gen_number):
    cromosome=[]
    for i in range(Gen_number):        
        cromosome.append(randint(0, 1))
    return cromosome

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


Gen_number=20
Quantity_initial_poblation=100
cross_over_probability=0.7
mutation_probability=0.001
initial_poblation=[]
for i in range(Quantity_initial_poblation):
    initial_poblation.append(generate_random_cromosome(Gen_number))


for i in range(Quantity_initial_poblation):
    print(initial_poblation[i])



