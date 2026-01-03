# College Attendance Analyzer
# Author: Pritish Pratap Singh
# Purpose: Analyze student attendance and generate reports

import matplotlib.pyplot as plt
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

plt.figure(figsize=(8,5))
plt.bar(data["Name"], data["Average"])
plt.axhline(70, linestyle='--')
plt.title("Average Attendance per Student")
plt.xlabel("Student")
plt.ylabel("Attendance %")
plt.tight_layout()
plt.savefig("student_average.png")
plt.close()

subject_avg = data.iloc[:,1:-1].mean()

plt.figure(figsize=(6,4))
subject_avg.plot(kind='bar')
plt.title("Subject Wise Average Attendance")
plt.ylabel("Attendance %")
plt.tight_layout()
plt.savefig("subject_average.png")
plt.close()

labels = ['Defaulters','Non-Defaulters']
sizes = [len(defaulters), len(data)-len(defaulters)]

plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Defaulter Distribution")
plt.savefig("defaulter_distribution.png")
plt.close()

