# Imports
from random import randint
from random import randrange
from random import choices
from random import random

# Global Vars
number_genes=20
quantity_population=100

crossover_probability=0.7
mutation_probability=0.001

# Generate [1, 1, 1, 1, ... ]
def generate_objetive_chromosome():
    chrom = [1] * number_genes
    return chrom

# Generate [random (0,1), ...]
def generate_random_cromosome():
    cromosome = []
    for i in range(number_genes):        
        cromosome.append(randint(0, 1))
    return cromosome

# Crossover: Get 2 new Chromosome
def crossover(crx,cry):
    middle = int(number_genes/2)
    if random()<=crossover_probability:
        crx1=crx[:middle]+cry[middle:]
        cry1=cry[:middle]+crx[middle:]
        return crx1,cry1
    return crx,cry

# Crossover: Get 2 new Chromosome
def crossover_random(crx,cry):
    middle = randint(1,number_genes-1)
    if random()<=crossover_probability:
        crx1=crx[:middle]+cry[middle:]
        cry1=cry[:middle]+crx[middle:]
        return crx1,cry1
    return crx,cry

# Mutation: Change a Random bit in Chromosome
def mutation(chromosome_crossover):
    if random()<=mutation_probability:
        random_position =  randrange(number_genes)
        chromosome_crossover[random_position] = 1 if chromosome_crossover[random_position] == 0 else 0
        return chromosome_crossover
    return chromosome_crossover

# Mutation_Both: Change a Random bit in Chromosome 
def mutation_both(c1, c2):
    if random()<=mutation_probability:
        random_position =  randrange(number_genes)
        c1[random_position] = 1 if c1[random_position] == 0 else 0
        c2[random_position] = 1 if c2[random_position] == 0 else 0
        return c1,c2
    return c1,c2  

# Fitness: Sumatory Gens in Chromosome
def fitness_function(chromosome):
    return sum(chromosome)

# Selection: Get 2 Chromosomes of Population
def selection(poblation,ff):    
    items = choices(poblation, weights=ff, k=2)
    return list(items[0]),list(items[1])

def run_first_generation(quantity_population,objective_chromosome):
    find_chromosome_objetive=False
    initial_poblation=[]
    ff=[]
    for i in range(quantity_population):                        #Generate the N  number of chromosomes
        chromosome=generate_random_cromosome()
        initial_poblation.append(chromosome)                    #Generate the chromosome
        ff_chromosome=fitness_function(chromosome)
        ff.append(ff_chromosome)                                #Finde his Fitness function
        find_chromosome_objetive = ff_chromosome==objective_chromosome
    return initial_poblation,ff,find_chromosome_objetive

def genetic_algorithm(quantity_population,max_run_cycles):
    average=0
    objective_chromosome_sum=number_genes
    for i in range(max_run_cycles) :
        cycle=1
        initial_poblation,ff,find_chromosome_objetive=run_first_generation(quantity_population,objective_chromosome_sum) #First Generation 

        while  not find_chromosome_objetive:  #Check if the goalChrom is not generate in initial Generation  
            cycle=cycle+1
            new_generation=[]
            newff=[]
            while len(new_generation)<len(initial_poblation):
                crx,cry=selection(initial_poblation,ff)

                crx,cry=crossover_random(crx,cry)

                #crx=mutation(crx)
                #cry=mutation(cry)

                crx, cry= mutation_both (crx,cry)

                ffx=fitness_function(crx)
                ffy=fitness_function(cry)
                newff.append(ffx)
                newff.append(ffy)
                new_generation.append(crx)
                new_generation.append(cry)
                find_chromosome_objetive= ffx== objective_chromosome_sum or ffy==objective_chromosome_sum
            initial_poblation= new_generation
            ff=newff
        print(i, cycle)
        average=average+cycle
    return average/max_run_cycles


if __name__ == "__main__" :
    max_run_cycles=int(input("Insert the quantity of cycle you want to do the algorithm: \n"))
    average_cycle=genetic_algorithm(quantity_population,max_run_cycles)
    print("The experiment find the best solution in the average of ", average_cycle,"generations")
