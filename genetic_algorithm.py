from random import randint
from random import randrange
import copy
from numpy.random import choice
import random

class Chromosome():
    def __init__(self):
        self.list=[]
        self.ff=0
        #self.ps=0

    def setList(self,list):
        self.list=list
    def setff(self,ff):
        self.ff=ff
    def setPs(self,ps):
        self.ps=ps
def generate_objetiveChromosome(length):
    chrom=[]
    for i in range(length):
        chrom.append(1)
    return chrom


def generate_random_cromosome(Gen_number):
    cromosome=[]
    for i in range(Gen_number):        
        cromosome.append(randint(0, 1))
    return cromosome

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def crossover(crx,cry,crossover_prob):
    if random.random()<=crossover_prob:
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
    return crx,cry

# Mutation: Change a Random bit
def mutation(chromosome_crossover,mutation_prob,gen_quantity):
    if random.random()<=mutation_prob:
        random_position =  randrange(gen_quantity)
        chromosome_crossover[random_position] = 1 if chromosome_crossover[random_position] == 0 else 0
        return chromosome_crossover
    return chromosome_crossover

def fitness_function(chromosome):
    sum=0
    for i in chromosome:
        if i==1:
            sum=sum+1
    return sum

## With choices
# def selection(poblation):
#     weights = [i.ff for i in poblation]
#     items = random.choices(poblation, weights=weights, k=2)
#     return items[0],items[1]



## With choice
def selection(poblation):
    weights = [i.ps for i in poblation]
    total_weight=0
    for i in weights:
        total_weight=total_weight+i
    
    item1 = choice(poblation, p=weights)
    item2 = choice(poblation, p=weights)
    return item1,item2


def compare_chromosome(chromosome,goal_chromosome):
    for i in range(len(goal_chromosome)):
        if goal_chromosome[i]!=chromosome[i]:
            return False
    return True

def print_Initial_Poblation(pob):
    for i in pob:
        print( i.list)

def run_first_generation(Gen_number,Quantity_initial_poblation,objective_chromosome):
    fitness_poblation=0
    find_chromosome_objetive=False
    initial_poblation=[]
    for i in range(Quantity_initial_poblation): #Generate the N  number of chromosomes
        chromosome=Chromosome()
        chromosome.list=generate_random_cromosome(Gen_number) #Generate the chromosome
        chromosome.ff=fitness_function(chromosome.list)  #Finde his Fitness function
        fitness_poblation=fitness_poblation+chromosome.ff
        initial_poblation.append(chromosome)     #Added into the generation
        find_chromosome_objetive=find_chromosome_objetive or compare_chromosome(chromosome.list,objective_chromosome)
    return fitness_poblation,initial_poblation,find_chromosome_objetive

def run_experiment(Gen_number,Quantity_initial_poblation,cross_over_probability,mutation_probability,max_run_cycles):
    average=0
    objective_chromosome=generate_objetiveChromosome(Gen_number)
    for i in range(max_run_cycles) :
        print(i, "*************************************************************")
        cycle=1
        #First Generation
        fitness_poblation,initial_poblation,find_chromosome_objetive=run_first_generation(Gen_number,Quantity_initial_poblation,objective_chromosome)
        
        while  not find_chromosome_objetive:  #Check if the goalChrom is not generate in initial Generation  
            cycle=cycle+1
            for chrom in initial_poblation:                
                chrom.ps=chrom.ff/(fitness_poblation)    #Get the prob selection of the generation                  
            new_generation=[]
            fitness_poblation=0
            while len(new_generation)<len(initial_poblation):
                #print_Initial_Poblation(initial_poblation)
                crx=Chromosome()
                cry=Chromosome()
                crx,cry=selection(initial_poblation)
                crx.list,cry.list=crossover(crx.list,cry.list,cross_over_probability)
                crx.list=mutation(crx.list,mutation_probability,Gen_number)
                cry.list=mutation(cry.list,mutation_probability,Gen_number)
                crx.ff=fitness_function(crx.list)
                cry.ff=fitness_function(cry.list)
                fitness_poblation=fitness_poblation+crx.ff+cry.ff
                new_generation.append(crx)
                new_generation.append(cry)
                find_chromosome_objetive=find_chromosome_objetive or compare_chromosome(crx.list,objective_chromosome)
                find_chromosome_objetive=find_chromosome_objetive or compare_chromosome(cry.list,objective_chromosome)                        
            initial_poblation=copy.deepcopy( new_generation)
        average=average+cycle
    return average/max_run_cycles


Gen_number=5
Quantity_initial_poblation=10
cross_over_probability=0.7
mutation_probability=0.1

max_run_cycles=int(input("Insert the quantity of cycle you want to do the algorithm: \n"))
average_cycle=run_experiment(Gen_number,Quantity_initial_poblation,cross_over_probability,mutation_probability,max_run_cycles)
print("the experiment find the best solution in the average of ", average_cycle,"generations")

