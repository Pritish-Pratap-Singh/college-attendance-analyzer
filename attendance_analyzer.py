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

print("Reports generated successfully.")
