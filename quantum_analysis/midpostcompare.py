import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')
pre = pd.read_csv("22-23 Quantum Course Pre-Survey_January 12, 2023_21.28.csv")
post = pd.read_csv("22-23 Quantum Course Post Semester 1 Survey_January 12, 2023_21.34.csv")
# post_interest = post.loc["Q25_1"]
# print(post_interest.value_counts())

# Describe something you think you would have benefitted from
f = open("post_wish.txt", 'w')
for each in post['Q63']:
    try:
        if len(each)>2:
            f.write(each)
            f.write('\n')
    except:
        pass
f.close()

# Do you have any recommendations for the course
f = open("post_recommendation.txt", 'w')
for each in post['Q64']:
    try:
        if len(each)>3:
            f.write(each)
            f.write('\n')
    except:
        pass
f.close()

# Instructor Feedback
f = open("post_instructor_feedback.txt", 'w')
for each in post['Q65']:
    try:
        if len(each)>3:
            f.write(each)
            f.write('\n')
    except:
        pass
f.close()
# Most liked part
f = open("post_like.txt", 'w')
for each in post['Q62']:
    try:
        if len(each)>3:
            f.write(each)
            f.write('\n')
    except:
        pass
f.close()

# One suggestion
f = open("post_suggestion.txt", 'w')
for each in post['Q81']:
    try:
        if len(each)>3:
            f.write(each)
            f.write('\n')
    except:
        pass
f.close()