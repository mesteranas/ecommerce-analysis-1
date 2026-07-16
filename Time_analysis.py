import pandas as pd
import os

# Check if the output folder exists if not create it
if not os.path.exists("output"):
    os.makedirs("output")
# Load the transactional dataset
df = pd.read_csv("ecommerce_transactions.csv")
df["Transaction_Date"]=pd.to_datetime(df["Transaction_Date"])
df.sort_values("Transaction_Date",ascending=True,inplace=True)
# create the output data frame
timeDF=pd.DataFrame(columns=["Month","Revenue","Revenue Growth %","Transactions count"])
timeDF["Month"]=df["Transaction_Date"].dt.strftime("%m/%Y").unique()
timeDF.set_index("Month",inplace=True)
timeGroup=df.groupby(df["Transaction_Date"].dt.strftime("%m/%Y"))
timeDF["Revenue"]=timeGroup["Purchase_Amount"].sum()
timeDF["Transactions count"]=timeGroup["Transaction_ID"].count()
timeDF["Revenue Growth %"]=(timeDF["Revenue"].pct_change()*100).round(2)
timeDF.reset_index(inplace=True)
timeDF.to_excel("output/Time_analysis.xlsx",index=False)
print("Done")