from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("seabornExamples\FIFA World Cup Goals Visualization\WorldCupMatches.csv")
df_goals = pd.read_csv("seabornExamples\FIFA World Cup Goals Visualization\goals.csv")

df["Total Goals"] = df["Home Team Goals"] + df["Away Team Goals"]

sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=0.8)
f, ax = plt.subplots(figsize=(12, 7))

ax = sns.barplot(x=df["Year"], y=df["Total Goals"])

ax.set_title("Average Number Of Goals Scored In World Cup Matches By Year")

plt.show()

f, ax2 = plt.subplots(figsize=(12, 7))
ax2 = sns.boxplot(x="year", y="goals", data=df_goals, palette="Spectral")
ax2.set_title("Goals Visualization")

plt.show()