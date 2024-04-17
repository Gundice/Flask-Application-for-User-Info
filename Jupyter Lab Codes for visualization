import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file
csv_file = "C:\\Users\\Adeyemo Bolanle\\Desktop\\python codes\\user_data.csv"
df = pd.read_csv(csv_file)

# Clean the data by removing rows with missing values or zeros in the expense columns
df = df.dropna(subset=['age', 'gender', 'total_income'])
df = df[(df[['utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare']] != 0).all(axis=1)]

# Convert columns to appropriate data types
df['age'] = df['age'].astype(int)
df['total_income'] = df['total_income'].astype(float)

# Visualize ages with the highest income
plt.figure(figsize=(10, 6))
sns.barplot(x='age', y='total_income', data=df)
plt.title('Ages with the Highest Income')
plt.xlabel('Age')
plt.ylabel('Total Income')
plt.xticks(rotation=45)
plt.savefig("C:\\Users\\Adeyemo Bolanle\\Desktop\\python codes\\ages_highest_income.png")
plt.show()

# Melt the DataFrame to have a single column for spending categories
melted_df = pd.melt(df, id_vars=['gender'], value_vars=['utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare'],
                    var_name='spending_category', value_name='expense')

# Visualize gender distribution across spending categories
plt.figure(figsize=(10, 6))
sns.countplot(x='gender', hue='spending_category', data=melted_df)
plt.title('Gender Distribution Across Spending Categories')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(title='Spending Category')
plt.savefig("C:\\Users\\Adeyemo Bolanle\\Desktop\\python codes\\gender_distribution.png")
plt.show()
