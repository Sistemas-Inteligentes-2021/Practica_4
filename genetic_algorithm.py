# Imports
from random import randint
from random import randrange
from random import choices
from random import random

def generate_objetive_chromosome(length):
    chrom = [1] * length
    return chrom

def generate_random_cromosome(length):
    cromosome = []
    for i in range(length):        
        cromosome.append(randint(0, 1))
    return cromosome


def crossover(crx,cry,crossover_prob,length):
    middle = int(length/2)
    if random()<=crossover_prob:
        crx1=crx[:middle]+cry[middle:]
        cry1=cry[:middle]+crx[middle:]
        return crx1,cry1
    return crx,cry

# Mutation: Change a Random bit
def mutation(chromosome_crossover,length):
    if random()<=mutation_probability:
        random_position =  randrange(length)
        chromosome_crossover[random_position] = 1 if chromosome_crossover[random_position] == 0 else 0
        return chromosome_crossover
    return chromosome_crossover

def fitness_function(chromosome):
    return sum(chromosome)

# With choices
def selection(poblation,ff):    
    items = choices(poblation, weights=ff, k=2)
    return items[0],items[1]


def compare_chromosome(chromosome,goal_chromosome):
    for i in range(len(goal_chromosome)):
        if goal_chromosome[i]!=chromosome[i]:
            return False
    return True

def print_Initial_Poblation(pob):
    for i in pob:
        print( i.list)

def run_first_generation(Gen_number,Quantity_initial_poblation,objective_chromosome):
    find_chromosome_objetive=False
    initial_poblation=[]
    ff=[]
    for i in range(Quantity_initial_poblation):                     #Generate the N  number of chromosomes
        chromosome=generate_random_cromosome(Gen_number)
        initial_poblation.append(chromosome)       #Generate the chromosome
        ff_chromosome=fitness_function(chromosome)
        ff.append(ff_chromosome)             #Finde his Fitness function
        find_chromosome_objetive = ff_chromosome==objective_chromosome
    return initial_poblation,ff,find_chromosome_objetive

def genetic_algorithm(Gen_number,Quantity_initial_poblation,cross_over_probability,mutation_probability,max_run_cycles):
    average=0
    objective_chromosome=Gen_number
    for i in range(max_run_cycles) :
        cycle=1
        #First Generation        
        initial_poblation,ff,find_chromosome_objetive=run_first_generation(Gen_number,Quantity_initial_poblation,objective_chromosome)

        while  not find_chromosome_objetive:  #Check if the goalChrom is not generate in initial Generation  
            cycle=cycle+1
            new_generation=[]
            newff=[]
            while len(new_generation)<len(initial_poblation):     
                           
                crx,cry=selection(initial_poblation,ff)
                # crx=copy.deepcopy(crxi);
                # cry=copy.deepcopy(cryi);
                crx,cry=crossover(crx,cry,cross_over_probability,Gen_number)
                crx=mutation(crx,Gen_number)
                cry=mutation(cry,Gen_number)
                ffx=fitness_function(crx)
                ffy=fitness_function(cry)
                newff.append(ffx)
                newff.append(ffy)
                new_generation.append(crx)
                new_generation.append(cry)
                find_chromosome_objetive= ffx == objective_chromosome or ffy==objective_chromosome
            initial_poblation= new_generation
            ff=newff
        average=average+cycle
    return average/max_run_cycles


Gen_number=10
Quantity_initial_poblation=100
cross_over_probability=0.7
mutation_probability=0.001

max_run_cycles=int(input("Insert the quantity of cycle you want to do the algorithm: \n"))
average_cycle=genetic_algorithm(Gen_number,Quantity_initial_poblation,cross_over_probability,mutation_probability,max_run_cycles)
print("the experiment find the best solution in the average of ", average_cycle,"generations")

