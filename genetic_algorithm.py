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

# Mutation_Both: Change a Random bit in Chromosome 
def mutation_both(chromosome_x, chromosome_y):
    if random()<=mutation_probability:
        random_position =  randrange(number_genes)
        chromosome_x[random_position] = 1 if chromosome_x[random_position] == 0 else 0
        chromosome_y[random_position] = 1 if chromosome_y[random_position] == 0 else 0
        return chromosome_x,chromosome_y
    return chromosome_x,chromosome_y  

# Fitness: Sumatory Gens in Chromosome
def fitness_function(chromosome):
    return sum(chromosome)

# Selection: Get 2 Chromosomes of Population
def selection(poblation,ff):    
    items = choices(poblation, weights=ff, k=2)
    return list(items[0]),list(items[1])

def run_first_generation(quantity_population,ff_objetive):
    find_chromosome_objetive=False
    initial_poblation=[]
    ff=[]
    for i in range(quantity_population):                        #Generate the N  number of chromosomes
        chromosome=generate_random_cromosome()
        initial_poblation.append(chromosome)                    #Generate the chromosome
        ff_chromosome=fitness_function(chromosome)
        ff.append(ff_chromosome)                                #Finde his Fitness function
        find_chromosome_objetive = ff_chromosome == ff_objetive
    return initial_poblation,ff,find_chromosome_objetive

# Compare: 2 Fitness Function with Fitness Function Objetive
def compare_chromosomes(ff_x, ff_y, ff_objetive):
    return ff_x == ff_objetive or ff_y == ff_objetive

# Execute: Selection, Crossover, Mutation
def execute_functions(initial_poblation, ff, ff_objetive, find_chromosome_objetive, cycle, i):
    while  not find_chromosome_objetive:  # Check if the goal Fitnes Function is not generate in initial Generation  
        cycle=cycle+1
        new_generation=[]
        new_ff=[]

        while len(new_generation)<len(initial_poblation):
            chromosome_x, chromosome_y= selection(initial_poblation,ff)                 # Selection
            chromosome_x, chromosome_y= crossover_random (chromosome_x, chromosome_y)   # Crossover
            chromosome_x, chromosome_y= mutation_both (chromosome_x, chromosome_y)      # Mutation

            ff_x=fitness_function(chromosome_x)                                         # Fitness Function chromosome_x
            ff_y=fitness_function(chromosome_y)                                         # Fitness Function chromosome_y

            new_ff.append(ff_x)                                                         # Add ff_x to New Fitness Function
            new_ff.append(ff_y)                                                         # Add ff_y to New Fitness Function

            new_generation.append(chromosome_x)                                         # Add chromosome_x to New Generation
            new_generation.append(chromosome_y)                                         # Add chromosome_y to New Generation

            find_chromosome_objetive = compare_chromosomes(ff_x, ff_y, ff_objetive)      # Compare with ff_objetive

        initial_poblation= new_generation
        ff=new_ff
    print("Cicle: " + str(i+1) +" - Generations: "+ str(cycle))
    return cycle

    
def genetic_algorithm(quantity_population,max_run_cycles):
    average= 0
    ff_objetive= number_genes

    for i in range(max_run_cycles) :
        cycle=1
        initial_poblation, ff, find_chromosome_objetive= run_first_generation(quantity_population,ff_objetive) # First Generation 
        average += execute_functions(initial_poblation, ff, ff_objetive, find_chromosome_objetive, cycle, i)   # Next Generations

    return average/max_run_cycles

# Main Function
def main():
    max_run_cycles=int(input("Insert the quantity of cycle you want to do the algorithm: "))
    average_cycle=genetic_algorithm(quantity_population,max_run_cycles)
    print("The experiment find the best solution in the average of: ", average_cycle," generations.")

if __name__ == '__main__':
    main()
    
