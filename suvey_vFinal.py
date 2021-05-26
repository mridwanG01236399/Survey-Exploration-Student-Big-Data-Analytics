# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 21:49:19 2020

@author: iwan, tim, lee, jt
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os  # needed for directory access

os.chdir('D:/George Mason University/Semester 2/Analytics Big Data to Information/Survey Exploration')
os.getcwd()

###############################################################################
#Import the data
data = pd.read_csv('Responses-20200407204228.csv', sep = ',', header=1)
data
data.head(10)
data.info()

data2 = data.drop(columns=['No.'])
data2.info()
###############################################################################
###############################################################################
#Import the questionare data
###############################################################################
data3 = pd.read_csv('Responses-20200407204228.csv', sep = ',')
data3.info()
data3['Unnamed: 0']

data4 = data3.drop(columns=['Unnamed: 0', 
                            'Unnamed: 1',
                            'Unnamed: 2',
                            'Unnamed: 3',
                            'Unnamed: 4',
                            'Unnamed: 5',
                            'Unnamed: 6',
                            'Unnamed: 7',
                            'Unnamed: 8',
                            'Unnamed: 9',
                            'Unnamed: 10',
                            'Unnamed: 11'])

data4.info()
###############################################################################
#cleansing AIT Section Column (Question 1)
###############################################################################
AIT_Section = []
i = 1
while (i < len(data4['Q1'])):
    
    if (not(math.isnan(pd.to_numeric(data4['Q1'][i], errors='coerce')))):
        AIT_Section.append('001')
        
    if (not(math.isnan(pd.to_numeric(data4['Q1.1'][i], errors='coerce')))):
        AIT_Section.append('004')
        
    if (not(math.isnan(pd.to_numeric(data4['Q1.2'][i], errors='coerce')))):
        AIT_Section.append('DL1')

    if (math.isnan(pd.to_numeric(data4['Q1'][i], errors='coerce')) and
        math.isnan(pd.to_numeric(data4['Q1.1'][i], errors='coerce')) and
        math.isnan(pd.to_numeric(data4['Q1.2'][i], errors='coerce'))):
        AIT_Section.append('Not Answered')  

    i = i + 1
###############################################################################
len(AIT_Section)
###############################################################################
#cleansing Gender Column (Question 2)
###############################################################################
Gender = []
i = 1
while (i < len(data4['Q2'])):
    
    if (not(math.isnan(pd.to_numeric(data4['Q2'][i], errors='coerce')))):
        Gender.append('Male')
    
    if (not(math.isnan(pd.to_numeric(data4['Q2.1'][i], errors='coerce')))):
        Gender.append('Female') 
        
    if (not(math.isnan(pd.to_numeric(data4['Q2.2'][i], errors='coerce')))):
        Gender.append('NonBinary')

    if (not(math.isnan(pd.to_numeric(data4['Q2.3'][i], errors='coerce')))):
        Gender.append('Prefer not to answer')

    if (math.isnan(pd.to_numeric(data4['Q2'][i], errors='coerce')) and
        math.isnan(pd.to_numeric(data4['Q2.1'][i], errors='coerce')) and
        math.isnan(pd.to_numeric(data4['Q2.2'][i], errors='coerce')) and
        math.isnan(pd.to_numeric(data4['Q2.2'][i], errors='coerce'))):
        Gender.append('Not Answered')  
    
    i = i + 1
###############################################################################
len(Gender)
###############################################################################
#cleansing Age Column (Question 3)
###############################################################################
Age = []
i = 1
while (i < len(data4['Q3'])):
    if (not(math.isnan(pd.to_numeric(data4['Q3'][i], errors='coerce')))):
        Age.append(data4['Q3'][i])  
    else:
        Age.append("Not Identified")  
    i = i + 1
###############################################################################
len(Age)
###############################################################################
#cleansing Height Column (Question 4)
###############################################################################
Height = []
i = 1
while (i < len(data4['Q4'])):
    if (not(math.isnan(pd.to_numeric(data4['Q4'][i], errors='coerce')))):
        Height.append(data4['Q4'][i])  
    else:
        Height.append("Not Identified")  
    i = i + 1
###############################################################################
len(Height)
###############################################################################
#cleansing Country of Citizenship Column (Question 5)
###############################################################################
#run this only once
#pip install country_converter --upgrade

import country_converter as coco
cc = coco.CountryConverter()

Citizenship1 = []
i = 1
while (i < len(data4['Q5'])):
    Citizenship1.append(data4['Q5'][i])    
    i = i + 1

Citizenship = cc.convert(names = Citizenship1, to = 'name_short')
###############################################################################
len(Citizenship)
###############################################################################
#cleansing the undergrad degree Column(Question 6)
###############################################################################
undergrade_degree = []
i = 1
while (i < len(data4['Q6'])):
    
    if (not(pd.isnull(data4['Q6'][i]))):
        if ("math" in data4['Q6'][i].casefold()):
            undergrade_degree.append("Science")
        elif ("stat" in data4['Q6'][i].casefold()):
            undergrade_degree.append("Science")
        elif ("computer" in data4['Q6'][i].casefold()):
            undergrade_degree.append("Engineering")
        elif ("engineer" in data4['Q6'][i].casefold()):
            undergrade_degree.append("Engineering")
        elif ("electronic" in data4['Q6'][i].casefold()):
            undergrade_degree.append("Engineering")
        elif ("cs" in data4['Q6'][i].casefold()):
            undergrade_degree.append("Engineering")
        elif ("tech" in data4['Q6'][i].casefold()):
            undergrade_degree.append("Engineering")
        elif ("cyber" in data4['Q6'][i].casefold()):
            undergrade_degree.append("Engineering")
        elif ("stat" in data4['Q6'][i].casefold()):
            undergrade_degree.append("Science")
        elif ("math" in data4['Q6'][i].casefold()):
            undergrade_degree.append("Science")
        elif ("mathematics" in data4['Q6'][i].casefold()):
            undergrade_degree.append("Science")
        elif ("physics" in data4['Q6'][i].casefold()):
            undergrade_degree.append("Science")
        elif ("biology" in data4['Q6'][i].casefold()):
            undergrade_degree.append("Science")
        elif ("business" in data4['Q6'][i].lower()):
            undergrade_degree.append("Business")
        else:
            undergrade_degree.append("Others")
    else:
        undergrade_degree.append("Others")
        
    i = i + 1
###############################################################################
len(undergrade_degree)
###############################################################################
#cleansing Expected Graduate Column(Question 7)
###############################################################################
Expected_Graduation = []
i = 1
while (i < len(data4['Q7'])):
    if (not(pd.isnull(data4['Q7'][i]))):
        if ((pd.to_numeric(data4['Q7'][i][5:][:2])) < 6):
            Expected_Graduation.append("spring " + data4['Q7'][i][:4])
        else:
            Expected_Graduation.append("fall " + data4['Q7'][i][:4])
    else:
        Expected_Graduation.append("Not Sure")
        
    i = i + 1
###############################################################################
len(Expected_Graduation)
###############################################################################
#cleansing Laptop Used Column(Question 8)
###############################################################################
laptop_used = []
i = 1
while (i < len(data4['Q8'])):
    
    if (((pd.to_numeric(data4['Q8'][i], errors='coerce')) == 1) and
        ((pd.to_numeric(data4['Q8.1'][i], errors='coerce')) == 1) and
        ((pd.to_numeric(data4['Q8.2'][i], errors='coerce')) == 1)):
        laptop_used.append('Microsoft/Windows, Apple/MacBook, and Other')
    elif (((pd.to_numeric(data4['Q8'][i], errors='coerce')) == 1) and 
          ((pd.to_numeric(data4['Q8.1'][i], errors='coerce')) == 1)):
        laptop_used.append('Microsoft/Windows and Apple/MacBook')
    elif (((pd.to_numeric(data4['Q8.1'][i], errors='coerce')) == 1) and
          ((pd.to_numeric(data4['Q8.2'][i], errors='coerce')) == 1)):
        laptop_used.append('Apple/MacBook and Other')
    elif (((pd.to_numeric(data4['Q8'][i], errors='coerce')) == 1) and
          ((pd.to_numeric(data4['Q8.2'][i], errors='coerce')) == 1)):
        laptop_used.append('Microsoft/Windows and Other')
    else:
        if (not(math.isnan(pd.to_numeric(data4['Q8'][i], errors='coerce')))):
            laptop_used.append('Microsoft/Windows')        
        if (not(math.isnan(pd.to_numeric(data4['Q8.1'][i], errors='coerce')))):
            laptop_used.append('Apple/MacBook')
        if (not(math.isnan(pd.to_numeric(data4['Q8.2'][i], errors='coerce')))):
            laptop_used.append('Other')
        if (math.isnan(pd.to_numeric(data4['Q8'][i], errors='coerce')) and
            math.isnan(pd.to_numeric(data4['Q8.1'][i], errors='coerce')) and
            math.isnan(pd.to_numeric(data4['Q8.2'][i], errors='coerce'))):
            laptop_used.append('Not Answered')    
    
    i = i + 1
###############################################################################
len(laptop_used)
###############################################################################
#cleansing Commuting Time Column(Question 9)
###############################################################################
commuting_time = []
i = 1
while (i < len(data4['Q9'])):
    if (not(math.isnan(pd.to_numeric(data4['Q9'][i], errors='coerce')))):
        commuting_time.append(data4['Q9'][i])  
    else:
        commuting_time.append("Not Identified")  
    i = i + 1
###############################################################################
len(commuting_time)
###############################################################################
#cleansing employed status Column(Question 10)
###############################################################################
employed_status = []
i = 1
while (i < len(data4['Q10'])):
    
    if (not(math.isnan(pd.to_numeric(data4['Q10'][i], errors='coerce')))):
        employed_status.append('Full Time')
    
    if (not(math.isnan(pd.to_numeric(data4['Q10.1'][i], errors='coerce')))):
        employed_status.append('Not Full Time') 
        
    if (not(math.isnan(pd.to_numeric(data4['Q10.2'][i], errors='coerce')))):
        employed_status.append('Not Working')
    
    if (math.isnan(pd.to_numeric(data4['Q10'][i], errors='coerce')) and
        math.isnan(pd.to_numeric(data4['Q10.1'][i], errors='coerce')) and
        math.isnan(pd.to_numeric(data4['Q10.2'][i], errors='coerce'))):
        employed_status.append('Do not know the employee status')    
        
    i = i + 1
###############################################################################
len(employed_status)
###############################################################################
#cleansing level of programming skill in Python Column(Question 11)
###############################################################################
level_programming = []
i = 1
while (i < len(data4['Q11'])):
    
    if (not(math.isnan(pd.to_numeric(data4['Q11'][i], errors='coerce')))):
        level_programming.append('Little/none')
    
    if (not(math.isnan(pd.to_numeric(data4['Q11.1'][i], errors='coerce')))):
        level_programming.append('Some familiarity') 
        
    if (not(math.isnan(pd.to_numeric(data4['Q11.2'][i], errors='coerce')))):
        level_programming.append('Average user')
        
    if (not(math.isnan(pd.to_numeric(data4['Q11.3'][i], errors='coerce')))):
        level_programming.append('Frequent use for projects')
        
    if (not(math.isnan(pd.to_numeric(data4['Q11.4'][i], errors='coerce')))):
        level_programming.append('Fluent/expert')        

    if (math.isnan(pd.to_numeric(data4['Q11'][i], errors='coerce')) and
        math.isnan(pd.to_numeric(data4['Q11.1'][i], errors='coerce')) and
        math.isnan(pd.to_numeric(data4['Q11.2'][i], errors='coerce')) and
        math.isnan(pd.to_numeric(data4['Q11.3'][i], errors='coerce')) and
        math.isnan(pd.to_numeric(data4['Q11.4'][i], errors='coerce'))):
        level_programming.append('Do not know the level')   
    
    i = i + 1
###############################################################################
len(level_programming)
###############################################################################
#Merging the questionare Data
###############################################################################
questionare_data = pd.DataFrame({'AIT_Section' : AIT_Section,
                                 'Gender' : Gender,
                                 'Age' : Age,
                                 'Height' : Height,
                                 'Citizenship' : Citizenship,
                                 'undergrade_degree' : undergrade_degree,
                                 'Expected_Graduation' : Expected_Graduation,
                                 'laptop_used' : laptop_used,
                                 'commuting_time' : commuting_time,
                                 'employed_status' : employed_status,
                                 'level_programming' : level_programming})
questionare_data.info()
questionare_data
###############################################################################
#summary of level_programming by IWAN
###############################################################################
questionare_data.groupby(['AIT_Section', 'level_programming']).size().reset_index(name='counts')
###############################################################################
#visualization of level_programming by IWAN
###############################################################################
AITSection_levelProgramming = questionare_data.groupby(['AIT_Section', 'level_programming']).size().reset_index(name='counts')

import seaborn as sns
sns.set(style="whitegrid")

# Draw a nested barplot to show the total of expert for class and sex
g = sns.catplot(x="AIT_Section", 
                y="counts", 
                hue="level_programming", 
                data=AITSection_levelProgramming,
                height=6, 
                kind="bar", 
                palette="muted")
g.despine(left=True)
g.set_ylabels("Number of Each Level Programming")
g.set_xlabels("AIT Section")
ax = plt.gca()
ax.set_title("Students Level Programming In Each Section", weight='bold').set_fontsize('18')
###############################################################################
#summary of employed_status by IWAN
###############################################################################
questionare_data.groupby(['AIT_Section', 'employed_status']).size().reset_index(name='counts')
###############################################################################
#visualization of employed_status by IWAN
###############################################################################
AITSection_employedStatus = questionare_data.groupby(['AIT_Section', 'employed_status']).size().reset_index(name='counts')

sns.set(style="whitegrid")

g = sns.catplot(x="AIT_Section", 
                y="counts", 
                hue="employed_status", 
                data=AITSection_employedStatus,
                height=6, 
                kind="bar", 
                palette="muted")
g.despine(left=True)
g.set_ylabels("Total of Each Employment Status")
g.set_xlabels("AIT Section")
ax = plt.gca()
ax.set_title("Employment Student Status In Each Section", weight='bold').set_fontsize('18')
###############################################################################
#summary of commuting_time by IWAN
###############################################################################
questionare_data.groupby("AIT_Section")['commuting_time'].describe().reset_index()
###############################################################################
#visualization of commuting_time by IWAN
###############################################################################
fig = plt.figure()
fig.suptitle('Commuting Time per Section', fontsize=14, fontweight='bold')

ax = fig.add_subplot(111)
sns.boxplot(x = questionare_data["AIT_Section"], 
            y=pd.to_numeric(questionare_data["commuting_time"],errors='coerce'), 
            palette="Blues")
ax.set_title('Students Commuting Time per Section')
ax.set_xlabel('AIT Section')
ax.set_ylabel('Commuting Time')
plt.show()
###############################################################################
#visualization of Q1 by Tim
###############################################################################
#summary of Gender
###############################################################################
questionare_data.groupby(['AIT_Section', 'Gender']).size().reset_index(name='counts')
###############################################################################
AITSection_gender=questionare_data.groupby(['AIT_Section', 'Gender']).size().reset_index(name='counts')
N = 3
section_male = (AITSection_gender.at[1,'counts'],
              AITSection_gender.at[3,'counts'],
              AITSection_gender.at[5,'counts'])
section_female = (AITSection_gender.at[0,'counts'],
              AITSection_gender.at[2,'counts'],
              AITSection_gender.at[4,'counts'])

ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, section_male, width)
p2 = plt.bar(ind, section_female, width,
             bottom=section_male)

plt.ylabel('The amount of students')
plt.title('AIT-580 Section')
plt.xticks(ind, ('001', '004', 'DL1'))
plt.yticks(np.arange(0, 31, 5))
plt.xlabel('AIT Section')
plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()
###############################################################################
#summary of Citizenship by Tim
###############################################################################
questionare_data.groupby(['AIT_Section', 'Citizenship']).size().reset_index(name='counts')
###############################################################################
AITSection_Citizenship1=questionare_data.groupby(['AIT_Section', 'Citizenship']).size().reset_index(name='counts')

plt.figure()

plt.subplot(2,2,1)
labels1 =  'India' , 'Pakistan','Saudi Arabia','Taiwan','United States' 
sizes1= [AITSection_Citizenship1.at[0,'counts'],AITSection_Citizenship1.at[1,'counts'],
        AITSection_Citizenship1.at[2,'counts'],AITSection_Citizenship1.at[3,'counts'],
        AITSection_Citizenship1.at[4,'counts']]
explode = (0.01, 0.01, 0.01)
plt.pie(sizes1, labels=labels1, startangle=90, autopct='%.1f%%',textprops = {"fontsize" : 10})
plt.title('Section 001',{"fontsize" : 14})

plt.subplot(2,2,2)
labels2 =  'India','Belgium' , 'Eritrea','Iran','Ukraine ','United States' 
sizes2= [AITSection_Citizenship1.at[8,'counts'],AITSection_Citizenship1.at[6,'counts'],
        AITSection_Citizenship1.at[7,'counts'],AITSection_Citizenship1.at[9,'counts'],
        AITSection_Citizenship1.at[10,'counts'],AITSection_Citizenship1.at[11,'counts']]
plt.pie(sizes2, labels=labels2, startangle=90, autopct='%.1f%%',textprops = {"fontsize" : 10})
plt.title('Section 004',{"fontsize" : 14})

plt.subplot(2,2,3)
labels3 =  'India ' , 'Indonesia',' South Korea','Taiwan','Thailand ','United States' 
sizes3= [AITSection_Citizenship1.at[12,'counts'],AITSection_Citizenship1.at[13,'counts'],
        AITSection_Citizenship1.at[14,'counts'],AITSection_Citizenship1.at[15,'counts'],
        AITSection_Citizenship1.at[16,'counts'],AITSection_Citizenship1.at[17,'counts']]
plt.pie(sizes3, labels=labels3, startangle=90, autopct='%.1f%%',textprops = {"fontsize" : 10})
plt.title('Section DL1',{"fontsize" : 14})

plt.show()

###############################################################################
#summary of Citizenship by Tim
###############################################################################
questionare_data.groupby(['AIT_Section', 'Citizenship']).size().reset_index(name='counts')
###############################################################################
#visualization of Citizenship by Tim
###############################################################################
AITSection_Citizenship2 = questionare_data.groupby(['AIT_Section', 'Citizenship']).size().reset_index(name='counts')

import seaborn as sns
sns.set(style="whitegrid")

# Draw a nested barplot to show the total of expert for class and sex
g = sns.catplot(x="AIT_Section", 
                y="counts", 
                hue="Citizenship", 
                data=AITSection_Citizenship2,
                height=6, 
                kind="bar", 
                palette="muted")
g.despine(left=True)
g.set_ylabels("Number of Citizenship")
g.set_xlabels("AIT Section")
ax = plt.gca()
ax.set_title("Countries of Citizenship In Each Section", weight='bold').set_fontsize('18')
###############################################################################
#summary of Type of Laptop Used by Tim
###############################################################################
questionare_data.groupby(['AIT_Section', 'laptop_used']).size().reset_index(name='counts')
###############################################################################
#visualization of Laptop_Used by Tim
###############################################################################
AITSection_laptop_used = questionare_data.groupby(['AIT_Section', 'laptop_used']).size().reset_index(name='counts')

import seaborn as sns
sns.set(style="whitegrid")

# Draw a nested barplot to show the total of expert for class and sex
g = sns.catplot(x="AIT_Section", 
                y="counts", 
                hue="laptop_used", 
                data=AITSection_laptop_used,
                height=6, 
                kind="bar", 
                palette="muted")
g.despine(left=True)
g.set_ylabels("Number of Each type of laptop")
g.set_xlabels("AIT Section")
ax = plt.gca()
ax.set_title("Type of Laptop Used In Each Section", weight='bold').set_fontsize('18')
###############################################################################
#summary of Gender by Tim
###############################################################################
questionare_data.groupby(['laptop_used', 'Gender']).size().reset_index(name='counts')
###############################################################################
laptop_used_gender=questionare_data.groupby(['laptop_used', 'Gender']).size().reset_index(name='counts')
N = 3
section_male = (laptop_used_gender.at[1,'counts'],
                laptop_used_gender.at[3,'counts'],
                laptop_used_gender.at[4,'counts'])
section_female = (laptop_used_gender.at[0,'counts'],
                  laptop_used_gender.at[2,'counts'],
                  laptop_used_gender.at[5,'counts'])

ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, section_male, width)
p2 = plt.bar(ind, section_female, width,
             bottom=section_male)

plt.ylabel('The amount of students')
plt.title('Type of Laptop Used')
plt.xticks(ind, ('Apple/MacBook', 'Microsoft/Windows', 'Both'))
plt.yticks(np.arange(0, 31, 5))
plt.xlabel('Type of Laptop')
plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()
###############################################################################
#visualization of Section by JT
###############################################################################
#summary of Section
###############################################################################
questionare_data.groupby(['AIT_Section']).size().reset_index(name='counts')
###############################################################################
AITSection = questionare_data.groupby(['AIT_Section']).size().reset_index(name='counts')

sns.set(style="whitegrid")

g = sns.catplot(x="AIT_Section", 
                y="counts",  
                data=AITSection,
                height=6, 
                kind="bar", 
                palette="muted")
g.despine(left=True)
g.set_ylabels("Number Of Student")
g.set_xlabels("Section")
ax = plt.gca()
ax.set_title("Number Of Student", weight='bold').set_fontsize('18')
###############################################################################
#visualization of Q3 by JT
###############################################################################
#summary of Age
###############################################################################
questionare_data.groupby(['Age']).size().reset_index(name='counts')
questionare_data.groupby(['AIT_Section', 'Age']).size().reset_index(name='counts')
###############################################################################

AIT_age = questionare_data.groupby(['Age']).size().reset_index(name='counts')

sns.set(style="whitegrid")

g = sns.catplot(x="Age", 
                y="counts",  
                data=AIT_age,
                height=6, 
                kind="bar", 
                palette="muted")
g.despine(left=True)
g.set_ylabels("Number Of Student")
g.set_xlabels("Age")
ax = plt.gca()
ax.set_title("Number Of Student For Ecah Age", weight='bold').set_fontsize('18')
###############################################################################
AITSection_age = questionare_data.groupby(['AIT_Section', 'Age']).size().reset_index(name='counts')

sns.set(style="whitegrid")

g = sns.catplot(x="AIT_Section", 
                y="counts", 
                hue="Age", 
                data=AITSection_age,
                height=6, 
                kind="bar", 
                palette="muted")
g.despine(left=True)
g.set_ylabels("Number Of Student")
g.set_xlabels("AIT Section")
ax = plt.gca()
ax.set_title("Number Of Student Age In Each Section", weight='bold').set_fontsize('18')
###############################################################################
fig = plt.figure()
fig.suptitle('Age for each Section', fontsize=14, fontweight='bold')

ax = fig.add_subplot(111)
sns.boxplot(x = questionare_data["AIT_Section"], 
            y=pd.to_numeric(questionare_data["Age"],errors='coerce'), 
            palette="Blues")
ax.set_xlabel('AIT Section')
ax.set_ylabel('Age')
plt.show()
###############################################################################
#visualization of Q4 by JT
###############################################################################
#summary of Height
###############################################################################
questionare_data.groupby(['Height']).size().reset_index(name='counts')
questionare_data.groupby(['AIT_Section', 'Height']).size().reset_index(name='counts')
###############################################################################
AIT_Height = questionare_data.groupby(['Height']).size().reset_index(name='counts')

sns.set(style="whitegrid")

g = sns.catplot(x="Height", 
                y="counts",  
                data=AIT_Height,
                height=6, 
                kind="bar", 
                palette="muted")
g.despine(left=True)
g.set_ylabels("Number Of Student")
g.set_xlabels("Height")
ax = plt.gca()
ax.set_title("Number Of Student Height", weight='bold').set_fontsize('18')
###############################################################################
AITSection_Height = questionare_data.groupby(['AIT_Section', 'Height']).size().reset_index(name='counts')

sns.set(style="whitegrid")

g = sns.catplot(x="AIT_Section", 
                y="counts", 
                hue="Height", 
                data=AITSection_Height,
                height=6, 
                kind="bar", 
                palette="muted")
g.despine(left=True)
g.set_ylabels("Number Of Student")
g.set_xlabels("AIT Section")
ax = plt.gca()
ax.set_title("Number Of Student Height In Each Section", weight='bold').set_fontsize('18')
###############################################################################
fig = plt.figure()
fig.suptitle('Student Height For Each Section', fontsize=14, fontweight='bold')

ax = fig.add_subplot(111)
sns.boxplot(x = questionare_data["AIT_Section"], 
            y=pd.to_numeric(questionare_data["Height"],errors='coerce'), 
            palette="Blues")
ax.set_xlabel('AIT Section')
ax.set_ylabel('Height')
plt.show()
###############################################################################
#summary and the visualization of the Expected Graduate Time by Lee
###############################################################################
AITSection_Expected_Graduation = questionare_data.groupby(['AIT_Section', 'Expected_Graduation']).size().reset_index(name='counts')

import seaborn as sns
sns.set(style="whitegrid")

# Draw a nested barplot to show the total of expert for class and sex
g = sns.catplot(x="AIT_Section", 
                y="counts", 
                hue="Expected_Graduation", 
                data=AITSection_Expected_Graduation,
                height=6, 
                kind="bar", 
                palette="muted")
g.despine(left=True)
g.set_ylabels("Number of Expected Graduation Time")
g.set_xlabels("AIT Section")
ax = plt.gca()
ax.set_title("Expected Graduation Time In Each Section", weight='bold').set_fontsize('18')
###############################################################################
#summary and the visualization of the undergrad degree by Lee
###############################################################################
AITSection_undergrade_degree = questionare_data.groupby(['AIT_Section', 'undergrade_degree']).size().reset_index(name='counts')

Business = [AITSection_undergrade_degree.at[0, 'counts'],
            AITSection_undergrade_degree.at[3, 'counts'],
            0]
Engineering = [AITSection_undergrade_degree.at[1, 'counts'],
               AITSection_undergrade_degree.at[4, 'counts'],
               AITSection_undergrade_degree.at[7, 'counts']]
Science = [0,
           AITSection_undergrade_degree.at[6, 'counts'],
           AITSection_undergrade_degree.at[9, 'counts']]
Others = [AITSection_undergrade_degree.at[2, 'counts'],
          AITSection_undergrade_degree.at[5, 'counts'],
          AITSection_undergrade_degree.at[8, 'counts']]

bars1 = Engineering
bars2 = Others
bars3 = Business
barsTS = Science

# Heights of bars1 + bars2
bars = np.add(bars1, bars2).tolist()

# The position of the bars on the x-axis
r = [1, 2, 3]

names = ['001', '004', 'DL1']
barWidth = 0.35       # the width of the bars: can also be len(x) sequence

# Create category_1
p1 = plt.bar(r, bars1, color='blue', edgecolor='white', width=barWidth)
# Create category_2
p2 = plt.bar(r, bars2, bottom=bars1, color='yellow', edgecolor='white', width=barWidth)
# Create category_3
p3 = plt.bar(r, bars3, bottom=bars, color='orange', edgecolor='white', width=barWidth)   
# Create barsTS
p4 = plt.bar(r, barsTS, bottom=bars, color='Grey', edgecolor='white', width=barWidth)

# Custom X axis
fig.add_subplot(111)
plt.xticks(r, names, fontweight='bold')
plt.xlabel("Section")
plt.ylabel("Number of Each Undergrad Degree")
plt.title("Undergrade Degree in Each Section", fontweight='bold')
plt.legend((p1[0], p2[0], p3[0], p4[0]), ('Engineering', 'Others', 'Business', 'Science'), bbox_to_anchor=(1.05, 1.0),loc = 'upper left')
plt.tight_layout()
plt.show()