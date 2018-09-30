
# coding: utf-8

# In[2]:


import csv


# In[3]:


f=open("guns.csv",'r')


# In[4]:


csvreader=csv.reader(f)


# In[5]:


data= list(csvreader)


# In[6]:


print(data[:5])


# In[7]:


headers=data[0]


# In[8]:


data=data[1:]


# In[9]:


print(headers)


# In[10]:


print(data[:5])


# In[11]:


years=[]
for each in data:
    years.append(each[1])


# In[12]:


year_counts={}


# In[13]:


for year in years:
    if year in year_counts:
        year_counts[year]+=1
    else:
        year_counts[year]=1
        


# In[14]:


print(year_counts)


# In[15]:


dates=[]


# In[16]:


import datetime
for row in data:
    dates.append(datetime.datetime(year=int(row[1]),month=int(row[2]),day=1))


# In[17]:


print(dates[:5])


# In[18]:


date_counts={}


# In[19]:


for date in dates:
    if date in date_counts:
        date_counts[date]+=1
    else:
        date_counts[date]=1


# In[20]:


print(date_counts)


# In[21]:


sex_counts={}


# In[22]:


for row in data:
    if row[5] in sex_counts:
        sex_counts[row[5]]+=1
    else:
        sex_counts[row[5]]=1
        


# In[23]:


races=[]
for row in data:
    races.append(row[7])


# In[24]:


print(races)


# In[25]:


race_counts={}


# In[26]:


for row in data:
    if row[7] in race_counts:
        race_counts[row[7]]+=1
    else:
        race_counts[row[7]]=1


# In[27]:


print(sex_counts)


# In[28]:


print(race_counts)


# # Till now we learned about the *dates* ,*sex* and *race* of the victims
# # Now we will move to know about their intents and hispanic origin code

# In[29]:


import csv
f2=open("census.csv",'r')


# In[30]:


census=list(csv.reader(f2))


# In[31]:


print(census)


# In[32]:


mapping={
    "Asian/Pacific Islander":0,
    "Black":0,
    "Native American/Native Alaskan":0,
    "Hispanic":0,
    "White":0
}


# In[33]:


census=census[1]


# In[34]:


print(census)


# In[35]:


asian=int(census[14])+int(census[15])


# In[37]:


mapping["Asian/Pacific Islander"]=asian
mapping["Black"]=int(census[12])
mapping["Native American/Native Alaskan"]=int(census[13])
mapping["Hispanic"]=int(census[11])
mapping["White"]=int(census[10])


# In[38]:


race_per_hundredk={}
for each in race_counts:
    race_per_hundredk[each]=race_counts[each]/mapping[each]*100000


# In[39]:


print(race_per_hundredk)


# In[41]:


intents=[]
races=[]
for each in data:
    intents.append(each[3])
    races.append(each[7])


# In[42]:


homicide_race_counts={}
for i,race in enumerate(races):
    if intents[i]=="Homicide":
        if race in homicide_race_counts:
            homicide_race_counts[race]+=1
        else :
            homicide_race_counts[race]=1
            


# In[43]:


print(homicide_race_counts)


# In[44]:


for each in homicide_race_counts:
    homicide_race_counts[each]=homicide_race_counts[each]/mapping[each]*100000


# In[45]:


print(homicide_race_counts)

