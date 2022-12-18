import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

set_one = np.genfromtxt("seabornExamples\Violin Plots\dataset1.csv", delimiter=",")
set_two = np.genfromtxt("seabornExamples\Violin Plots\dataset2.csv", delimiter=",")
set_three = np.genfromtxt("seabornExamples\Violin Plots\dataset3.csv", delimiter=",")
set_four = np.genfromtxt("seabornExamples\Violin Plots\dataset4.csv", delimiter=",")

n=500
df = pd.DataFrame({
    "label": ["set_one"] * n + ["set_two"] * n + ["set_three"] * n + ["set_four"] * n,
    "value": np.concatenate([set_one, set_two, set_three, set_four])
})

sns.set_style("darkgrid")
sns.set_palette("pastel")

sns.violinplot(data=df, x="label", y="value")
plt.show()
