import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats.mstats import winsorize
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import StandardScaler
from simple_colors import *

# This code uses a modified format of the "vectors.csv" file
df_factors = pd.read_csv("./code/vectors.csv", sep=',', header=0)

print(df_factors.info())

stats = pd.DataFrame({ "Missing Values": df_factors.isnull().sum(),
                       "Mean": df_factors.mean(),
                       "Median": df_factors.median(),
                       "Mode": df_factors.mode().iloc[0] })

print(stats)

print(df_factors.describe().T)


plot_hist_month = sns.histplot(data=df_factors["FireDiscoveryMonth"], bins=12, color="dodgerblue")
plot_hist_month.set_title("Fire Occurrences by Month")
plot_hist_month.set_xlabel("Month")
plot_hist_month.set_ylabel("Occurrences")

plot_hist_precipitation = sns.histplot(data=df_factors["Precipitation"], bins=df_factors["Precipitation"].count() // 200, color="dodgerblue")
plot_hist_precipitation.set_title("Fire Occurrences by Daily Mean Precipitation")
plot_hist_precipitation.set_xlabel("Precipitation (inches)")
plot_hist_precipitation.set_ylabel("Occurrences")

plot_hist_temperature = sns.histplot(data=df_factors["Temperature"], bins=df_factors["Temperature"].count() // 200, color="dodgerblue")
plot_hist_temperature.set_title("Fire Occurrences by Daily Mean Temperature")
plot_hist_temperature.set_xlabel("Temperature (Fahrenheit)")
plot_hist_temperature.set_ylabel("Occurrences")


plot_boxplot_month = sns.boxplot(x=df_factors["FireDiscoveryMonth"], color="dodgerblue")
plot_boxplot_month.set_title("Fire Occurrences by Month")
plot_boxplot_month.set_xlabel("Month")

plot_boxplot_precipitation = sns.boxplot(x=df_factors["Precipitation"], color="dodgerblue")
plot_boxplot_precipitation.set_title("Fire Occurrences by Daily Mean Precipitation")
plot_boxplot_precipitation.set_xlabel("Precipitation (inches)")

plot_boxplot_temperature = sns.boxplot(x=df_factors["Temperature"], color="dodgerblue")
plot_boxplot_temperature.set_title("Fire Occurrences by Daily Mean Temperature")
plot_boxplot_temperature.set_xlabel("Temperature (Fahrenheit)")
