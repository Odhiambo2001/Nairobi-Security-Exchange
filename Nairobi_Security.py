import pandas as pd
#save file to a variable for easy access
Nairobi_file_path=("C:/Users/Administrator/Downloads/Nairobi All Share Historical Data.csv")
#Read the data and store data in Dataframe titled Nairobi_data
Nairobi_data=pd.read_csv(Nairobi_file_path)
#is the DataFrame object that contains the data read from the CSV file.
Nairobi_data
#print a summary of the data in Nairobi_data
print(Nairobi_data.describe())
# method that returns the same summary statistics as describe(), but without printing them to the console.
Nairobi_data.describe()
#displays the first 5 rows of the Nairobi_data DataFrame.
print(Nairobi_data.head())
#What is the average price (rounded to the nearest interger)?
avg_price = round(Nairobi_data['Price'].mean())
print("The average price is:", avg_price)
#Display the entire dataframe
print(Nairobi_data)
#Calculate the percentage change


Nairobi_data['Date']=pd.to_datetime(Nairobi_data['Date'])#Convert Date to datetime


latest_date=Nairobi_data['Date'].max()#get the latest date
percentage_change = (latest_date - pd.to_datetime('today')).days / (latest_date - Nairobi_data['Date'].min()).days * 100
print("The percentage change is:",percentage_change)





