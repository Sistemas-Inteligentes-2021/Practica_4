# Libraries
from random import randint
from random import randrange
from random import choices
from random import random
from graph_cycle_generation import graph_generations

# Global Vars
genes_number=20
quantity_population=100

generation_number=100
crossover_probability=0.7
mutation_probability=0.001

# Generate [1, 1, 1, 1, ... ]
def generate_objetive_chromosome():
    chrom = [1] * genes_number
    return chrom

# Generate [random (0,1), ...]
def generate_random_chromosome():
    chromosome = []
    for i in range(genes_number):        
        chromosome.append(randint(0, 1))
    return chromosome

# Crossover: Get 2 new Chromosome
def crossover(crx,cry):
    middle = int(genes_number/2)
    if random()<=crossover_probability:
        crx1=crx[:middle]+cry[middle:]
        cry1=cry[:middle]+crx[middle:]
        return crx1,cry1
    return crx,cry

# Crossover: Get 2 new Chromosome
def crossover_random(crx,cry):
    middle = randint(1,genes_number-1)
    if random()<=crossover_probability:
        crx1=crx[:middle]+cry[middle:]
        cry1=cry[:middle]+crx[middle:]
        return crx1,cry1
    return crx,cry

# Mutation_Both: Change a Random bit in Chromosome 
def mutation_both(chromosome_x, chromosome_y):
    if random()<=mutation_probability:
        random_position =  randrange(genes_number)
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

def run_first_generation(quantity_population):
    initial_poblation=[]
    ff=[]
    for i in range(quantity_population):                        #Generate the N  number of chromosomes
        chromosome=generate_random_chromosome()
        initial_poblation.append(chromosome)                    #Generate the chromosome
        ff_chromosome=fitness_function(chromosome)
        ff.append(ff_chromosome)                                #Finde his Fitness function
    return initial_poblation,ff


# Execute: Selection, Crossover, Mutation
def execute_functions(initial_poblation, ff, generations):

    
    for i in range(generation_number):                                            # Check if the goal Fitnes Function is not generate in initial Generation  
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

        initial_poblation= new_generation
        ff=new_ff
        generations.append(ff)


def genetic_algorithm(quantity_population, generations):
    initial_poblation, ff, = run_first_generation(quantity_population)              # First Generation 
    execute_functions(initial_poblation, ff, generations)   # Next Generations

def fitness_poblation(generation,ff_poblation):
    
    for i in generation:
        sumatory=0
        sumatory=sum(i)
        ff_poblation.append(sumatory/genes_number)
    

# Main Function
def main():
    generations= []
    ff_poblation=[]
    genetic_algorithm(quantity_population, generations)
    fitness_poblation(generations, ff_poblation)
    print("|------- RESULTS -------|")
    print("* Genes:", genes_number)
    print("* Population:", quantity_population)
    print("* Probability Crossover:", crossover_probability)
    print("* Probability Mutation:", mutation_probability)
    print("|-----------------------|")

    graph_generations(ff_poblation,generation_number)


if __name__ == '__main__':
    main()
    
