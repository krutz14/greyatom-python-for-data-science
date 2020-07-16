# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)
bank=pd.DataFrame(bank_data)
categorical_var=bank.select_dtypes(include='object')
#print(categorical_var)
numerical_var=bank.select_dtypes(include='number')
#print(numerical_var)
banks=bank.drop(["Loan_ID"],axis=1)
#print(banks.shape)
#print(banks.isnull().sum())
bank_mode=banks.mode()
#print(bank_mode)
#print(banks.head())
for column in banks.columns:
    banks[column].fillna(banks[column].mode()[0],inplace=True)
#print(banks.isnull().sum().values.sum())
#for column in df.columns:
 #   df[column].fillna(df[column].mode()[0], inplace=True)
#print(banks)
avg_loan_amount=banks.pivot_table(index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc=np.mean)
#print(avg_loan_amount['LoanAmount'][1],2)

loan_approved_se=banks[(banks['Self_Employed']=='Yes')& (banks['Loan_Status']=='Y')].count()
#print(loan_approved_se)
loan_approved_nse=banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')].count()
#print(loan_approved_nse)
percentage_se=round((loan_approved_se/614)*100,2)
#print(percentage_se)

percentage_nse=round((loan_approved_nse/614)*100,2)
#print(percentage_sne)
loan_term=banks.apply(lambda x: (x/12) if x.name=='Loan_Amount_Term' else x)
#print(loan_term.head())
big_loan_term=loan_term[loan_term['Loan_Amount_Term'] >= 25.0].count()
#print(big_loan_term)
#step5
#new_df = df[df.apply(lambda x : len(x['Title'].split(" "))>=4,axis=1)]

#dfObj.apply(lambda x: np.square(x) if x.name == 'z' else x)

loan_groupby=banks.groupby('Loan_Status')
loan_groupby=loan_groupby['ApplicantIncome', 'Credit_History']
mean_values=round(loan_groupby.mean(),2)
print(mean_values.iloc[1,0], 2)



#Code starts here




