# -*- coding: utf-8 -*-
"""
Created on Wed May  1 14:36:07 2019
Python: Pandas. - Data Analysis. Basic Tasks.
@author: Carla Pastor
Note: The mask used is similar to NumPy boolean mask. Examples; df[df['c1']>11] # df[boolean_mask]
or, 	bool_mask = df % 3 == 0
		df[bool_mask] # returns values where it is True and NaN where False.
 
# Source provided: Customers_Purchases (Excel file)
"""
 
# Find in which directory you are in at the moment? (your current working directory on your computer)

import os
cwd = os.getcwd()
cwd

# Loop through the files in your working directory and display their names

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    print (f)
	
# import pandas 
import pandas as pd

# 1. Load the data in a variable "cust", data file name is 'Customers_Purchases.csv'.

cust = pd.read_csv('Customers_Purchases.csv')
cust = pd.read_csv('Customers_Purchases.csv')

# 2. Its good idea to see how the data look like, display first 5 rows of your data-set.

cust.head()

# 3. How many entries your data have? Can you tell the no. of columns in your data?

cust.info()

# 4. What are the max and min ages of your customer? Can you find mean of your customer?

print('Max. age of the customer is: ',cust['age'].max())
print('Max. age of the customer is: ', cust['age'].min())
print('Avg. age of the customer is: ',cust['age'].mean())

# 5. What are the three most common customer's names?
# Note: value_counts() returns object containing counts of unique values. The resulting object will be in descending order so that the first element is the most frequently-occurring element. Excludes NA values by default.

cust['first'].value_counts().head(3)

# 6. Two customers have the same phone number, can you find those customers?
# Note: lets find what phone number is twice

cust['phone'].value_counts().head(2)

# Now we know the phone number, let's find out the other information.
cust[cust['phone'] == '(999) 989-9009']

# 7. How many customers have profession "Structural Engineer"?

cust[cust['profession'] == 'Structural Engineer'].count()

# use any column such as ['last'] to get a number
cust[cust['profession'] == 'Structural Engineer'].count()['last']

# 8. How many male customers are 'Structural Engineer'?

cust[(cust['profession'] == 'Structural Engineer') & (cust['gender']=='Male')].count()

# 9. Find out the female Structural Engineers from province Alberta (AB)?

cust[(cust['profession'] == 'Structural Engineer') & (cust['gender']=='Female') & (cust['province']=='AB')]
	 
# 10. What is the max, min and average spending?

print('Max. spending: ',cust['price(USD)'].max())
print('Mai. spending: ', cust['price(USD)'].min())
print('Avg. spending: ',cust['price(USD)'].mean())	 
	 
# 11. Who did not spend anything? Company wants to send a deal to encourage the customer to buy stuff!

cust[cust['price(USD)']==0.0]

# 12. As a loyalty reward, company wants to send thanks coupon to those who spent $100 or more, please find out the customers?

cust[cust['price(USD)']>=100.0]

# 13. How many emails are associated with this credit card number '9090400010000900'?

#cust[cust['cc_no']==9090400010000900].count()
cust[cust['cc_no']==9090400010000900]['email']	 
	 
# 14. We need to send new cards to the customers well before the expire, how many cards are expiring in 2019?
# Note: Use sum() and count() and see the difference in their use 

#cust[cust['cc_exp'].apply(lambda x: x[5:]) == '19'].count()
sum(cust['cc_exp'].apply(lambda x: x[5:]) == '19')

# 15. How many people use Visa as their Credit Card Provider?

sum(cust['cc_type']=='Visa')
	 
# 16. Can you find the customer who spent 100 USD using Visa?
# cust['cc_type'].unique() # to check all types first

cust[(cust['cc_type']=='Visa') & (cust['price(USD)'] == 100.0)]	 
	 
# 17. What are two most common professions?

cust['profession'].value_counts().head(2)	 
	 
# 18. Can you tell the top 5 most popular email providers? (e.g. gmail.com, yahoo.com, etc...)

cust['email'].apply(lambda x: x.split('@')[1]).value_counts().head(5)	 
	 
# 19. Is there any customer who is using email with "am.edu"?
# Note: Use lambda expression in apply(). split the email address at @.

cust[cust['email'].apply(lambda x: x.split('@')[1])=='am.edu']
	 
# 20. Which day of the week, the store gets more customers?

cust['weekday'].value_counts().head()	 
	 
# File in process.. 
	 
	 
	 