import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
def load_and_process(address):
    df1 = (
          pd.read_csv(address)
          .dropna(subset=['charges'])
        .rename(columns={'region':'area'})
        .replace({'southwest': 'SW', 'southeast': 'SE', 'northeast': 'NE', 'northwest': 'NW'})
          .round({"bmi":2,"charges":2})
          .sort_values('bmi',ascending=True)
          .reset_index(drop=True)
    )
    return df1

def percentage_young_smokers(df):
    index = df[smoker].index
    number_smokers = len(index)
    
    index = df[elderly].index
    number_elderly = len(index)
    
    index = df[young].index
    number_young = len(index)
    
    index = df[smoker & young].index
    number_young_smokers = len(index)
    
    index = df[smoker & elderly].index
    number_elderly_smokers = len(index)
    
    percentage = ((number_young_smokers)/(number_young))*100
    print("the percentage of young smokers: {}%".format(percentage))
    return


def percentage_elderly_smokers(df):
    index = df[smoker].index
    number_smokers = len(index)
    
    index = df[elderly].index
    number_elderly = len(index)
    
    index = df[young].index
    number_young = len(index)
    
    index = df[smoker & young].index
    number_young_smokers = len(index)
    
    index = df[smoker & elderly].index
    number_elderly_smokers = len(index)
    
    percentage = ((number_elderly_smokers)/(number_elderly))*100
    print("the percentage of elderly smokers: {}%".format(percentage))
    return

def charges_mean(df):
    average= df["charges"].mean()
    print("the average charges are: {}".format(average))
    return
def boxplot(df):
    plt.figure(figsize=(14,9))
    x= sns.boxplot(x='area',y='charges',data= df, hue='smoker')
    return x