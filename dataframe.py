import pandas as pd

# Step 1: Load the CSV file
df = pd.read_csv("sample_data.csv")

# Step 2: Display statistics
print("Descriptive Statistics:\n", df.describe())

# Step 3: Get the number of rows and columns
rows, cols = df.shape
print(f"\nNumber of rows: {rows}")
print(f"Number of columns: {cols}")

# Step 4: Rename the columns
df.columns = ['height', 'weight']
print("\nRenamed columns:\n", df.head())

# Step 5: Add new column for height in meters (1 inch = 0.0254 meters)
df['height_in_meters'] = df['height'] * 0.0254
print("\nAdded 'height_in_meters' column:\n", df.head())

# Step 6: Filter rows where weight > 150 pounds
filtered_df = df[df['weight'] > 150]
print("\nFiltered data (weight > 150):\n", filtered_df)
