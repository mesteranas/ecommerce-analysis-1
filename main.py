import pandas as pd
import functions
import os

# Initialize the report string
analysis_report = ""

# Check if the output folder exists if not create it
if not os.path.exists("output"):
    os.makedirs("output")
# Load the transactional dataset
df = pd.read_csv("ecommerce_transactions.csv")

# Identify the country with the highest number of transactions
country_counts = df.groupby("Country")["User_Name"].count()
top_country = country_counts.idxmax()
top_country_count = country_counts.max()
analysis_report += f"{top_country} is the country with the most transactions with {top_country_count} transactions.\n\n"

# Identify the most frequently used payment method
payment_method_counts = df["Payment_Method"].value_counts()
analysis_report += f"The most used payment method is {payment_method_counts.idxmax()} with {payment_method_counts.max()} transactions.\n\n"

# Identify the country with the highest total purchase amount
country_spending = df.groupby("Country")["Purchase_Amount"].sum()
analysis_report += f"{country_spending.idxmax()} is the country with the most money spent.\n"

# Identify the most common product category by transaction volume
category_counts = df["Product_Category"].value_counts()
analysis_report += f"{category_counts.idxmax()} is the most common category with {category_counts.max()} transactions.\n"

# Identify the product category generating the most revenue
category_revenue = df.groupby("Product_Category")["Purchase_Amount"].sum()
analysis_report += f"{category_revenue.idxmax()} is the category that brings in the most revenue: {category_revenue.max()}.\n\n"

# Identify the highest spending user
user_spending = df.groupby("User_Name")["Purchase_Amount"].sum()
analysis_report += f"{user_spending.idxmax()} is the highest spender with {user_spending.max()}.\n\n"

# Identify the most active shopper
user_purchase_frequency = df["User_Name"].value_counts()
analysis_report += f"{user_purchase_frequency.idxmax()} bought {user_purchase_frequency.max()} times.\n\n"
with open("report.md","w",encoding="utf-8") as file:
    file.write(analysis_report)
    print("Done")
# Create country data frame
CountryDF=pd.DataFrame(columns=["Country","Revenue","Top user","Most Frequent Payment Method","Most populer category","Transactions","Ranking"])
CountryDF["Country"]=df["Country"].unique()
CountryDF.set_index("Country",inplace=True)
# country group
countryGroup=df.groupby("Country")
CountryDF["Revenue"]=countryGroup["Purchase_Amount"].sum()
CountryDF["Top user"]=countryGroup.apply(functions.GetTopUser)
CountryDF["Most Frequent Payment Method"]=countryGroup.apply(functions.getMostFrequentPaymentMethod)
CountryDF["Most populer category"]=countryGroup.apply(functions.getMostPopulerCategory)
CountryDF["Transactions"]=countryGroup["Transaction_ID"].count()
CountryDF["Ranking"]=CountryDF["Revenue"].rank(ascending=False).astype("int64")
CountryDF=CountryDF.sort_values("Ranking",ascending=True)
CountryDF=CountryDF.reset_index()
CountryDF.to_excel("output/country.xlsx",index=False)
print("Done")
