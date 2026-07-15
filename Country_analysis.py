import pandas as pd

import os


# Check if the output folder exists if not create it
if not os.path.exists("output"):
    os.makedirs("output")
# Functions
def GetTopUser(country:pd.Series):
    userGroup=country.groupby("User_Name")["Purchase_Amount"].sum()
    return userGroup.idxmax()
def getMostFrequentPaymentMethod(country:pd.Series):
    PaymentGroup=country["Payment_Method"].value_counts()
    return PaymentGroup.idxmax()
def getMostPopulerCategory(country:pd.Series):
    categoryGroup=country["Product_Category"].value_counts()
    return categoryGroup.idxmax()
# Load the transactional dataset
df = pd.read_csv("ecommerce_transactions.csv")

# Create country data frame
CountryDF=pd.DataFrame(columns=["Country","Revenue","Top user","Most Frequent Payment Method","Most populer category","Transactions","Ranking"])
CountryDF["Country"]=df["Country"].unique()
CountryDF.set_index("Country",inplace=True)
# country group
countryGroup=df.groupby("Country")
CountryDF["Revenue"]=countryGroup["Purchase_Amount"].sum()
CountryDF["Top user"]=countryGroup.apply(GetTopUser)
CountryDF["Most Frequent Payment Method"]=countryGroup.apply(getMostFrequentPaymentMethod)
CountryDF["Most populer category"]=countryGroup.apply(getMostPopulerCategory)
CountryDF["Transactions"]=countryGroup["Transaction_ID"].count()
CountryDF["Ranking"]=CountryDF["Revenue"].rank(ascending=False).astype("int64")
CountryDF=CountryDF.sort_values("Ranking",ascending=True)
CountryDF=CountryDF.reset_index()
CountryDF.to_excel("output/country.xlsx",index=False)
print("Done")
