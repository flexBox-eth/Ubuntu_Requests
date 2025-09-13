# ------------------------------
# IMPORT LIBRARIES
# ------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# ------------------------------
# TASK 1: LOAD AND EXPLORE DATA
# ------------------------------

print("Task 1: Load and Explore Dataset\n")

try:
    # Load Iris dataset
    iris_data = load_iris()
    df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
    df['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)
except Exception as e:
    print(f"Error loading dataset: {e}")

# Inspect first rows
print("First 5 rows:\n", df.head())

# Dataset structure
print("\nDataset Info:")
print(df.info())

# Missing values
print("\nMissing values per column:\n", df.isnull().sum())

# Drop missing values if any
df = df.dropna()

# ------------------------------
# TASK 2: BASIC DATA ANALYSIS
# ------------------------------

print("\nTask 2: Basic Data Analysis\n")

# Summary statistics
print("Summary statistics:\n", df.describe())

# Group by species and compute mean of numerical columns
grouped = df.groupby('species').mean()
print("\nAverage measurements per species:\n", grouped)

# Observations (you can add more)
print("\nObservation: Setosa species generally has smaller petal and sepal measurements.")

# ------------------------------
# TASK 3: DATA VISUALIZATION
# ------------------------------

print("\nTask 3: Data Visualization\n")
sns.set(style="whitegrid")

# 1. Line chart (mock trend using cumulative sum)
df['sepal length (cm)'].cumsum().plot(kind='line', title='Cumulative Sepal Length Trend')
plt.xlabel('Sample Index')
plt.ylabel('Cumulative Sepal Length (cm)')
plt.show()

# 2. Bar chart (average petal length per species)
grouped['petal length (cm)'].plot(kind='bar', title='Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.show()

# 3. Histogram (distribution of sepal width)
df['sepal width (cm)'].plot(kind='hist', bins=10, title='Sepal Width Distribution')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter plot (sepal length vs petal length)
plt.scatter(df['sepal length (cm)'], df['petal length (cm)'], c=df['species'].cat.codes, cmap='viridis')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(iris_data.target_names)
plt.show()

print("\nAll visualizations created successfully.")
print("Insights can be added as markdown or comments.")
