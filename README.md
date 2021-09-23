# Practica_4
## Members

- Daniel Camacho
- Adrian Mendoza
- Juslan Vargas

## 1. Describing the Problem
We have a poblation with 100 chromosomes and we must find the strongest chromosome in the new generations that we will create. The strongest chromosome is the one that will have only the number 1 in each gene. We will continue generating new populations until we find the strongest chromosome.

## 2. Describing the Solution
To solve this problem we use the Genetic Algorithm, we are going to implement the 3 actions that comes with this algorithm:
- Selection
- Crossover
- Mutation
In the other hand to calculate the probability of selection we are going to use the fitness function to get the strongest chromosome (with more 1)
## 3. Experiments & Results

We execute the algorithm 20 times and we get the next data being the generations column the number of generations that were expanded until find the strongest chromosome
### First Experiment Pc=0.7 Pm=0.001
In this first experiment we use a Crossover probability of 0.7 (70%) and a Mutation probability of 0.001(1%). We can also  see the results in the section of images/population_100/PC_07_PM_0.001/Console
Nº Run | Generations
:---: | :---: 
1| 55  
2| 30 
3| 37  
4| 60  
5| 30  
6| 65  
7| 59 
8| 48  
9| 59 
10| 34 
11| 33  
12| 31  
13| 27  
14| 25  
15| 28  
16| 44  
17| 54 
18| 37 
19| 425 
20| 42 
AVERAGE| 61.15  
### WITHOUT CROSSOVER Pc=0 Pm=0.001
In this experiment we use a Crossover probability of 0 (0%) and a Mutation probability of 0.001(1%). We can also  see the results in the section of images/population_100/with_out_crossover/Console

Nº Run | Space States 
:---: | :---: 
1 | 1636
2 | 7690
3 | 3399
4 | 4144
5 | 1095
6 | 4721
7 | 1749
8 | 2578
9 | 1721
10 | 1751
11 | 2055
12 | 1777
13 | 2344
14 | 5076
15 | 3272
16 | 3936
17 | 2282
18 | 5326
19 | 7031
20 | 2017
AVERAGE| 3280.0   |
### WITHOUT MUTATION Pc=0.7 Pm=0
In this experiment we use a Crossover probability of 0.7 (70%) and a Mutation probability of 0 (0%). We can also  see the results in the section of images/population_100/without_mutation/Console
Nº Run | Space States 
:---: | :---: 
1 | 48
2 | 45
3 | 58
4 | 35
5 | 40
6 | 33
7 | 25
8 | 44
9 | 45
10 | 38

AVERAGE|  41.1  |

We comment this results on the conclusion.

### Other Experiments
In this experiments we use a Crossover probability of 0.9 (90%), 0.3 (30%) and 0.7 (70%)  respectly and a Mutation probability of 0.001(1%), 0.001(1%), 0.1(1%) respectly
Nº Run | Pc=0.9 P=0.001  | Pc=0.3 P=0.001 | Pc=0.7 P=0.1
:---: | :---:  | :---:  | :---: 
1 | 30 | 101 | 53
2 | 53 | 2099 | 28
3 | 59 | 71 | 151
4 | 37 | 59 | 62
5 | 41 | 28 | 72
6 | 44 | 78 | 54
7 | 36 | 69 | 60
8 | 32 | 84 | 11
9 | 34 | 2405 | 64
10 | 36 | 44 | 28
11 | 33 | 42 | 56
12 | 51 | 71 | 58
13 | 57 | 66 | 37
14 | 34 | 486 | 38
15 | 55 | 51 | 31
16 | 55 | 44 | 44
17 | 22 | 37 | 30
18 | 38 | 1583 | 37
19 | 46 | 576 | 37
20 | 27 | 721 | 98
AVERAGE| 41.0   | 433.75  |  52.45 |

### Quantity of states
In this experiments we use a Crossover probability of 0.9 (90%) (the best) and mutation 0.001(1%). The thing that we are changing in this experiment is the number of chromosomes in the initial state.

Nº Run | 50  | 100 | 500  | 1000
:---: | :---:  | :---:  |  :---: | :---: 
1 | 2517 | 56 | 31 | 21
2 | 7460 | 50 | 36 | 34
3 | 1051 | 42 | 33 | 24
4 | 51 | 37 | 20 | 31
5 | 2399 | 17 | 22 | 28
6 | 4615 | 42 | 29 | 25
7 | 660 | 215 | 38 | 31
8 | 38 | 63 | 30 | 36
9 | 417 | 33 | 19 | 29
10 | 159 | 41 | 35 | 24
11 | 928 | 27 | 24 | 20
12 | 2717 | 37 | 27 | 21
13 | 2705 | 36 | 31 | 29
14 | 1177 | 36 | 39 | 32
15 | 4575 | 31 | 32 | 25
16 | 1361 | 11 | 34 | 29
17 | 79 | 37 | 30 | 24
18 | 967 | 40 | 28 | 30
19 | 119 | 25 | 17 | 28
20 | 36 | 31 | 24 | 27
AVERAGE| 1701.55 | 45.35  | 28.95  | 27.4

### Quantity of states

## 4. Conclusions

Which is the best option?
- In the experiments we look and conclude that the best option is pick the "other_experiment_p1" with Pc(crossover probability) = 0.9 (90%) and pm (mutation probability) = 0.001 (1%) because with more probability of crossover we pick the strongest chromosome to make the new generation stronger than last generation.

Which is the best quantity for initial poblation?
- In the experiment we look and conclude that as we are increasing the quantity of initial poblation the number of  generation to find the strongest chromose decrease, in the experiment we use  Pc(crossover probability) = 0.9 (90%) and pm (mutation probability) = 0.001 (1%) and with 1000 chromosomes as initial poblation

WITHOUT MUTATION Pc=0.7 Pm=0
- If we don't have mutation, in many initial poblations its probably than with only crossover we will not be able to reach the solution. For doing that we get noticed that the algorithm work at some point, so we decided to split in 10 solutions(like table and images/population_100/without_mutation/Console), the error is that we were in a infinite cycle (you can see it  in images/population_100/without_mutation_error)

### Comments

At the beggining we experiment a lot of problems principally in the situation of the selection of the cromosomes. so we decided to change the focus we work with list, at the beggining we experimented that work with list is more efficient and find a solution, unfortunetly we got some values of generations that were overcalculated with values extremely high, but we resolved it changing the partition of the crossover function, now the partition is not for the middle the partition is chosed randomly, and with that we get more real values, some values still being extremely high but is because the number of chromosomes in the initial state, we can conclude that with more poblation of chromosomes we get more real values and in less steps


## 5. Bibliography

➡️  Random function: [Python Docs: Random][random]

➡️  Weighted random choice: [Python Docs: Random][random]

➡️  Random in Range: [Python Docs: Randrange][random_range]



[random]: https://docs.python.org/3/library/random.html

[random_range]: https://docs.python.org/3/library/random.html#random.randrange



