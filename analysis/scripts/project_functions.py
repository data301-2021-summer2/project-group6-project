import pandas as pd
import numpy as np
import seaborn as sns
import pandas_profiling as pf
import matplotlib.pyplot as plt

path='../data/raw/adult.data'
def load_and_process(path):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
        pd.read_csv('../data/raw/adult.data')
        .drop([' 13', ' 2174', ' 0', ' 40', 'Unnamed: 0', ' Never-married', ' Not-in-family'], axis=1)
        .rename({' State-gov': 'Work Class', ' 77516': 'Final Weight', ' <=50K':'Income', '39': 'Age', ' White':'Race', ' Adm-clerical': 'Occupation', ' Bachelors': 'Education Level', ' Never-married': 'Marital-Status', ' Male': 'Sex', ' Not-in-family': 'Relationship', ' United-States': 'Native-Country'}, axis=1)
    )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
        df1
        .replace([' 1st-4th', ' 5th-6th', ' 7th-8th'], 'Elementary')
        .replace([' 9th', ' 10th', ' 11th', ' 12th'], 'High School')
    )

    # Make sure to return the latest dataframe

    return df2 

load_and_process(path)

