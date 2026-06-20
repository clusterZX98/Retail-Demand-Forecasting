# 🛒 Walmart Store Sales Analysis Dashboard

## 1. Project Title

**Walmart Store Sales Analysis & Forecasting Dashboard**

A data analytics project that explores Walmart store performance using historical weekly sales data. The project uncovers sales trends, holiday impacts, economic influences, and store-level performance through data analysis and interactive visualizations.

---

## 2. Problem Statement

Retail businesses generate massive amounts of sales data every week. Understanding sales patterns, identifying key drivers, and predicting future performance are critical for making informed business decisions.

This project aims to:

* Analyze Walmart's historical weekly sales data.
* Identify factors affecting sales performance.
* Understand holiday season impacts on revenue.
* Evaluate economic indicators such as fuel price, CPI, and unemployment.
* Create actionable insights for store managers and business stakeholders.
* Build a foundation for future sales forecasting models.

---

## 3. Features

### 📊 Data Analysis

* Weekly sales trend analysis
* Store-wise sales comparison
* Holiday vs Non-Holiday sales performance
* Economic indicator analysis

### 📈 Interactive Visualizations

* Sales trend charts
* Store performance dashboards
* Correlation heatmaps
* Seasonal analysis

### 🧠 Business Insights

* Best-performing stores
* Worst-performing stores
* Impact of unemployment on sales
* Impact of fuel prices on consumer spending

### 🔮 Future Scope

* Sales forecasting using Machine Learning
* Demand prediction
* Inventory optimization
* Automated reporting system

---

## 4. Tech Stack

### Programming Language

* Python 3.10+

### Libraries

pandas
numpy
matplotlib
plotly
seaborn
scikit-learn
xgboost
lightgbm
prophet
tensorflow
fastapi
uvicorn
pymongo
sqlalchemy
python-dotenv
mlflow
evidently
joblib
requests
pydantic
jinja2
catboost
statsmodels




### Dashboard Framework (Optional)

* Streamlit

### Development Tools

* VS Code
* Jupyter Notebook
* Git
* GitHub

---

## 5. Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/walmart-sales-analysis.git
```

### Navigate to Project Folder

```bash
cd walmart-sales-analysis
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6. Usage

### Run Analysis Notebook

```bash
jupyter notebook
```

Open:

```bash
Walmart_Sales_Analysis.ipynb
```

### Run Streamlit Dashboard

```bash
streamlit run app.py
```

Dashboard will be available at:

```bash
http://localhost:8501
```

---

## Dataset Information

### Source

Walmart Store Sales Dataset

### Dataset Size

* Records: 6,435
* Features: 8

### Columns

| Feature      | Description                                      |
| ------------ | ------------------------------------------------ |
| Store        | Store Number                                     |
| Date         | Weekly Date                                      |
| Weekly_Sales | Weekly Revenue                                   |
| Holiday_Flag | Holiday Indicator (1 = Holiday, 0 = Non-Holiday) |
| Temperature  | Temperature in Region                            |
| Fuel_Price   | Regional Fuel Price                              |
| CPI          | Consumer Price Index                             |
| Unemployment | Unemployment Rate                                |

---

## Key Business Questions

1. Which stores generate the highest revenue?
2. How do holidays affect sales?
3. Does fuel price impact sales?
4. How does unemployment affect consumer spending?
5. What are the seasonal sales patterns?
6. Which factors are most correlated with sales?

---

## 7. API Endpoints

### If Using Streamlit Only

No backend API is required.

### Future FastAPI Integration

#### Get Overall Sales

```http
GET /sales/overall
```

#### Get Store Sales

```http
GET /sales/store/{store_id}
```

#### Holiday Sales Analysis

```http
GET /sales/holiday
```

#### Sales Forecast

```http
POST /forecast
```

Request:

```json
{
    "store_id": 1,
    "weeks": 12
}
```

Response:

```json
{
    "predicted_sales": [...]
}
```

---

## 8. Screenshots

### Dashboard Overview

Insert Screenshot Here

```markdown
![Dashboard](images/dashboard.png)
```

### Sales Trend Analysis

```markdown
![Sales Trend](images/sales_trend.png)
```

### Correlation Heatmap

```markdown
![Heatmap](images/heatmap.png)
```

### Store Performance Dashboard

```markdown
![Store Analysis](images/store_analysis.png)
```

---

## 9. Deployment

### Streamlit Cloud

```bash
https://your-app-name.streamlit.app
```

### Render

```bash
https://your-app-name.onrender.com
```

### Railway

```bash
https://your-app-name.up.railway.app
```

### Deployment Steps

1. Push project to GitHub.
2. Connect repository to Streamlit Cloud or Render.
3. Configure dependencies using `requirements.txt`.
4. Deploy application.
5. Share public dashboard URL.

---

## Project Structure

```text
walmart-sales-analysis/
│
├── data/
│   └── Walmart_Store_sales.csv
│
├── notebooks/
│   └── Walmart_Sales_Analysis.ipynb
│
├── dashboard/
│   └── app.py
│
├── images/
│   ├── dashboard.png
│   ├── heatmap.png
│   └── sales_trend.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 10. Contributors

### Piyush Rawat

* Data Analysis
* Dashboard Development
* Business Insights
* Documentation

GitHub:

```text
https://github.com/yourusername
```

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

* Walmart Sales Dataset
* Python Open Source Community
* Pandas Documentation
* Streamlit Community

⭐ If you found this project useful, consider giving it a star on GitHub.

