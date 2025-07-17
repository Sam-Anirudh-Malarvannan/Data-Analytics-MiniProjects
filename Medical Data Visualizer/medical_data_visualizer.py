import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Read Dataset
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column using BMI formula
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

# Normalize 'cholesterol' and 'gluc': 0 is good, 1 is bad
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


# Function to create categorical plot
def draw_cat_plot():
    # Melt DataFrame into Long format
    df_cat = pd.melt(df, id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and count values
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # Create the plot
    fig = sns.catplot(data=df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar').fig

    return fig


# Function to create heatmap
def draw_heat_map():
    # Clean invalid data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Correlation matrix
    corr = df_heat.corr()

    # Mask the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Plot HeatMap
    fig, ax = plt.subplots(figsize=(12, 8))

    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": 0.5}, ax=ax)

    return fig
