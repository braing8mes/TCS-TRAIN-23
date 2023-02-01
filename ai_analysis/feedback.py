import pandas as pd

mid = pd.read_csv("Mid-point Survey Survey Student Analysis Report.csv")
print(mid.columns)
f = open("like.txt", 'w')
for each in mid['6543: What did you like the most about semester 1 of the course? (This may be related to the content, course structure, or anything else that comes to mind)']:
    try:
        if len(each)>1:
            f.write(each)
            f.write('\n')
    except:
        pass
f.close()
f = open("suggestions.txt", 'w')
for each in mid['6544: Describe something that you think would have benefited your experience in the first semester of the program.']:
    try:
        if len(each)>1:
            f.write(each)
            f.write('\n')
    except:
        pass
f.close()
f = open("general.txt", 'w')
for each in mid['6568: Is there anything else you would like to add regarding your view of the course, what you learned or any suggestions?']:
    try:
        if len(each)>1:
            f.write(each)
            f.write('\n')
    except:
        pass
f.close()