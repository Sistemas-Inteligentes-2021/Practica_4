# Libraries
import matplotlib.pyplot as plt
import pandas as pd

# Graph: Display Image
def graph_generations(generations, lenght):
    # Data
    cycles=[i for i in range(1,lenght+1)]
    df = pd.DataFrame({
        'x_axis': cycles,
        'y_axis': generations
    })

    # Plot
    plt.plot('x_axis', 'y_axis', data=df, linestyle='-', marker='o')

    plt.ylabel('# Generations')
    plt.xlabel('# Number Cycles')
    plt.title('- Genetic Algorithm -')
    if lenght < 20:
        plt.xticks(cycles)
    plt.show()