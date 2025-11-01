# Author: Sushma J
# Project: Colorado Motor Vehicle Sales Data Analysis (2018–2024)

# Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load Dataset
data = pd.read_csv("colorado_motor_vehicle_sales.csv", delim_whitespace=True)

print("✅ CSV Loaded Successfully!")
print("\nColumns Found:", data.columns.tolist())
print("\nPreview of Data:")
print(data.head())

# ------------------------------
# Data Cleaning
# ------------------------------
data.dropna(inplace=True)

# Ensure correct data types
data['Year'] = data['Year'].astype(int)
data['Units_Sold'] = pd.to_numeric(data['Units_Sold'], errors='coerce')
data['Revenue'] = pd.to_numeric(data['Revenue'], errors='coerce')
data['Average_Price'] = pd.to_numeric(data['Average_Price'], errors='coerce')

# ------------------------------
# 1️⃣ Total Sales Trend (2018–2024)
# ------------------------------
total_sales = data.groupby('Year')['Units_Sold'].sum().reset_index()

plt.figure(figsize=(8, 5))
sns.lineplot(x='Year', y='Units_Sold', data=total_sales, marker='o')
plt.title('Total Vehicle Units Sold Trend (2018–2024)')
plt.xlabel('Year')
plt.ylabel('Total Units Sold')
plt.grid(True)
plt.tight_layout()
plt.savefig('1_total_sales_trend.png')
plt.close()

# ------------------------------
# 2️⃣ Sales by Vehicle Type
# ------------------------------
vehicle_sales = data.groupby('Vehicle_Type')['Units_Sold'].sum().sort_values(ascending=False).reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(x='Vehicle_Type', y='Units_Sold', data=vehicle_sales, palette='magma')
plt.title('Units Sold by Vehicle Type')
plt.xlabel('Vehicle Type')
plt.ylabel('Units Sold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('2_sales_by_vehicle_type.png')
plt.close()

# ------------------------------
# 3️⃣ Average Price Trend
# ------------------------------
avg_price = data.groupby('Year')['Average_Price'].mean().reset_index()

plt.figure(figsize=(8, 5))
sns.lineplot(x='Year', y='Average_Price', data=avg_price, marker='o', color='green')
plt.title('Average Vehicle Price Trend (2018–2024)')
plt.xlabel('Year')
plt.ylabel('Average Price (USD)')
plt.grid(True)
plt.tight_layout()
plt.savefig('3_average_price_trend.png')
plt.close()

# ------------------------------
# 4️⃣ Top Manufacturers by Revenue
# ------------------------------
manufacturer_revenue = data.groupby('Manufacturer')['Revenue'].sum().sort_values(ascending=False).head(10).reset_index()

plt.figure(figsize=(9, 6))
sns.barplot(x='Manufacturer', y='Revenue', data=manufacturer_revenue, palette='coolwarm')
plt.title('Top 10 Manufacturers by Total Revenue (2018–2024)')
plt.xlabel('Manufacturer')
plt.ylabel('Total Revenue (USD)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('4_top_manufacturers_revenue.png')
plt.close()

# ------------------------------
# 5️⃣ Units Sold by Brand
# ------------------------------
data['Units_Sold'] = pd.to_numeric(data['Units_Sold'], errors='coerce')

brand_sales = (
    data.groupby('Manufacturer')['Units_Sold']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

print("\n✅ Checking brand_sales DataFrame:")
print(brand_sales.head())

plt.figure(figsize=(9, 6))
sns.barplot(x='Manufacturer', y='Units_Sold', data=brand_sales, palette='viridis')
plt.title('Top 10 Manufacturers by Units Sold (2018–2024)')
plt.xlabel('Manufacturer')
plt.ylabel('Units Sold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('5_units_sold_by_brand.png')
plt.close()

# ------------------------------
# ✅ Summary Output
# ------------------------------
print("\n✅ Analysis Complete! The following graphs have been saved:")
print("1_total_sales_trend.png")
print("2_sales_by_vehicle_type.png")
print("3_average_price_trend.png")
print("4_top_manufacturers_revenue.png")
print("5_units_sold_by_brand.png")