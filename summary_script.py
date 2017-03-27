##################################################################################################################
#
#Dataquest challenge to get more comfortable using Pandas to manipulate DataFrames and calculate summary statistics
#Data from https://github.com/fivethirtyeight/data/tree/master/college-majors files all-ages.csv & recent-grads.csv
#execfile('summary_script.py')
#"X:\HomeDirs\Documents\Data Science\Challenge Summarizing Data"
#
##################################################################################################################


#Question 2: Read data in
import pandas as pd

#Import data
all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv")
print(all_ages[0:5])
print(recent_grads[0:5])


#Question 3: Summarize the number of people in each Major_category for both data sets
	
def total_col_count(dframe, column):
	cat_counts = {}
	unique_values = list(dframe[column].unique())
	
	for category in unique_values:
		rows = dframe[dframe[column] == category]
		sum_of_values = rows['Total'].sum()
		cat_counts[category] = sum_of_values
		
	return cat_counts
	
aa_cat_counts = total_col_count(all_ages, "Major_category")
rg_cat_counts = total_col_count(recent_grads, "Major_category")
print(aa_cat_counts)
print(rg_cat_counts)


#Question 4: Calculate the proportion of recent college graduates that worked low wage jobs

low_wage_percent = 0.0
total_col = float(recent_grads["Total"].sum())
total_low_wage = float(recent_grads["Low_wage_jobs"].sum())
low_wage_percent = total_low_wage / total_col


#Question 5: 
majors = recent_grads['Major'].unique()
rg_lower_count = 0

sorted_recent_grads = recent_grads.sort("Major_code")

for m in majors:
	grads = sorted_recent_grads.loc[recent_grads["Major"] == m]
	all = all_ages.loc[all_ages["Major"] == m]
	
	grad_unemployment = grads.iloc[0]['Unemployment_rate']
	all_unemployment = all.iloc[0]["Unemployment_rate"]
	
	
	if grad_unemployment < all_unemployment:
		rg_lower_count += 1
		
print(rg_lower_count)
	
	
	
	
	
	
	
	
	
