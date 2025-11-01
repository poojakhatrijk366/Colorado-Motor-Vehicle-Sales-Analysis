🚘 Colorado Motor Vehicle Sales Data Analysis (2018–2024)

*Author:* Sushma J — Finance Analyst  
*Tool:* Python (Visual Studio Code / Jupyter Notebook)  
*Dataset:* colorado_motor_vehicle_sales.csv  
*Script:* colorado_motor_vehicle_sales_analysis.py

---

## 📖 Project Overview
This project analyzes vehicle sales trends in Colorado from *2018 to 2024*, focusing on different manufacturers, models, and vehicle types.  
The analysis helps identify *sales performance, market share, pricing trends,* and *revenue contribution* across vehicle categories.

---

## 🎯 Objectives
- Analyze sales growth trends for major vehicle manufacturers.  
- Compare vehicle types (SUV, Sedan, Truck) performance over years.  
- Identify average pricing patterns and revenue leaders.  
- Visualize top-performing brands in terms of sales and revenue.

---

## 📂 Project Structure

Colorado-Motor-Vehicle-Sales-Analysis/
│
├── colorado_motor_vehicle_sales.csv               # Dataset file
├── colorado_motor_vehicle_sales_analysis.py       # Python analysis code
├── requirements.txt                               # Dependencies list
├── README.md                                      # Project documentation
│
├── 1_total_sales_trend.png                        # Graph: Total vehicle sales over years
├── 2_sales_by_vehicle_type.png                    # Graph: Sales distribution by vehicle type
├── 3_average_price_trend.png                      # Graph: Average vehicle price trend
├── 4_top_manufacturers_revenue.png                # Graph: Top manufacturers by total revenue
└── 5_units_sold_by_brand.png                      # Graph: Units sold comparison among brands


---

## ⚙ Setup Instructions

### 1️⃣ Clone the Repository
bash
git clone https://github.com/<your-username>/Colorado-Motor-Vehicle-Sales-Analysis.git
cd Colorado-Motor-Vehicle-Sales-Analysis


### 2️⃣ Create a Virtual Environment
bash
python -m venv env
source env/bin/activate      # For Mac/Linux
env\Scripts\activate         # For Windows


### 3️⃣ Install Dependencies
bash
pip install -r requirements.txt


### ▶ Run the Project
bash
python colorado_motor_vehicle_sales_analysis.py


---

## 📊 Generated Graphs
1️⃣ *Total Sales Trend (2018–2024)* – Line chart showing total sales growth.  
2️⃣ *Sales by Vehicle Type* – Bar chart comparing SUVs, Sedans, and Trucks.  
3️⃣ *Average Price Trend* – Line chart showing changes in vehicle pricing.  
4️⃣ *Top Manufacturers by Revenue* – Horizontal bar chart of revenue leaders.  
5️⃣ *Units Sold by Brand* – Bar chart comparing brand-wise performance.

---

## 📈 Output Summary
- Year-over-year vehicle sales and pricing analysis.  
- Total revenue and units sold by each manufacturer.  
- Top-performing brands in Colorado vehicle market.  
- All graphs automatically saved as .png in the project folder.

---

## 🧩 Dependencies
- pandas  
- matplotlib  
- seaborn  
- numpy  
- os  

---

## 🏁 Conclusion
This analysis provides clear insights into *Colorado’s motor vehicle market, helping stakeholders understand which brands, models, and vehicle types are driving the **sales and revenue growth*.