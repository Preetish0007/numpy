#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[10]:


c=np.array([[[{"min temp":12,"max temp":32},{"min temp":13,"max temp":25},{"min temp":7,"max temp":26},{"min temp":8,"max temp":26}]]])


# In[9]:


c


# In[2]:


a=np.arange(1,225)


# In[3]:


a


# In[4]:


a=np.reshape(a,(4,4,7,2))


# In[5]:


a


# In[17]:


ex=np.array([[[[ 10,  16],
                 [  8,  20],
                 [ 15,  20],
                 [ 15,  29],
                 [  9,  28],
                 [ 11,  26],
                 [ 10,  29]],

                [[ 13,  25],
                 [ 10,  20],
                 [ 14,  26],
                 [-13,  27],
                 [  9,  32],
                 [ 11,  30],
                 [ 14,  20]],

                [[  7,  26],
                 [  8,  27],
                 [  8,  24],
                 [  8,  25],
                 [ 12,  25],
                 [ 13,  30],
                 [  7,  20]],

                [[  8,  26],
                 [ 15,  20],
                 [ 15,  28],
                 [ 13,  21],
                 [  9,  28],
                 [  7,  30],
                 [  8,  28]]],


               [[[ 12,  24],
                 [ 13,  25],
                 [ 11,  31],
                 [  9,  32],
                 [ 15,  21],
                 [ 11,  22],
                 [  7,  31]],

                [[ 12,  29],
                 [  7,  22],
                 [ 11,  25],
                 [  9,  21],
                 [ 15,  20],
                 [  8,  30],
                 [  7,  28]],

                [[ 12,  21],
                 [  9,  27],
                 [  7,  21],
                 [  8,  22],
                 [ 12,  21],
                 [ 11,  31],
                 [  8,  25]],

                [[  9,  26],
                 [ 15,  25],
                 [ 10,  30],
                 [ 11,  32],
                 [ 12,  30],
                 [ 14,  23],
                 [  7,  27]]],


               [[[  1,  20],
                 [  3,  20],
                 [  5,  21],
                 [  4,  18],
                 [  2,  21],
                 [  5,   5],
                 [ 19,   6]],

                [[  5,  20],
                 [  2,  22],
                 [  7,  18],
                 [  4,  22],
                 [  6,  22],
                 [  5,   5],
                 [ 22,   6]],

                [[  8,  18],
                 [  8,  21],
                 [  7,  19],
                 [  5,  18],
                 [  5,  20],
                 [  3,   7],
                 [ 19,   7]],

                [[  6,  19],
                 [  3,  20],
                 [  5,  21],
                 [  2,  20],
                 [  3,  22],
                 [  8,   5],
                 [ 21,   7]]],


               [[[  9,  21],
                 [  8,  22],
                 [-10,  19],
                 [  9,  22],
                 [ 12,  18],
                 [ 12,  71],
                 [ 18,  12]],

                [[ 12,  19],
                 [ 12,  20],
                 [ 12,  18],
                 [ 12,  20],
                 [ 12,  20],
                 [ 11,   8],
                 [ 18,  10]],

                [[  8,  19],
                 [ 11,  22],
                 [  9,  18],
                 [  8,  18],
                 [  9,  20],
                 [  7,   8],
                 [ 18,   7]],

                [[  8,  18],
                 [ 11,  18],
                 [  9,  21],
                 [ 11,  20],
                 [  9,  22],
                 [  8,   9],
                 [ 19,  12]]]])
           


# In[15]:


temp=np.array([[[[7,29],[6,29],[6,25],[14,21],[10,28],[15,21],[14,20]],[[10,26],[13,32],[6,29],[-13,25],[7,31],[14,29],[12,31]],[[15,23],[12,25],[8,30],[8,31],[15,27],[12,27],[6,20]],[[6,29],[6,28],[7,32],[7,32],[14,32],[13,21],[14,25]]],[[[15,30],[9,20],[15,27],[15,23],[7,23],[15,30],[13,27]],[[9,28],[14,20],[6,21],[14,25],[11,21],[14,21],[10,20]],[[7,28],[6,27],[11,27],[11,20],[13,22],[15,20],[13,27]],[[11,23],[11,26],[11,21],[15,26],[9,21],[12,31],[6,24]]],[[[5,19],[7,19],[8,20],[6,19],[3,21],[5,7],[19,2]],[[4,22],[5,20],[6,20],[3,22],[6,18],[5,2],[18,3]],[[7,19],[5,22],[4,21],[8,21],[8,21],[2,3],[21,5]],[[5,21],[7,20],[2,19],[7,21],[4,18],[8,3],[21,8]]]
,[[[7,22],[9,22],[-10,19],[8,19],[12,20],[11,71],[21,7]],[[7,18],[11,19],[7,18],[8,18],[11,18],[11,7],[21,8]],[[10,19],[12,20],[7,21],[12,21],[8,18],[9,8],[21,9]],[[10,22],[8,19],[7,19],[12,20],[11,20],[12,8],[19,7]]]])


# In[16]:


#q1
temp


# In[20]:


#q2a
temp.shape


# In[21]:


#q2b
temp.ndim


# In[18]:


#q3 Print the daily temperatures for the first week of each month.
temp[:,:1]


# In[8]:


#q4 Print the temperatures for Tuesday of each month
temp[:,:,1:2,:]


# In[19]:


#q5 Print only the maximum temperature for all the weekdays of Dec and Feb.
temp[1::2,:,:,1:]


# In[22]:


#q6 Print all the days along with the week number in November when the minimum temperature was less than 8 degrees
for i in range (0,4):
    y=f[0,i:i+1,0:7,0:1]
    z=f[0,i:i+1,0:7,0:1]<8
    print("Week no. is: ",i+1)
    print(y[z])


# In[24]:


#q7 Print all the weeks in Dec and Jan where the maximum temperature has crossed a threshold of 20 degrees.

for i in range (0,4):
    y=f[1:4:2,i:i+1,0:7,1:2]
    z=f[1:4:2,i:i+1,0:7,1:2]>20
    print("Week no. is: ",i+1)
    print(y[z])


# In[47]:


#q8 Check if there are any absurd values present in the dataset
q1 = np.percentile(temp, 25)
q3 = np.percentile(temp, 75)
iqr = q3 - q1
threshold = 1.5 * iqr
outliers = np.where((temp < q1 - threshold) | (temp > q3 + threshold))

print("Outliers of array is : \n", temp[outliers])


# In[46]:


#q10 Find and print the indexes of all the outlier(unusual) values present in the above dataset.
outliers


# In[ ]:


#q11 Replace the outliers with an appropriate value.
temp[0,1,3,0]=15
temp[3,0,5,1]=30
print(temp)


# In[24]:


#q12 Find the average max temperature for the winter months in Jaipur.
b=np.average(temp[:,:,:,1:])
np.round(b,decimals=2)


# In[4]:


#q13 Find the weekly min avg temp for the month of Dec in Jaipur
a=np.mean(temp[1::4,0:1,:,0::2])
a=np.round(a,decimals=2)
b=np.mean(temp[1::4,1:2,:,0::2])
b=np.round(b,decimals=2)
c=np.mean(temp[1::4,2:3,:,0::2])
c=np.round(c,decimals=2)
d=np.mean(temp[1::4,3:4,:,0::2])
d=np.round(d,decimals=2)
print(a,"",b,"",c,"",d)


# In[9]:


#q14 Find the overall avg temp for the months Dec and Jan

b=np.average(temp[1:3,:,:,:])
np.round(b,decimals=2)


# In[41]:


#15.Find the least temp experienced by the city in the month of Dec and Jan. Also print the exact date( Day/Week/Month) for the same.
mindec = np.min(temp[1])
minjan = np.min(temp[2])
c = np.where(temp[1]==mindec)
print(c)
print("december : ")
for i,n in zip(c[0],c[1]):
  print(f'week: {i+1} day: {n+1} ', mindec)

d = np.where(temp[2]==mindec)
print(d)
print("janurary : ")
for i,n in zip(d[0],d[1]):
    print(f'week: {i+1} day: {n+1} ', minjan)


# In[42]:


#16 Find the max temp in the month of Feb and return its date(Day/Week/Month)
maxfeb = np.max(temp[3])
c=np.where(temp[3]==maxfeb)
print('max temp in feb = ', maxfeb)
print(c)
for i , n in zip(c[0],c[1]):
    print(f'feb: Week{i+1}, day{n+1} : ',maxfeb)


# In[39]:


#q17 Find the days in the month of Nov where the max temp of the day dropped below the avg temp of the month.
b=np.average(temp[0::4])
c=np.round(b,decimals=2)
print("average temp of november is:",c)
d=np.where(temp[0::4,:,:,1:]<c)
print(d)


# In[48]:


#18 Convert the above dataset into an array where the weeks of the same 
#month must be present in the same row, but belonging to different months
#should come in a row either below or above the selected month
np.reshape(temp,(4,56))


# In[43]:


#q19 The above data is appropriate for an audience who follow the metric system of measurement. Create an array that holds the same data but presented in Fahrenheit.
cel=np.array(temp)
feh=((9*cel/5)+32)
print("temperature in fahrenheit is:\n",feh)


# In[44]:


#q20 Sort the above data in descending order on the basis of weekly average for the month of Dec
a=np.mean(temp[1::4,0::4,:,:])
b=np.mean(temp[1::4,1::4,:,:])
c=np.mean(temp[1::4,2::4,:,:])
d=np.mean(temp[1::4,3::4,:,:])
arr=np.array([a,b,c,d])
arr[::-1].sort()
print(arr)



# In[45]:


#q22 Create an array that stores the difference between the min and max temp for each day in all the winter month
a=temp[:,:,:,1:]
b=temp[:,:,:,0::2]
c=a-b
print("difference between max and min temp:\n",c)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




