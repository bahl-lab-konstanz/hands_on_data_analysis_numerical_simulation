import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


##  Simulate a simple random walk.


def simulate_random_walk_2D(num_individuals, num_steps, p_left=0.5, p_up=0.5):
    # Create an empty DataFrame to store the positions
    df = pd.DataFrame(columns=['x_position', 'y_position'])

    # Start the random walk simulation for each individual
    for i in range(num_individuals):
        # Initialize the position of the current individual to (0, 0)
        current_position = np.array([0.0, 0.0])

        # Simulate the random walk for the current individual
        for step in range(num_steps):
            # Generate random numbers between 0 and 1 for x and y directions
            prob_x = np.random.rand()
            prob_y = np.random.rand()

            # Update the position based on the random numbers
            # Here probability of moving left or right is 0.5. For directed walks, change this
            if prob_x < p_left:
                current_position[0] -= np.random.normal(1, 0.5)  # agent moves left
            else:
                current_position[0] += np.random.normal(1, 0.5)  # agent moves right

            # Here probability of moving up or down is 0.5. For directed walks, change this
            if prob_y < p_up:
                current_position[1] -= np.random.normal(1, 0.5)  # agent moves up
            else:
                current_position[1] += np.random.normal(1, 0.5)  # agent moves down

            # Append the current position to the DataFrame
            df = df.append(pd.DataFrame([[i, step, current_position[0], current_position[1]]],
                                        columns=['fish_ID', 'swim_number', 'x_position', 'y_position']))

    # Set the multi-index with 'Individual' and 'Step' columns
    df.set_index(['fish_ID', 'swim_number'], inplace=True)

    return df


def see_trajectory(df):
    for fish in df.index.unique('fish_ID'):
        df_fish = df.xs(fish, level='fish_ID')
        x = list(df_fish.x_position)
        y = list(df_fish.y_position)

        end_x = x[-1]
        end_y = y[-1]

        plt.scatter(end_x, end_y, marker='o')
        plt.plot(x, y, alpha=0.7)

    plt.show()

    return plt


def count_movements(df):
    for fish in df.index.unique('fish_ID'):
        df_fish = df.xs(fish, level='fish_ID')

        df_fish['difference_x_position'] = df_fish['x_position'].diff()
        df_fish['difference_y_position'] = df_fish['y_position'].diff()

        positive_x = (df_fish['difference_x_position'] > 0).sum()
        negative_x = (df_fish['difference_x_position'] < 0).sum()

        positive_y = (df_fish['difference_y_position'] > 0).sum()
        negative_y = (df_fish['difference_y_position'] < 0).sum()

        print("fish_ID:", fish)
        print("Left moving counts:", positive_x)
        print("Right moving counts:", negative_x)
        print("Up moving counts:", positive_y)
        print("Down moving counts:", negative_y)

    return None


# Example use

N = 6  # Number of individuals
num_steps = 200  # Number of steps in the random walk

# Simulate the random walk in two dimensions
result = simulate_random_walk_2D(N, num_steps)

# Print the resulting DataFrame
print(result)
see_trajectory(result)
count_movements(result)
# Position and trajectory visualisation

# Exercise section
# Make it a directed walk with individuals likely to move more right.
# Make it a directed walk with individuals likely to move more left and up.
