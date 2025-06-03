# Brazilian E-Commerce Data Analysis Portfolio

## Project Overview
This project analyzes the [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) to uncover insights into customer behavior, order trends, and product performance. The goal is to demonstrate data analysis skills using Python, including data cleaning, exploratory data analysis (EDA), and visualization.

## Repository Structure
- `ecommerce_analysis.py`: Main Python script for loading, cleaning, and analyzing the dataset.
- `*.csv`: Dataset files from the Olist Brazilian E-Commerce dataset.
- `order_trends.png`: Visualization of monthly order trends.
- `top_categories.png`: Visualization of top product categories by revenue.
- `state_orders.png`: Visualization of top states by order count.

## Requirements
- Python 3.8+
- Libraries: `pandas`, `matplotlib`, `seaborn`
- Install dependencies using:
  ```bash
  pip install pandas matplotlib seaborn
  ```

## Analysis Details
The project includes the following analyses:
1. **Order Trends Over Time**: Tracks the number of orders per month to identify seasonal patterns.
2. **Top Product Categories by Revenue**: Identifies the highest revenue-generating product categories.
3. **Customer Segmentation by State**: Analyzes order distribution across Brazilian states.

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/peixotojeff/Brazilian-E-Commerce-Public-Dataset-by-Olist.git
   ```
2. Ensure the CSV files are in the repository root.
3. Run the analysis script:
   ```bash
   python ecommerce_analysis.py
   ```
4. View generated visualizations (`*.png`) in the repository.

## Visualizations
- **Monthly Order Trends**: Line plot showing order volume over time.
- **Top Categories**: Bar plot of the top 10 product categories by revenue.
- **State Orders**: Bar plot of the top 10 states by order count.

## Future Improvements
- Add customer purchase frequency analysis.
- Incorporate delivery time analysis.
- Build an interactive dashboard using Streamlit or Plotly.

## Author
Jeff Peixoto