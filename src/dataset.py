# Import the pandas library
import pandas as pd

# Create a simple DataFrame with some sample data
data = {
    "Name": ["John", "Alice", "Bob", "Eve"],
    "Age": [23, 25, 22, 28],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
}

# Convert the dictionary into a pandas DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Basic Operations

# 1. Selecting a single column
print("\nNames column:")
print(df["Name"])

# 2. Selecting rows where age is greater than 23
print("\nRows where Age > 23:")
print(df[df["Age"] > 23])

# 3. Add a new column
df["Country"] = "USA"
print("\nDataFrame with new column 'Country':")
print(df)
