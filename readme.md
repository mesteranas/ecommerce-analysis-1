# ecommerce-analysis-1

A Python project that analyzes an e-commerce transactions dataset using **Pandas**. It generates business insights by analyzing countries, product categories, and monthly sales trends, then exports the results as Excel spreadsheets and a Markdown report.

This project was created as a learning exercise in data analysis and demonstrates practical use of Pandas for working with real-world transactional data.

## Features

- Country-level sales and transaction analysis
- Product category analysis
- Monthly revenue and transaction trend analysis
- Month-over-month revenue growth calculation
- Automatic Excel report generation
- Automatic Markdown report generation
- Clean and readable Python code

## Requirements

- Python 3.10+
- pandas

Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the analysis scripts:

```bash
python Country_analysis.py
python categoryAnalysis.py
python Time_analysis.py
python report.py
```

The generated reports will be saved automatically in the `output` directory.

## Files

| File | Description |
|------|-------------|
| `Country_analysis.py` | Analyzes the dataset by country. Calculates total revenue, transaction count, most popular payment method, most popular product category, top customer, and country revenue rankings. Exports the results to `output/country.xlsx`. |
| `categoryAnalysis.py` | Performs product category analysis, including revenue, transaction count, top customer, highest-revenue country, and category rankings. Exports the results to `output/category.xlsx`. |
| `Time_analysis.py` | Performs monthly time-series analysis, including monthly revenue, transaction count, and month-over-month revenue growth. Exports the results to `output/Time_analysis.xlsx`. |
| `report.py` | Generates a Markdown report summarizing the key insights discovered during the analysis. The report is saved as `output/report.md`. |
| `ecommerce_transactions.csv` | The dataset used for all analyses. |
| `requirements.txt` | Lists the required Python packages. |
| `resources.txt` | Contains the link to the original dataset. |
| `output/` | Contains all generated reports after running the analysis scripts. |

## Output

Running the project generates:

- `country.xlsx`
- `category.xlsx`
- `Time_analysis.xlsx`
- `report.md`

inside the `output` directory.

## Dataset

This project uses the **E-Commerce Transactions Dataset** created by **smayanj**.

Original source:
https://www.kaggle.com/datasets/smayanj/e-commerce-transactions-dataset/data

All credit for the dataset belongs to its original author.

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

The dataset is distributed separately by its original author. Please refer to the original Kaggle page for its licensing information and future updates.

## Author

**Anas Youssef**

GitHub: https://github.com/mesteranas

---

If you found this project useful, consider giving the repository a ⭐ and crediting the original dataset creator.