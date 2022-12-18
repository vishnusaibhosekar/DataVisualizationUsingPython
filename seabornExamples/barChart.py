import warnings
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
warnings.filterwarnings("ignore")

set_one = np.genfromtxt("seabornExamples\dataset1.csv", delimiter=",")
set_two = np.genfromtxt("seabornExamples\dataset1.csv", delimiter=",")
set_three = np.genfromtxt("seabornExamples\dataset1.csv", delimiter=",")
set_four = np.genfromtxt("seabornExamples\dataset1.csv", delimiter=",")

n=500
df = pd.DataFrame({
    "label": ["set_one"] * n + ["set_two"] * n + ["set_three"] * n + ["set_four"] * n,
    "value": np.concatenate([set_one, set_two, set_three, set_four])
})

sns.set_style("darkgrid")
sns.set_palette("pastel")

sns.barplot(data=df, x="label", y="value")
plt.show()