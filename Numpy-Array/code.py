# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
new_record=np.array(new_record)
cencus=np.concatenate((data,new_record),axis=0)

age=cencus[:,0] 

max_age=np.amax(age)
min_age=np.amin(age)
age_mean=np.mean(age)
age_std=np.std(age)
print(np.shape(data),np.shape(cencus),type(age),min_age,max_age,"{:.2f}".format(age_mean),"{:.2f}".format(age_std))

race=cencus[:,2]
race_0=race[(race==0)]
race_1=race[(race==1)]
race_2=race[(race==2)]
race_3=race[(race==3)]
race_4=race[(race==4)]
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
minority_race=[len_0,len_1,len_2,len_3,len_4].index(min([len_0,len_1,len_2,len_3,len_4]))
print(minority_race)
senior_citizen=age[(age>60)]
senior_citizen_len=len(senior_citizen)
working_hours_sum=0
for x in cencus:
    if x[0]>60:
        working_hours_sum+=x[6]
avg_working_hours=working_hours_sum/senior_citizen_len
print("{:.2f}".format(avg_working_hours))
education_num=cencus[:,1] 
high=education_num[(education_num>10)]
low=education_num[(education_num<=10)]
avg_pay_high=0
avg_pay_low=0
for x in cencus:
    if x[1]>10:
        avg_pay_high+=x[7]
    elif x[1]<=10:
        avg_pay_low+=x[7]
avg_pay_high=avg_pay_high/len(high)
avg_pay_low=avg_pay_low/len(low)
print("{:.2f}".format(avg_pay_high))
print("{:.2f}".format(avg_pay_low))








