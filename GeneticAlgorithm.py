#from random import seed
from random import randint
#seed(1)
class Chromosome():
    def __init__(self):
        self.list=[]
        self.ff=0
        self.ps=0

    def setList(self,list):
        self.list=list
    def setff(self,ff):
        self.ff=ff
    def setPs(self,ps):
        self.ps=ps

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

def fitness_function(chromosome):
    sum=0
    for i in chromosome:
        if i==1:
            sum=sum+1
    return sum


Gen_number=20
Quantity_initial_poblation=100
cross_over_probability=0.7
mutation_probability=0.001
initial_poblation=[]
for i in range(Quantity_initial_poblation):
    chromosome=Chromosome()
    chromosome.list=generate_random_cromosome(Gen_number)
    chromosome.ff=fitness_function(chromosome.list)
    initial_poblation.append(chromosome)


for i in range(Quantity_initial_poblation):
    print(initial_poblation[i].list, initial_poblation[i].ff)



