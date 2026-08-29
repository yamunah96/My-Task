import pandas as pd

# read csv file
df= pd.read_csv("products.csv")
df.head()

# check the number of rows and columns
df.shape

# summary about data
df.info()

# statstical info about column contain numerical values
df.describe()

# checking is any missing values
df.isnull().sum()

#checking duplicated values
df.duplicated().sum()

# Find total products.
print(df.shape[0])

# Find unique categories.
print(df['category'].unique())

# Count products category-wise.
df['category'].value_counts()

# Find average price.
print("The average price is: ",df['price'].mean())

# Find highest-priced product.
print(df[df['price'] == df['price'].max()][['product_name','price']])

#second method to Find highest-priced product.
product=df.loc[df['price'].idxmax()]
print("Product:", product['product_name'])
print("Price:", product['price'])

# Find lowest-priced product.
print(df[df['price'] == df['price'].min()][['product_name','price']].values)

#second method to Find lowest-priced product.
product=df.loc[df['price'].idxmin()]
print("Product:", product['product_name'])
print("Price:", product['price'])

# Find products priced above ₹50,000.
df[df['price']>50000][['product_name','price']]

# Find products with rating greater than 4.
df[df['rating']>4][['product_name','rating']]

# Sort products by price.
df.sort_values(by='price',ignore_index=True)

# Sort products by rating.
df.sort_values(by='rating',ignore_index=True)

# Find products with stock below 10.
df[df['stock']<10]

# Create discount_amount.
df['discount_amount']= df['price']*(df['discount']/100)

df.head(5)

# Create final_price.
df['final_price']=df['price']-df['discount_amount']

df.head(5)

# Find average price by category.
category_avg_price= df.groupby('category')['price'].mean().round(2)
print(category_avg_price)

# Find average rating by brand.
brand_avg_rating= df.groupby('brand')['rating'].mean().round(2)
print(brand_avg_rating)

# Find maximum product price category-wise.
maximum_product_price_category= df.groupby('category')['price'].max()
print(maximum_product_price_category)

# Export final data.
df.to_csv("final_product_data.csv",index=True)