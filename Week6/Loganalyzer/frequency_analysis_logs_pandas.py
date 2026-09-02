
"""frequency analysis_logs_pandas"""

# Load the log information into Pandas and perform frequency analysis.
import pandas as pd

with open("application.log") as f:
  data_file= f.readlines()

df= pd.DataFrame(data_file,columns=['log'])
df.head()

# frequency analysis
# count of info occurrences
info_occurrences=0
warning_occurrences=0
error_occurrences=0

for line in df.values:
  if "INFO" in line[0]:
      info_occurrences+=1
  if "ERROR" in line[0]:
       error_occurrences+=1
  if "WARNING" in line[0]:
      warning_occurrences+=1

print(f"Count of info occurrence: {info_occurrences}")
print(f"Count of error occurrence: {error_occurrences}")
print(f"Count of warning occurrence: {warning_occurrences}")

# second method
info_count = df["log"].str.contains("INFO").sum()
error_count = df["log"].str.contains("ERROR").sum()
warning_count = df["log"].str.contains("WARNING").sum()

print("INFO:", info_count)
print("ERROR:", error_count)
print("WARNING:", warning_count)

# log level counts
df["log_level"] = df["log"].str.split("|").str[1].str.strip()

df["log_level"].value_counts()

# INFO / ERROR / WARNING percentage
# normalize Return proportions rather than frequencies.
df["log_level"].value_counts(normalize=True).mul(100).round(2)

df['module']= df['log'].str.split("|").str[2]
df['module'].value_counts()

pd.crosstab(
    df["module"],
    df["log_level"],
    normalize="index"
).mul(100).round(2)

