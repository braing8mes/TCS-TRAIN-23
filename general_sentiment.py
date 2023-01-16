"""
General sentiments on the course comparing pre-course survey to post-course survey. 
Mid course survey feelings.

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')

# Mid course survey

mid = pd.read_csv("Mid-Course Survey Survey Student Analysis Report (1).csv")
useful = []
for each in mid.columns:
    if each.startswith("1.0") == False:
        useful.append(each)
mid_clean = mid[useful]

# interest questions
num_conv = {
"Significantly more interested": 1,
"More interested": 2,
"Stayed the same": 3,
"Less interested": 4,
"Significantly less interested": 5,
}
interest = mid_clean[['6572: After one semester of this course, how has your interest in STEM (science, technology, engineering, and math) changed?',
       '6573: After one semester of this course, how has your interest in quantum computing changed?']]
stem = mid_clean['6572: After one semester of this course, how has your interest in STEM (science, technology, engineering, and math) changed?'].value_counts(normalize=True)
quantum = mid_clean['6573: After one semester of this course, how has your interest in quantum computing changed?'].value_counts(normalize=True)

colors = plt.get_cmap('Blues')(np.linspace(0.9, 0.2, len(stem)))

explode = (0, 0, 0, 0, 0)
f1 = plt.figure(1)
patches, texts = plt.pie(stem, colors= colors, radius= 40, wedgeprops={"linewidth": 0.3, "edgecolor": "white"}, explode=explode)

plt.title("STEM Interest Change")

plt.axis("equal")
labels = [f'{l}, {s:.1f}%' for l, s in zip(list(num_conv.keys()), stem*100)]
plt.legend(patches, labels, loc='best',
    fontsize=8)
plt.tight_layout()

f2=plt.figure(2)
patches2, texts2 = plt.pie(quantum, colors= colors, radius= 40, wedgeprops={"linewidth": 0.3, "edgecolor": "white"}, explode=explode)

plt.title("Quantum Interest Change")

plt.axis("equal")
labels2 = [f'{l}, {s:.1f}%' for l, s in zip(list(num_conv.keys()), quantum*100)]
plt.legend(patches2, labels2, loc='best',
    fontsize=8)
plt.tight_layout()

diff = mid_clean["6575: How would you rate the level of difficulty of the first semester? "].value_counts(normalize=True)
labels = list(diff.index)
f3 = plt.figure(3)
patches3, texts3 = plt.pie(diff, colors= colors, radius= 40, wedgeprops={"linewidth": 0.3, "edgecolor": "white"})

plt.title("Level of Difficulty")

plt.axis("equal")
labels3 = [f'{l}, {s:.1f}%' for l, s in zip(labels, diff*100)]
plt.legend(patches3, labels3, loc='best',
    fontsize=8)
plt.tight_layout()


overall = mid_clean['6576: On a scale of 1-5, how would you rate the first semester of the course overall?'].value_counts(normalize=True)
labels = list(overall.index)
f4 = plt.figure(4)
patches4, texts4 = plt.pie(overall, colors= colors, radius= 40, wedgeprops={"linewidth": 0.3, "edgecolor": "white"}, explode=explode)

plt.title("Overall Rating")

plt.axis("equal")
labels4 = [f'{l}, {s:.1f}%' for l, s in zip(labels, overall*100)]
plt.legend(patches4, labels4, loc='best',
    fontsize=8)
plt.tight_layout()

confidence = mid_clean['6574: After semester 1, my confidence in my STEM skills has:'].value_counts(normalize=True)
f5 = plt.figure(5)
labels = list(confidence.index)
patches5, texts5 = plt.pie(confidence, colors= colors, radius= 40, wedgeprops={"linewidth": 0.3, "edgecolor": "white"}, explode=explode)

plt.title("STEM confidence")

plt.axis("equal")
labels5 = [f'{l}, {s:.1f}%' for l, s in zip(labels, confidence*100)]
plt.legend(patches5, labels5, loc='best',
    fontsize=8)
plt.tight_layout()
plt.show()