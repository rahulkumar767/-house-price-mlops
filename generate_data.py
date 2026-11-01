
import pandas as pd
import numpy as np
import os

# Generate 200 house records
np.random.seed(42)

n = 200

area = np.random.randint(500, 4000, n)
bedrooms = np.random.randint(1, 6, n)
bathrooms = np.random.randint(1, 5, n)
age = np.random.randint(1, 31, n)

# Calculate house prices
price = (
    area * 2500
    + bedrooms * 300000
    + bathrooms * 200000
    - age * 50000
    + np.random.randint(-200000, 200000, n)
)

# Create dataset
data = {
    "area_sqft": area,
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "house_age": age,
    "price": price
}

df = pd.DataFrame(data)

# Create data folder
os.makedirs("data", exist_ok=True)

# Save CSV file
df.to_csv("data/house_prices.csv", index=False)

print("200 House Records Created Successfully!")
print(df.head())
print("\nDataset Shape:", df.shape)
