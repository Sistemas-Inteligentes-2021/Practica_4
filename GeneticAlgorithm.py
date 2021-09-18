#from random import seed
from random import randint

#seed(1)

def generate_random_cromosome(Gen_number):
    cromosome=[]
    for i in range(Gen_number):        
        cromosome.append(randint(0, 1))
    return cromosome




Gen_number=20
Quantity_initial_poblation=100
cross_over_probability=0.7
mutation_probability=0.001
initial_poblation=[]
for i in range(Quantity_initial_poblation):
    initial_poblation.append(generate_random_cromosome(Gen_number))


for i in range(Quantity_initial_poblation):
    print(initial_poblation[i])



