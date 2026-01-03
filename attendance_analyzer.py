# College Attendance Analyzer
# Author: Pritish Pratap Singh
# Purpose: Analyze student attendance and generate reports

import pandas as pd

# Load data
data = pd.read_csv("attendance.csv")

# Fill missing values
data.fillna(0, inplace=True)

# Calculate average attendance
data["Average"] = data.iloc[:, 1:].mean(axis=1)

# Identify defaulters (<75%)
defaulters = data[data["Average"] < 75]

# Save reports
data.to_csv("full_report.csv", index=False)
defaulters.to_csv("defaulters.csv", index=False)

# Display top performers
top = data.sort_values(by="Average", ascending=False).head(3)
top.to_csv("top_performers.csv", index=False)
print("Top performers saved.")


print("Reports generated successfully.")
