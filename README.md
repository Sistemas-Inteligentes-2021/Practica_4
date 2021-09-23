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
## 3. Experiments & Results

We execute the algorithm 20 times and we get the next data being the generations column the number of generations that were expanded until find the strongest chromosome
### First Experiment Pc=0.7 Pm=0.001
In this first experiment we use a Crossover probability of 0.7 (70%) and a Mutation probability of 0.001(1%). We can also  see the results in the section of images/first_experiment.png
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
In this experiment we use a Crossover probability of 0 (0%) and a Mutation probability of 0.001(1%). We can also  see the results in the section of images/without_crossover.png

Nº Run | Space States 
:---: | :---: 
1| 1636 |
2| 4059 |
3| 3228 |
4| 3108 |
5| 4420 |
6| 5067 |
7| 4333 |
8| 3885 |
9| 1544 |
10| 3110 |
11| 3452 |
12| 3572 |
13| 6837 |
14| 1927 |
15| 5399 |
16| 3548 |
17| 1743 |
18| 2359 |
19| 2960 |
20|  1645 |
AVERAGE| 3519.4   |
### WITHOUT MUTATION Pc=0.7 Pm=0
In this experiment we use a Crossover probability of 0.7 (70%) and a Mutation probability of 0 (0%). We can also  see the results in the section of images/without_mutation.png
Nº Run | Space States 
:---: | :---: 
1| 37  |
2| 34  |
3| 58  |
4| 33  |
5|   |
6|   |
7|   |
8|   |
9|   |
10|   |
11|   |
12|   |
13|   |
14|   |
15|   |
16|   |
17|   |
18|   |
19|   |
20|   |
AVERAGE|   |

We comment this results on the conclusion.

### Other Experiments
In this experiments we use a Crossover probability of 0.9 (90%), 0.3 (30%) and 0.7 (70%)  respectly and a Mutation probability of 0.001(1%), 0.001(1%), 0.1(1%) respectly
Nº Run | Pc=0.9 P=0.001  | Pc=0.3 P=0.001 | Pc=0.7 P=0.1
:---: | :---:  | :---:  | :---: 
1| 55  | 695  | 46  |
2| 30  | 2350  | 49  |
3| 56  | 92  | 37  |
4| 38  | 77  | 36  |
5| 44  | 60  | 39  |
6| 31  | 59  | 19  |
7| 36  | 42  | 31  |
8| 56  | 43  | 114  |
9| 54  | 70  | 75  |
10| 24  | 72  | 45  |
11| 49  | 56  | 40  |
12| 25  | 961  | 48  |
13| 50  | 1125  | 97  |
14| 35  | 80  | 30  |
15| 44  | 1216  | 53  |
16| 37  | 73  | 58  |
17| 41  | 48  | 41  |
18| 36  | 92  | 67  |
19| 48  | 52  | 54  |
20| 47  | 40  | 81  |
AVERAGE| 41.8  | 365.15  |  53 |

### Quantity of states
In this experiments we use a Crossover probability of 0.7 (70%) and mutation 0.001(1%). The thing that we are changing in this experiment is the number of chromosomes in the initial state.

Nº Run | 50  | 100 | 500  | 1000
:---: | :---:  | :---:  |  :---: | :---: 
1| 60  | 49  | 37  | 31  |
2| 200  | 33  | 26  | 31  |
3| 36  | 50  | 30  | 30  |
4| 5317  | 47  | 32  | 31  |
5| 5883  | 62  | 32  | 23  |
6| 25  | 21  | 48  | 32  |
7| 4551  | 53  | 18  | 34  |
8| 1753  | 33  | 23  | 39  |
9| 12  | 185  | 32  | 23  |
10| 710  | 56  | 28  | 14  |
11| 47  | 32  | 10  | 20  |
12| 57  | 58  | 31  | 24  |
13| 35  | 42  | 28  | 34  |
14| 2054  | 33  | 26  | 27  |
15| 9274  | 26  | 40  | 28  |
16| 446  | 48  | 21  | 35  |
17| 1455  | 32  | 41  | 37  |
18| 139  | 32  | 34  | 34  |
19| 6030  | 49  | 32  | 34  |
20| 5085  | 33  | 45  | 33  |
AVERAGE| 2158.45 | 48.7  | 30.7  | 29.7
## 4. Conclusions

Which is the best option?
- In the experiments we look and conclude that the best option is pick the "other_experiment_p1" with Pc(crossover probability) = 0.9 (90%) and pm (mutation probability) = 0.001 (1%) because with more probability of crossover we pick the strongest chromosome to make the new generation stronger than last generation.

Which is the best quantity for initial poblation?
- In the experiment we look and conclude that as we are increasing the quantity of initial poblation the number of  generation to find the strongest chromose decrease, in the experiment we use  Pc(crossover probability) = 0.9 (90%) and pm (mutation probability) = 0.001 (1%) and with 1000 chromosomes as initial poblation

WITHOUT MUTATION Pc=0.7 Pm=0
- If we don't have mutation, in many initial poblations its probably than with only crossover we will not be able to reach the solution.

### Comments

At the beggining we experiment a lot of problems principally in the situation of the selection of the cromosomes. so we decided to change the focus we work with list, at the beggining we experimented that work with list is more efficient and find a solution, unfortunetly we got some values of generations that were overcalculated with values extremely high, but we resolved it changing the partition of the crossover function, now the partition is not for the middle the partition is chosed randomly, and with that we get more real values, some values still being extremely high but is because the number of chromosomes in the initial state, we can conclude that with more poblation of chromosomes we get more real values and in less steps


## 5. Bibliography

➡️  Random function: [Python Docs: Random][random]

➡️  Weighted random choice: [Python Docs: Random][random]

➡️  Random in Range: [Python Docs: Randrange][random_range]



[random]: https://docs.python.org/3/library/random.html

[random_range]: https://docs.python.org/3/library/random.html#random.randrange



