import pandas as pd
def GetTopUser(country:pd.Series):
    userGroup=country.groupby("User_Name")["Purchase_Amount"].sum()
    return userGroup.idxmax()
def getMostFrequentPaymentMethod(country:pd.Series):
    PaymentGroup=country["Payment_Method"].value_counts()
    return PaymentGroup.idxmax()
def getMostPopulerCategory(country:pd.Series):
    categoryGroup=country["Product_Category"].value_counts()
    return categoryGroup.idxmax()