# E-Commerce Transactions Analyzer



## 📖 Project Explanation



This project is a data analysis utility that processes e-commerce transaction workflows using the Python `pandas` library. The core script (`main.py`) reads a transactional dataset to automatically evaluate database records and extract high-level business intelligence metrics.



The system programmatically evaluates the data to generate insights across the following core areas:



* **Geographic Volume:** It determines which country handles the highest overall volume of user transactions.





* **Financial Performance:** It aggregates total purchases to pinpoint the country where the most money is spent.





* **Payment Preferences:** It isolates the single most frequently utilized payment method across the entire customer base.





* **Product Category Analytics:** It tracks transaction frequencies to identify the most common product category, alongside calculating cumulative sales values to reveal the highest revenue-generating product category.





* **Customer Behavior:** It identifies the platform's highest-spending user by total purchase value and isolates the most active shopper based on order frequency.







All computed metrics are compiled directly into an automated Markdown text file (`report.md`) for quick executive reviews.



---



## ⚖️ Legal Notice & Attribution



* **Dataset Source:** The foundational data utilized by this application is derived from the public **E-Commerce Transactions Dataset** curated by *smayanj* on Kaggle.

* **Repository Status:** For ease of immediate local deployment and execution, a copy of the transactional dataset (`ecommerce_transactions.csv`) is bundled directly within this project repository.





* **Licensing:** Both the original Kaggle source dataset and this analytical codebase are officially licensed under the terms of the **MIT License**. You are permitted to use, modify, merge, publish, and distribute this work freely, provided that the original license and copyright notices are preserved.

