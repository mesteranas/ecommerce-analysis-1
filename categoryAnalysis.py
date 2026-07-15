import pandas as pd
import os

# Check if the output folder exists if not create it
if not os.path.exists("output"):
    os.makedirs("output")
# Functions
def GetTopUser(category:pd.Series):
    userGroup=category.groupby("User_Name")["Purchase_Amount"].sum()
    return userGroup.idxmax()
def getTopCountry(category:pd.Series):
    countryGroup=category.groupby("Country")["Purchase_Amount"].sum()
    return countryGroup.idxmax()
# Load the transactional dataset
df = pd.read_csv("ecommerce_transactions.csv")
# Category analysis
categoryDF=pd.DataFrame(columns=["Category","Revenue","Top user","Top country","Transactions count","Ranking"])
categoryDF["Category"]=df["Product_Category"].unique()
categoryDF.set_index("Category",inplace=True)
categoryGroup=df.groupby("Product_Category")
categoryDF["Revenue"]=categoryGroup["Purchase_Amount"].sum()
categoryDF["Top user"]=categoryGroup.apply(GetTopUser)
categoryDF["Top country"]=categoryGroup.apply(getTopCountry)
categoryDF["Transactions count"]=categoryGroup["Transaction_ID"].count()
categoryDF["Ranking"]=categoryDF["Revenue"].rank(ascending=False).astype("int64")
categoryDF=categoryDF.sort_values("Ranking",ascending=True)
categoryDF=categoryDF.reset_index()
categoryDF.to_excel("output/category.xlsx",index=False)
print("Done")