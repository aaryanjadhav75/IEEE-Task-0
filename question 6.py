import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("processed_student_performance.csv")

plt.figure(figsize=(10, 6))
plt.bar(df["Student"], df["Final_Score"], color="skyblue", edgecolor="black")
plt.title("Student Names vs Final Scores")
plt.xlabel("Student Name")
plt.ylabel("Final Score")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("final_scores.png")
plt.close()

plt.figure(figsize=(8, 5))
plt.scatter(
    df["Hours_Studied"],
    df["Final_Score"],
    color="darkorange",
    edgecolor="black",
)
plt.title("Hours Studied vs Final Score")
plt.xlabel("Hours Studied")
plt.ylabel("Final Score")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("study_vs_score.png")
plt.close()

plt.figure(figsize=(8, 5))
plt.hist(df["Final_Score"], bins=10, color="seagreen", edgecolor="black")
plt.title("Distribution of Final Scores")
plt.xlabel("Final Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("score_distribution.png")
plt.close()

plt.figure(figsize=(8, 5))
plt.scatter(
    df["Attendance"], df["Improvement"], color="purple", edgecolor="black"
)
plt.title("Attendance vs Score Improvement")
plt.xlabel("Attendance (%)")
plt.ylabel("Improvement (Final - Previous)")
plt.axhline(0, color="gray", linestyle="--", alpha=0.7)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("attendance_vs_improvement.png")
plt.close()