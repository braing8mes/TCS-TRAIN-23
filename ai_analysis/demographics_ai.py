"""
Pre and post course survey analysis.

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

full = pd.read_csv("train_full.csv")
withdrew = pd.read_csv("train_withdrew.csv")
b = False
if b:
    full_race = full['Race/Ethnicity'].value_counts().to_dict()
    withdrew_race = withdrew['Race/Ethnicity'].value_counts().to_dict()

    drop_race = {}
    for key in full_race.keys():
        try:
            drop_race[key] = round(100*withdrew_race[key]/full_race[key], 1)
        except:
            drop_race[key] = 0.0
    print(drop_race)

if b:
    full_gender = full['Gender'].value_counts().to_dict()
    withdrew_gender = withdrew['Gender'].value_counts().to_dict()

    drop_gender = {}
    for key in full_gender.keys():
        try:
            drop_gender[key] = round(100*withdrew_gender[key]/full_gender[key], 1)
        except:
            drop_gender[key] = 0.0
    print(drop_gender)

if b:
    full_lgbtq = full['LGBTQ'].value_counts().to_dict()
    withdrew_lgbtq = withdrew['LGBTQ'].value_counts().to_dict()

    drop_lgbtq = {}
    for key in full_lgbtq.keys():
        try:
            drop_lgbtq[key] = round(100*withdrew_lgbtq[key]/full_lgbtq[key], 1)
        except:
            drop_lgbtq[key] = 0.0
    print(drop_lgbtq)

if b:
    full_income = full['Income Level'].value_counts().to_dict()
    withdrew_income = withdrew['Income Level'].value_counts().to_dict()

    drop_income = {}
    for key in full_income.keys():
        try:
            drop_income[key] = round(100*withdrew_income[key]/full_income[key], 1)
        except:
            drop_income[key] = 0.0
    print(drop_income)

full_drop = full[['Final Score (from Gradebook)', 'Race/Ethnicity', 'Gender', 'LGBTQ', 'Income Level', 'Python']]
full_drop = full_drop.dropna()
demo_score = full_drop['Final Score (from Gradebook)']
demo_data = full_drop[['Race/Ethnicity', 'Gender', 'LGBTQ', 'Income Level', 'Python']]
race_data = full_drop[['Race/Ethnicity', 'Income Level', 'Python']]
gender_data = full_drop[['Gender', 'Python']]
income_data = full_drop[['Income Level', 'Python']]
X = pd.get_dummies(data=income_data, drop_first=False)
Y = demo_score
model = LinearRegression().fit(X, Y)

X_train_Sm= sm.add_constant(X)
ls=sm.OLS(Y ,X_train_Sm).fit()
print(ls.summary())



