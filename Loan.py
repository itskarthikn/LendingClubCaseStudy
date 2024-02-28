#import the libraries
import pandas as pd
import numpy as np
#import the plotting libraries
import matplotlib.pyplot as plt
%matplotlib inline
#import the necessary libraries
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns

df=pd.read_csv("C:\\Users\\karth\\Python\\Course2\\loan_details\\loan.csv")
df.head()
df.shape
df.isnull().sum(axis=0)
# drop columns with all NaN's
df = df.dropna(axis=1, how='all')
df.shape
df.isnull().sum()