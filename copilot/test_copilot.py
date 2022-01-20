# Import pandas package
import pandas as pd

# Load the titanic dataset from github
titanic_url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/titanic.csv'
titanic_df = pd.read_csv(titanic_url)

# Compute the percentage of survivors
titanic_df['Survived'].mean()

# Compute the average of the age of the passengers
titanic_df['Age'].mean()

# Filter the titanic dataset by the column 



titanic_df_class_1 = titanic_df[titanic_df['Pclass'] == 1]

# Group the titanic dataset by the passenger class and compute the mean survival rate
titanic_df_class_1.groupby('Pclass').mean()



# Define a function to implement the newton raphson method iteratively
def newton_raphson(x, y, z):
    """
    Newton-Raphson method to solve the equation:
    z = x + y
    """
    # Initialize the guess
    guess = 0.5

    # Iterate until the guess is close enough to the solution
    while abs(guess**2 - (x + y)) > 0.001:
        # Update the guess
        guess = guess - ((guess**2 - (x + y)) / (2 * guess))

    # Return the solution
    return guess


# Define a a function advent of code 2021 day 11
def advent_of_code_day_11(input_list):
    """
    Advent of code day 11
    """
    # Initialize an empty list
    output_list = []

    # Iterate over the input list
    for i in range(len(input_list)):
        # Get the current input
        current_input = input_list[i]

        # Check if the current input is a number
        if isinstance(current_input, int) or isinstance(current_input, float):
            # Append the current input to the output list
            output_list.append(current_input)
        else:
            # Check if the current input is an operation
            if current_input in ['+', '-', '*', '/']:
                # Get the previous output
                previous_output = output_list[-1]

                # Get the previous input
                previous_input = input_list[i - 1]

                # Get the next input
                next_input = input_list[i + 1]

                # Compute the result
                result = eval(f'{previous_output}{current_input}{next_input}')

                # Append the result to the output list
                output_list.append(result)

    # Return the output list
    return output_list

import numpy as np

# Definir una función que devuelve la matriz identidad con NumPy
def identidad_numpy(n):
    """
    Devuelve la matriz identidad con NumPy
    """
    return np.identity(n)


# Define a Game of Life class
class GameOfLife:
    """
    Game of Life
    """

    # Define the constructor
    def __init__(self, n):
        """
        Constructor
        """
        # Initialize the grid
        self.grid = identidad_numpy(n)

    # Define a function to compute the next generation
    def next_generation(self):
        """
        Compute the next generation
        """
        # Compute the number of rows and columns in the grid
        n_rows, n_cols = self.grid.shape

        # Iterate over the rows
        for row in range(n_rows):
            # Iterate over the columns
            for col in range(n_cols):
                # Get the number of living neighbors
                n_living_neighbors = self.get_n_living_neighbors(row, col)

                # Check if the current cell is alive
                if self.grid[row, col]:
                    # Check if the current cell has less than 2 living neighbors
                    if n_living_neighbors < 2:
                        # Set the current cell to dead
                        self.grid[row, col] = 0

                    # Check if the current cell has more than 3 living neighbors
                    elif n_living_neighbors > 3:
                        # Set the current cell to dead
                        self.grid[row, col] = 0

                # Check if the current cell is dead
                else:
                    # Check if the current cell has exactly 3 living neighbors
                    if n_living_neighbors == 3:
                        # Set the current cell to alive
                        self.grid[row, col] = 1

    # Define a function to get the number of living neighbors
    def get_n_living_neighbors(self, row, col):
        """
        Get the number of living neighbors
        """
        # Initialize the number of living neighbors
        n_living_neighbors = 0

        # Get the number of rows and columns in the grid
        n_rows, n_cols = self.grid.shape

        # Iterate over the rows
        for i in range(row - 1, row