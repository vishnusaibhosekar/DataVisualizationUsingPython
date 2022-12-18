import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

# Take in the data from the CSVs as NumPy arrays:
set_one = np.genfromtxt("seabornExamples\KDE Plots\kdeDataset1.csv", delimiter=",")
set_two = np.genfromtxt("seabornExamples\KDE Plots\kdeDataset2.csv", delimiter=",")
set_three = np.genfromtxt("seabornExamples\KDE Plots\kdeDataset3.csv", delimiter=",")
set_four = np.genfromtxt("seabornExamples\KDE Plots\kdeDataset4.csv", delimiter=",")

# Creating a Pandas DataFrame:
n=500
df = pd.DataFrame({
    "label": ["set_one"] * n + ["set_two"] * n + ["set_three"] * n + ["set_four"] * n,
    "value": np.concatenate([set_one, set_two, set_three, set_four])
})

# Setting styles:
sns.set_style("darkgrid")
sns.set_palette("pastel")

# Add your code below:
sns.kdeplot(set_one, shade=True)
sns.kdeplot(set_two, shade=True)
sns.kdeplot(set_three, shade=True)
sns.kdeplot(set_four, shade=True)

plt.show()