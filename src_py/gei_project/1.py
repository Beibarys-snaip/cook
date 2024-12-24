import json 
import os
save_file = "save.json"

def load_save():
    if os.path.exists(save_file):
        with open(save_file, "r") as file:
            return json.load(file)
    else:

        return {"user1": "user2", "level": 1, "score": 0}


def save_game(data):
    with open(save_file, "w") as file:
        json.dump(data, file, indent=4)

def update_save(level_increase=1, score_increase=100):
    data = load_save()
    data["level"] += level_increase
    data["score"] += score_increase
    save_game(data)
    print("Сохранение обновлено:", data)

current_save = load_save()
print("Текущие данные:", current_save)
update_save()