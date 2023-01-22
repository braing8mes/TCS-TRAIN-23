"""
Pre and post course survey analysis.

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')
pre = pd.read_csv("22-23 Quantum Course Pre-Survey_January 12, 2023_21.28.csv")
post = pd.read_csv("22-23 Quantum Course Post Semester 1 Survey_January 12, 2023_21.34.csv")
pre_demo = pre.loc[:,"Q110_1": "Q110_9"]
# for column in pre_demo:
    # print(pre_demo[column].value_counts())

pre_race={
    "Native American or Alaska Native": 29,
    "Asian": 1633,
    "White": 847,
    "Hawaiian or Pacific Islander": 21,
    "Black or African American": 478,
    "Hispanic or Latine/o/a/x": 423,
    "Middle Eastern or North African": 343,
    "Prefer not to say": 252,
    "Other": 202,
}
post_demo = post.loc[:, "Q124_1": "Q124_9"]
# for column in post_demo:
    # print(post_demo[column].sum())
post_race={
    "Native American or Alaska Native": 4,
    "Asian": 69,
    "White": 40,
    "Hawaiian or Pacific Islander": 0,
    "Black or African American": 25,
    "Hispanic or Latine/o/a/x": 15,
    "Middle Eastern or North African": 43,
    "Prefer not to say": 14,
    "Other": 7,
}
demo_rate={}
for key in pre_race.keys():
    demo_rate[key] = round(100*post_race[key]/pre_race[key], 1)
print(demo_rate)

pre_gen = pre.loc[:,"Q109"]
post_gen = post.loc[:, "Q123"]
# print(pre_gen.value_counts())
# print(post_gen.value_counts())
pre_gender={
    "Male": 2434,
    "Female": 1263,
    "Prefer not to say": 99,
    "Non-binary": 49,
    "Other": 18,
}
post_gender={
    "Male": 111,
    "Female": 72,
    "Prefer not to say": 11,
    "Non-binary": 3,
    "Other": 1,
}
gender_rate={}
for key in pre_gender.keys():
    gender_rate[key] = round(100*post_gender[key]/pre_gender[key], 1)
print(gender_rate)

focus = post.loc[(post.index<2)| (post["Q124_1"]=='1') | (post["Q124_7"]=='1')]
focus.to_csv("vulnerable_race.csv")