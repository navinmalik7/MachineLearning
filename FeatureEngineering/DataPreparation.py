import pandas as pd
# Load dataset
df = pd.read_csv('FeatureEngineering/housing_data.csv')
# Overview of the data
print(df.info())
# Summary statistics
print(df.describe())
# Check for missing values
print(df.isnull().sum())
