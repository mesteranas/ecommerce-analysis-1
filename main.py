import pandas as pd
import os

# Check if the output folder exists if not create it
if not os.path.exists("output"):
    os.makedirs("output")
# Load the transactional dataset
df = pd.read_csv("ecommerce_transactions.csv")
