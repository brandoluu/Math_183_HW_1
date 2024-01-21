import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mt
import seaborn as sns
import csv


#Function where given a file name return a list of dictionaries containing the data
def getInfo(filename):
    with open(filename, mode='r') as f:
        csv_reader = csv.DictReader(f)
        dataList = []
        for row in csv_reader:
            dataList.append(row)
    return dataList


#Function that returns the BMI of a given weight and height
def getBMI(weight, height):
    return weight / (height*height)
    
dictionary = getInfo('/Users/brandonluu/MATH 183/HW 1/obesity_study.csv') 
studentData = getInfo('/Users/brandonluu/MATH 183/HW 1/student_data_183.csv')

"""
# HW 1 Q2 Part D
col = []    # for status
bmi = []

for dict in dictionary:
    #if dict["status"] not in col:
    col.append(dict["status"])
    bmi.append(getBMI(float(dict["weight"]), float(dict["height"])))

#use this to make the graph
df = pd.DataFrame({"BMI": bmi, "Status": col})


sns.boxplot(x="Status", y="BMI", data=df)
plt.show()
"""

"""
# HW 1 Q2 Part E
physicalTransport = 0
notPhysical = 0
for dict in dictionary:
    if dict["transportation"] == "Walking" or dict["transportation"] == "Bike":
        physicalTransport += 1
    else:
        notPhysical += 1

data = [physicalTransport, notPhysical]
keys = ["Physical Transport", "Other"]
palette_color = sns.color_palette('bright') 
plt.pie(data, labels=keys, colors=palette_color, autopct='%.0f%%') 
plt.show()
"""

"""
# HW 1 Q2 Part F
col = []    
bmi = []

for dict in dictionary:
    col.append(dict["transportation"])
    bmi.append(getBMI(float(dict["weight"]), float(dict["height"])))

#use this to make the graph
df = pd.DataFrame({"BMI": bmi, "Transportation": col})

sns.boxplot(x="Transportation", y="BMI", data=df)
plt.show()
"""

"""
# HW 1 Q3 Part C
gender = []    # x axis
physicalHours = []       # y axis

for student in studentData:
    gender.append(student["sex"])
    physicalHours.append(float(student["time_physical"]))

#use this to make the graph
df = pd.DataFrame({"Physical Hours": physicalHours, "Gender": gender})

sns.boxplot(x="Gender", y="Physical Hours", data=df)
plt.show()
"""

"""
# HW 1 Q3 Part E
comfort = ["Super Comfy", "Pretty good", "Meh", "Bad", "Awful"]
prettyGood = 0
bad = 0
meh = 0
superComfy = 0
awful = 0
for student in studentData:
    studentComfort = student["seat_comfort"]
    if studentComfort == "Meh":
        meh += 1
    elif studentComfort == "Pretty good":
        prettyGood += 1
    elif studentComfort == "Super comfy":
        superComfy += 1
    elif studentComfort == "Awful":
        awful += 1
    elif studentComfort == "Bad":
        bad += 1
comfortData = [superComfy, prettyGood, meh, bad, awful]
df = pd.DataFrame({"Number of Students": comfortData, "Comfort Rating": comfort})

sns.barplot(x="Comfort Rating", y="Number of Students", data=df)
plt.show()
"""

"""
# HW 1 Q3 Part F
hoursOnline = []
hoursReading = []
for student in studentData:
    hoursReading.append(float(student["time_reading"]))
    hoursOnline.append(float(student["time_online"]))

df = pd.DataFrame({"Hours Online": hoursOnline, "Hours Reading": hoursReading})
sns.scatterplot(data=df, x="Hours Online", y="Hours Reading")
plt.show()
"""

"""
# HW 1 Q3 Part E
hoursOnline = []
for student in studentData:
    hoursOnline.append(float(student["time_online"]))

df = pd.DataFrame({"Hours Online": hoursOnline})
sns.histplot(data=df, stat="frequency",x="Hours Online", binwidth=3)
plt.show()
"""


"""
# HW 1 Q3 Part I
studentCredit = [] 
totalCredit = 0
for student in studentData:
    studentCredit.append(float(student["wi24_credits"]))
    totalCredit += float(student["wi24_credits"])

mean = int(totalCredit)/len(studentCredit)
median = studentCredit[int(len(studentCredit)/2)]
mode = max(set(studentCredit), key=studentCredit.count)

print("Mean: " + str(mean))
print("Median: " + str(median))
print("Mode: " + str(mode))
"""

# HW 1 Q3 Part J
numEngineers = 0
for student in studentData:
    if student["major"] == "Engineering":
        numEngineers += 1

print(numEngineers)
print(numEngineers/len(studentData) * 100)






     


