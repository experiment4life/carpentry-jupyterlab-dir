import sys
import glob
import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

# make sure additional arguements or flag
# have been provided by the user
if len(sys.argv) == 1:
        # why the program will not continue
        print("Not enough arguments have been provide")
        # how this can be corrected
        print("Usage: python gdp_plots.py < filenames >")
        print("Options:")
        print("-a : plot all gdp data sets in current directory")

# check for -a flag in arguments
if '-a' in sys.argv:
        filenames = glob.glob('data/*gdp*[ae].csv')
        if filenames == []:
                # file list is empty (no files found)
                print("No files found in this folder.")
                print("Make sure the data folder and files are located")
                print("in the current directory")
else:
        filenames = sys.argv[1:]

for filename in filenames:

        # load data and transpose so that country names are
        # the columns and their gdp data becomes the rows
        data = pandas.read_csv(filename, index_col = 'country').T

        # create a plot of the transposed data
        ax = data.plot()

        # set some plot attributes
        ax.set_xlabel('Year')
        ax.set_ylabel('GDP Per Capita')
        # set the x locations and labels
        ax.set_xticks(range(len(data.index)))
        ax.set_xticklabels(data.index, rotation = 45)

        # save the plot
        split_name1 = filename.split('.')[0] #data/gapminder_gdp_XXX
        split_name2 = split_name1.split('/')[1]
        save_name = 'figs/' + split_name2 + '.png'
        plt.savefig(save_name)

cd ..
python swc-gapminder/gdp_plots.py -a # error message is outputted!
cd swc-gapminder
git status
git add gdp_plots.py
git commit -m "handling case if no files are present in current directory"

### Let's start a new branch to begin refactoring or reorganizing our code
git checkout -b refactor
git branch # check branch
cat gdp_plots.py

# how should we reorganize our script into a set of fxns?

    - one function that parses arguments

    - one function for creating one plot

    - one function that creates multiple plots

    - one function that will call all possible functions--the "main" function


import sys
import glob
import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt


def parse_arguments(argv):
    """
    Parse the argument list passed from the command line
    (after the program filename is removed) and return a list
    of filenames.

    Input:
    ------
        argument list (normally sys.argv[1:])

    Returns:
    --------
        filenames: list of strings, list of files to plot
    """


def create_plot(filename):
    """
    Creates a plot for the specified
    data file.

    Input:
    ------
        filename: string, path to file to plot

    Returns:
    --------
        none
    """


def create_plots(filenames):
    """
    Takes in a list of filenames to plot
    and creates a plot for each file.

    Input:
    ------
        filenames: list of strings, list of files to plot

    Returns:
    --------
        none
    """


def main():
    """
    main function - does all the work
    """



# call main
main()
