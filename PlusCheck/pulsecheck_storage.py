import json

DATA_FILE = "mood_entries.json"

def load_entries():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("Error: JSON file is corrupted.")
        return []

    except FileNotFoundError:
        print("Error: JSON file not found.")
        return []

def save_entries(datas):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(datas, file, ensure_ascii=False, indent=2)


def validate_score(score):
    if 1<= score <= 5:
        return True
    return False
        
def calculate_average(entries):
    total = sum(entry["score"] for entry in entries)
    return total / len(entries)


entries = load_entries()     
        
new_entry = {
    "name": "فاطمه",
    "score": 9,
    "reason": "لاندا"
}


if validate_score(new_entry["score"]):
    entries.append(new_entry)
    save_entries(entries)
    print("Entry saved successfully.")
else:
    print("Invalid score!")
    
    
average = calculate_average(entries)
print(f"average score: {average: 1f}")