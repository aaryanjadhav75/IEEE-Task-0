import numpy as np


hours_studied = np.array([4.5, 6.0, 3.5, 8.0, 5.5])
attendance = np.array([90, 95, 80, 100, 85])
previous_scores = np.array([70, 82, 65, 88, 74])
final_scores = np.array([72, 85, 60, 92, 78])

print("--- Initial Arrays Created ---\n")


arrays = {
    "Hours studied": hours_studied,
    "Attendance": attendance,
    "Previous scores": previous_scores,
    "Final scores": final_scores
}

for name, arr in arrays.items():
    print(f"{name} -> Shape: {arr.shape}, Data Type: {arr.dtype}")


mean_final = np.mean(final_scores)
print(f"\n2. Mean final score: {mean_final}")


max_final = np.max(final_scores)
min_final = np.min(final_scores)
print(f"3. Maximum final score: {max_final}")
print(f"   Minimum final score: {min_final}")


std_final = np.std(final_scores)
print(f"4. Standard deviation of final scores: {std_final:.2f}")


updated_final_scores = final_scores + 5
print(f"5. Final scores after adding 5 bonus marks: {updated_final_scores}")


scored_at_least_75 = final_scores >= 75
print(f"6. Boolean array (scored >= 75): {scored_at_least_75}")


filtered_scores = final_scores[scored_at_least_75]
print(f"7. Scores greater than or equal to 75: {filtered_scores}")
