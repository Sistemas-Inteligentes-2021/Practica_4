from random import randint
from random import randrange

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

# Mutation: Change a Random bit
def mutation(chromosome_crossover):
    random_position =  randrange(20)
    chromosome_crossover[random_position] = 1 if chromosome_crossover[random_position] == 0 else 0
    return chromosome_crossover

def fitness_function(chromosome):
    sum=0
    for i in chromosome:
        if i==1:
            sum=sum+1
    return sum


Gen_number=5
Quantity_initial_poblation=10
cross_over_probability=0.7
mutation_probability=0.001
initial_poblation=[]
fitness_poblation=0
for i in range(Quantity_initial_poblation):
    chromosome=Chromosome()
    chromosome.list=generate_random_cromosome(Gen_number)
    chromosome.ff=fitness_function(chromosome.list)
    fitness_poblation=fitness_poblation+chromosome.ff
    initial_poblation.append(chromosome)

for chrom in initial_poblation:
    chrom.ps=chrom.ff/fitness_poblation

for i in range(Quantity_initial_poblation):
    print(initial_poblation[i].list, initial_poblation[i].ff,'/',fitness_poblation,'=',initial_poblation[i].ps )


