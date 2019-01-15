# Gender						{'F':0, 'M':1}
# Age							{'0-17':0, '18-25':1, '26-35':2, '36-45':3, '46-50':4, '51-55':5, '55+':6}
# Occupation 					from 0 to 20
# City_Category					{'A':0, 'B':1, 'C':2}
# Stay_In_Current_City_Years    from 0 to 4
# Marital_Status				{'Yes':1, 'No':0}
# Product_Category_1 			from 1 to 18
# Product_Category_2 			from 1 to 18
# Product_Category_3 			from 1 to 18
# Product_ID					string

import pandas as pd

def pre_process(Gender, Age, Occupation, City_Category, Stay_In_Current_City_Years, 
				Marital_Status, Product_ID, Product_Category_1, Product_Category_2, Product_Category_3):
				
	Stay_In_Current_City_Years_0 = 0
	Stay_In_Current_City_Years_1 = 0
	Stay_In_Current_City_Years_2 = 0
	Stay_In_Current_City_Years_3 = 0
	Stay_In_Current_City_Years_4 = 0

	if Stay_In_Current_City_Years == 0:
		Stay_In_Current_City_Years_0 = 1
	elif Stay_In_Current_City_Years == 1:
		Stay_In_Current_City_Years_1 = 1
	elif Stay_In_Current_City_Years == 2:
		Stay_In_Current_City_Years_2 = 1
	elif Stay_In_Current_City_Years == 3:
		Stay_In_Current_City_Years_3 = 1
	else:
		Stay_In_Current_City_Years_4 = 1

	Age_Count = pd.read_csv('Age_Count.csv', index_col=0)['0']
	Occupation_Count = pd.read_csv('Occupation_Count.csv', index_col=0)['0']
	Product_Category_1_Count = pd.read_csv('Product_Category_1_Count.csv', index_col=0)['0']
	Product_Category_2_Count = pd.read_csv('Product_Category_2_Count.csv', index_col=0)['0']
	Product_Category_3_Count = pd.read_csv('Product_Category_3_Count.csv', index_col=0)['0']
	Product_ID_Count = pd.read_csv('Product_ID_Count.csv', index_col=0)['0']

	df = pd.DataFrame([Gender, Age, Occupation, City_Category, Marital_Status, 
					Product_Category_1, Product_Category_2, Product_Category_3, 
					Stay_In_Current_City_Years_0, Stay_In_Current_City_Years_1, 
					Stay_In_Current_City_Years_2, Stay_In_Current_City_Years_3, Stay_In_Current_City_Years_4, 
					Age_Count[Age], Occupation_Count[Occupation], 
					Product_Category_1_Count[Product_Category_1], Product_Category_2_Count[Product_Category_2], 
					Product_Category_3_Count[Product_Category_3], Product_ID_Count[Product_ID]], 
		columns=['Gender','Age','Occupation','City_Category','Marital_Status',
				'Product_Category_1','Product_Category_2','Product_Category_3',
				'Stay_In_Current_City_Years_0','Stay_In_Current_City_Years_1',
				'Stay_In_Current_City_Years_2','Stay_In_Current_City_Years_3','Stay_In_Current_City_Years_4',
				'Age_Count','Occupation_Count','Product_Category_1_Count','Product_Category_2_Count',
				'Product_Category_3_Count','Product_ID_Count'])

	return df

#print(pre_process(Gender = 0, Age = 0, Occupation = 10, City_Category = 0, Stay_In_Current_City_Years = 2, 
#				Marital_Status = 0, Product_ID = 'P00248942', Product_Category_1 = 1, Product_Category_2 = 6, Product_Category_3 = 14))