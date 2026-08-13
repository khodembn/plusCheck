datas = [
    {"name": "ali", "score": 4, "reason": "alpha"},
    {"name": "ahamd", "score": 2, "reason": "beta"},
    {"name": "reza", "score": 1, "reason": "delta"},
    {"name": "mobina", "score": 3, "reason": "Gamma"},
    {"name": "armin", "score": 5, "reason": "Epsilon"},
]


def get_mood_status(score: int):
    if score == 5:
        status = "excellent"
    elif score == 4:
        status = "good"
    elif score == 3:
        status = "normal"
    elif score < 3:
        status = "needs attention"

    return status


needs_attentions = 0
total_score = 0

for data in datas:
    user_status = get_mood_status(data["score"])
    data["status"] = user_status

    total_score += data["score"]

    if user_status == "needs attention":
        needs_attentions += 1

    print(data["name"], user_status)




total_user = len(datas)
average_mood = total_score / total_user


if average_mood >= 4:
    class_status = "Excellent"
elif average_mood >= 3:
    class_status = "Good"
elif average_mood >= 2:
    class_status = "Normal"
else:
    class_status = "Needs Attention"


print("\n--- team Report ---")
print("Total people:", total_user)
print("Average mood:", average_mood)
print("Needs attention:", needs_attentions)
print("team status:", class_status)