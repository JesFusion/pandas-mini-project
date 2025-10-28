import pandas as pd

# Dataset 1: Sales for Jan
sales_jan = {
    'product_id': ['P101', 'P102', 'P103'],
    'units_sold': [50, 80, 120]
}
df_jan = pd.DataFrame(sales_jan)

# Dataset 2: Sales for Feb
sales_feb = {
    'product_id': ['P101', 'P103', 'P104'],
    'units_sold': [55, 130, 20]
}
df_feb = pd.DataFrame(sales_feb)

# Dataset 3: Product Details
product_details = {
    'product_id': ['P101', 'P102', 'P103', 'P104'],
    'name': ['Widget A', 'Widget B', 'Gadget C', 'Gizmo D'],
    'category': ['Widgets', 'Widgets', 'Gadgets', 'Gizmos']
}
df_products = pd.DataFrame(product_details)



print(f'''
============================= Original  DataFrames =============================


============================= DataFrame for January =============================

{df_jan}

============================= DataFrame for February =============================

{df_feb}

============================= Product Details =============================

{df_products}
''')



all_sales = pd.concat([df_jan, df_feb], ignore_index = True)

print(f'''
============================= All Sales =============================
      
{all_sales}
''')

total_sales = all_sales.groupby("product_id")["units_sold"].sum()

final_report = pd.merge(
    total_sales, df_products,
    on = "product_id", how = "left"
)



print(f'''
============================= Total Sales =============================
      
{total_sales}


============================= Final report =============================

{final_report}
''')


