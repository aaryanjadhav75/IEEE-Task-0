import pandas as pd

df = pd.read_csv("student_performance.csv")

print(df.head())

print(df.shape)

print(df.columns)

print(df.isnull().sum())

print(df["Final_Score"].mean())

print(df.loc[df["Final_Score"].idxmax()])

df["Improvement"] = df["Final_Score"] - df["Previous_Score"]

print(df[df["Attendance"] >= 80])

df = df.sort_values(by="Final_Score", ascending=False)

df.to_csv("processed_student_performance.csv", index=False)