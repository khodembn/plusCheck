mood_scores = [5, 2, 4, 3, 1, 4, 5]

good = 0
normal = 0
needs_attentions = 0

for mood in mood_scores:
    
    if mood >= 4:
        good += 1
    elif mood ==3:
        normal += 1
    else:
        needs_attentions += 1    
        

print("Good:", good)
print("Normal:", normal)
print("Need Attentions:", needs_attentions)


moods_scores = [5, 4, 2, 1, 3, 5, 2]

total = 0 
low_mood = 0

for mood in moods_scores:
    total += mood
    
    if mood < 3:
        low_mood += 1
        
average =  total/len(moods_scores)

print(f"Team Mood Average: {average:.2f}")
print(f"Members with Low Mood: {low_mood}")

if low_mood >= 3:
    print("🚨 Warning! Several team members are not feeling well. Consider checking in with them.")
elif average < 3:
    print("😕 The team's overall mood is low and needs attention.")
elif average < 4:
    print("🙂 The team is in a balanced state.")
else:
    print("😄 The team is in a great mood. Keep up the good work!")
    
     
