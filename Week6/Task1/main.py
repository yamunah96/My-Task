import pandas as pd
df= pd.read_csv("students.csv")
df

df.head(5)

df.tail(5)

df.shape

df.columns

df.dtypes

df.info()

df.describe()

df.isnull().sum()

cols=['age','python_marks','sql_marks','pandas_marks','attendance']
df[cols]= df[cols].fillna(df[cols].mean())

df['city']=df['city'].fillna("None")
df['name']=df['name'].fillna("None")

df.isnull().sum()

df.duplicated().sum()

df.drop_duplicates(inplace=True)

df.duplicated().sum()

print("Average Python Marks:", df['python_marks'].mean().round(2))

print("Average SQL Marks:", df['sql_marks'].mean().round(2))

print("Average Pandas Marks:", df['pandas_marks'].mean().round(2))

print("Maximum Python Marks:", df['python_marks'].max())
print("Minimum Python Marks:", df['python_marks'].min())

print("Maximum SQL Marks:", df['sql_marks'].max())
print("Minimum SQL Marks:", df['sql_marks'].min())

print("Maximum Pandas Marks:", df['pandas_marks'].max())
print("Minimum Pandas Marks:", df['pandas_marks'].min())

df.sort_values(by='python_marks',ascending=False)

df.sort_values(by='attendance',ascending=False)

# Filter students having Python marks greater than 80.
df[df['python_marks'] >80]

# Filter students having attendance greater than 75.
df[df['attendance']>75]

# Select only name, python_marks, and pandas_marks.
df[['name','python_marks','pandas_marks']]

# Add a new column called total_marks.
df['total_marks']=(df['pandas_marks']+df['python_marks']+df['sql_marks']).round(2)

df['average_marks']=(df['total_marks']/3).round(2)

df.to_csv("final.csv")

df['python_marks']= df['python_marks'].fillna(df['python_marks'].mean())

# filtering
df[df['pandas_marks'] == df['pandas_marks'].max()]['name']

df.rename(columns={"name":"student_name"})

df['city'].unique()

# Filter students having Python marks greater than 80.
# df[df['python_marks'] >80]
# (df['python_marks'] >80).sum()
df[df['python_marks'] >80][['name','python_marks']]

# Sort students by attendance.
df.sort_values(by='attendance',ascending=False)

df['python_marks'].mean().round(2)

# Add a new column called total_marks.
df['total_marks']=(df['pandas_marks']+df['python_marks']+df['sql_marks']).round(2)

df

# sql marks >90 and python marks>90
df[(df['sql_marks']>90) & (df['python_marks']>90)]

df.query("python_marks>90 and city=='Hubballi'")

