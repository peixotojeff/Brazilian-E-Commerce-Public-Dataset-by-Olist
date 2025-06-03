import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set plot style
sns.set(style="whitegrid")

# Load datasets
orders = pd.read_csv('olist_orders_dataset.csv')
order_items = pd.read_csv('olist_order_items_dataset.csv')
products = pd.read_csv('olist_products_dataset.csv')
customers = pd.read_csv('olist_customers_dataset.csv')
categories = pd.read_csv('product_category_name_translation.csv')

# Merge datasets
data = orders.merge(order_items, on='order_id', how='left')
data = data.merge(products, on='product_id', how='left')
data = data.merge(customers, on='customer_id', how='left')
data = data.merge(categories, on='product_category_name', how='left')

# Data cleaning
data['order_purchase_timestamp'] = pd.to_datetime(data['order_purchase_timestamp'])
data = data.dropna(subset=['order_purchase_timestamp', 'price', 'product_category_name_english'])

# Assuming 'data' is your DataFrame loaded earlier in the script
# Analysis 1: Order Trends Over Time
data['order_year_month'] = data['order_purchase_timestamp'].dt.to_period('M')
order_trends = data.groupby('order_year_month').size().reset_index(name='order_count')

# Convert Period objects to strings
order_trends['order_year_month'] = order_trends['order_year_month'].astype(str)

# Create the line plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=order_trends, x='order_year_month', y='order_count')
plt.title('Monthly Order Trends')
plt.xlabel('Year-Month')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.savefig('order_trends.png')
plt.close()

# Analysis 2: Top Product Categories by Revenue
category_revenue = data.groupby('product_category_name_english')['price'].sum().reset_index()
category_revenue = category_revenue.sort_values(by='price', ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(data=category_revenue, x='price', y='product_category_name_english')
plt.title('Top 10 Product Categories by Revenue')
plt.xlabel('Total Revenue (BRL)')
plt.ylabel('Category')
plt.tight_layout()
plt.savefig('top_categories.png')
plt.close()

# Analysis 3: Customer Segmentation by State
state_orders = data.groupby('customer_state').size().reset_index(name='order_count')
state_orders = state_orders.sort_values(by='order_count', ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(data=state_orders, x='order_count', y='customer_state')
plt.title('Top 10 States by Order Count')
plt.xlabel('Number of Orders')
plt.ylabel('State')
plt.tight_layout()
plt.savefig('state_orders.png')
plt.close()

print("Analysis complete. Visualizations saved as PNG files.")