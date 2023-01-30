"""
Pre and post course survey analysis.

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer

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

full_demo = full[['Final Score (from Gradebook)', 'Enrollment Status', 'Race/Ethnicity', 'Gender', 'LGBTQ', 'Income Level', 'Location', 'Python']]
# full_demo = full[['Final Score (from Gradebook)', 'Python']]
full_demo = full_demo.dropna(thresh = 2)
full_demo['Python'] = full_demo['Python'].astype(str).str[:1]
full_demo['Python'] = full_demo['Python'].astype(int)

imp = SimpleImputer(missing_values=np.nan, strategy='mean') 
df_mode['MaxSpeed'] = mode_imputer.fit_transform(df_mode['MaxSpeed'].values.reshape(-1,1))
scores = np.array(full_demo['Final Score (from Gradebook)'])
python = np.array(full_demo['Python']).reshape(-1,1)
model = LinearRegression().fit(python, scores)
r2 = model.score(python, scores)
print(r2)
print(model.coef_)
print(model.intercept_)

plt.figure(figsize=(12,8))
sb.heatmap(corr, cmap="Greens", annot=True)
plt.style.use('fivethirtyeight')
