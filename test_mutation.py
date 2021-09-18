# Mutation
# https://docs.python.org/3/library/random.html#random.randrange
from random import randrange

gens_number = 20
chrom_0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
chrom_1 = [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1]
chrom_2 = [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1]

# Mutation: Change a random bit
def mutation(chromosome_crossover):
    random_position =  randrange(20)
    # print(random_position)
    # print( chromosome_crossover[random_position] )
    chromosome_crossover[random_position] = 1 if chromosome_crossover[random_position] == 0 else 0 ;
    return chromosome_crossover


# result = mutation (chrom_0)
# print(chrom_0)
# print(result)
print(chrom_1)
result = mutation (chrom_1)
print(result)
