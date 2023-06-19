# DATA ANALYSIS WITH PANDAS

# For this section we will need an external library, pandas. So, we will use an "import" statement, that provides
# our script with the requested package from our conda environment. For convenience, we will use an abbreviation using
# the "as" keyword to give the imported library an alias
import pandas as pd

# we also import a bunch of other libraries and utilities that we will use along this section
from pathlib import Path
import matplotlib.pyplot as plt
from utils.constants import color_list
from utils.tutorial_navigation import step

### Introduction
# When working with tabular data, such as data stored in spreadsheets or databases, pandas is the perfect tool.
# It allows to easily explore, clean, and process data. In pandas, a data table is called a DataFrame.
# The name "pandas" stands for "Python Data Analysis" (or Panel Data according to some sources).

### Tutorial Navigation
# To navigate this section we need to update the value of the variable step in file ./utils/tutorial_navigation

# First of all we have to provide the path of the location where we saved the data. Here we are using the relative
# path (relative to the present script). You can also provide it in form of absolute path. We start by loading one chunk
# of our dataset
path = "../data/fish_100.csv"

# We then procede loading the data and showing the overall information
if step == 1 or step == 2:
    # load data in a dataframe structure
    df = pd.read_csv(path)

if step == 1:
    # print information
    print(df.info())

# Let's peek at the data
if step == 2:
    # show the first 10 lines of the dataframe
    print(df.head())

# We are not 100% happy with the result. In fact, we have an additional row, named "Unnamed: 0". Furthermore, we notice
# that that column contains just increasing numbers. In our output we can see that we already have an unnamed set of
# increasing numbers identifying the rows (the leftmost column of values).
# This happens because any dataframe needs an index, i.e. a non-ambiguous way to refer to rows.

# To correctly extract the information on the index, we need to provide pandas with more information about how we want
# the data to be loaded:
if step >= 3:
    # load csv specifying where to extract columns and rows names
    df = pd.read_csv(path, index_col=0, header=0)
if step == 3:
    # show the first 10 lines of the dataframe now
    print(df.head())

# pandas provides an easy way to access basic statistical characteristics of our data. In particular dataframes have
# built-in methods "min()", "max()", "mean()", "sum()", "corr()", and "describe()" which gives a summary
if step == 4:
    # print basic statistics of the columns "average_speed" and "start_time"
    print("AVERAGE SPEED")
    print(df["average_speed"].describe())

    print("START TIME")
    print(df["start_time"].describe())

# The dataset we just used come from a single fish. For our analysis we need to put together data from different
# individuals
if step >= 5:
    dir_path = Path("../data")
    data_list = []
    for fish_dataset_path in dir_path.glob("*.csv"):
        # load data in a temporary structure
        data_list.append(pd.read_csv(fish_dataset_path, index_col=0, header=0))
    # merge all the dataframes in data_list
    df = pd.concat(data_list, axis=0)
if step == 5:
    # print information about the dataframe
    print(df.info())

# Someone could have noticed that the information in the index is redundant, in fact we can already identify specific
# swims in a meaningful way by combining three columns: fish_ID, trial and swim_number. For this reason we now want to
# get rid of the default incremental index in favor of a more meaningful hierarchical index, or MultiIndex.
# The great benefit of MultiIndex is the possibility to store and manipulate data with an arbitrary number of dimensions
# in lower dimensional data structures like DataFrames (2d).
if step >= 6:
    # refactor dataframe using multi-level indexing with "fish_ID", "trial", "swim_number"
    df = df.set_index(["fish_ID", "trial", "swim_number"])
if step == 6:
    # print the head of the dataframe
    print(df.head())

# Now that we have a proper dataframe, we can extract some information. For example, we can now check the accuracy of
# each fish using the amount of 1s in correct_bout

if step >= 7:
    # we are going to simplify the analysis as much as possible, so we will only consider left or right swims, filtering
    # out all the straight ones, identified in the dataframe by the value -1 in column "correct_bout"
    df = df[~(df["correct_bout"] == -1)]

if step == 8:
    # we iterate over fishes
    for fish_id in df.index.unique("fish_ID"):
        # we select only the subset of rows corresponding to the present fish, using all the trials
        df_fish = df.xs(fish_id, level="fish_ID")
        # and now we compute the accuracy as correct_bouts/total_bouts
        accuracy = df_fish["correct_bout"].sum() / len(df_fish["correct_bout"])
        print(f"INFO | fish {fish_id} has accuracy = {accuracy}")

if step == 9:
    # we can also perform the same operation using the groupby method
    df_accuracy = df.groupby("fish_ID")["correct_bout"].mean()

    # from the output dataframe we can also obtain information on the best and worst performing fish
    print(f"INFO | fish {df_accuracy.idxmax()} has accuracy {df_accuracy.max()}. It's the best")
    print(f"INFO | fish {df_accuracy.idxmin()} has accuracy {df_accuracy.min()}. It's the worst")

# Finally we are interested in looking at how the best and worst fish move in the arena, so we are going to plot the
# swimming trajectory for these two
if step == 10:
    # define the index of the best and worst fish
    fish_id_best = 109
    fish_id_worst = 101

    # define grid for plotting
    fig, axs = plt.subplots(1, 2)

    # plot the trajectory for the best fish
    axs[0].set_title("best fish trajectory")
    axs[0].set_ylabel("start_y_position")
    axs[0].set_xlim([-1, 1])
    axs[0].set_ylim([-1, 1])
    for trial in df.index.unique("trial"):
        df.xs((fish_id_best, trial), level=["fish_ID", "trial"]).plot(x="start_x_position", y="start_y_position",
                                                                      ax=axs[0], kind="line", legend=False,
                                                                      color=color_list[trial])

    # plot the trajectory for the worst fish
    axs[1].set_title("worst fish trajectory")
    axs[1].set_xlim([-1, 1])
    axs[1].set_ylim([-1, 1])
    for trial in df.index.unique("trial"):
        df.xs((fish_id_worst, trial), level=["fish_ID", "trial"]).plot(x="start_x_position", y="start_y_position",
                                                                       ax=axs[1], kind="line", legend=False,
                                                                       color=color_list[trial])

    # show plots
    plt.show()
