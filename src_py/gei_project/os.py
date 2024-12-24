import os

file_path = "data.txt"

def read_file():
    if not os.path.exists(file_path):
        print("Файл не найден!")
        return []
    with open(file_path, "r") as file:
        data = file.readlines()
    return [line.strip().split(", ") for line in data]

def write_file(data):
    with open(file_path, "w") as file:
        for player, score in data:
            file.write(f"{player}, {score}\n")

def add_player(name, score):
    data = read_file()
    data.append((name, score))
    write_file(data)
    print(f"Игрок {name} добавлен!")

def update_player(name, new_score):
    data = read_file()
    for i, (player, score) in enumerate(data):
        if player == name:
            data[i] = (name, new_score)
            write_file(data)
            print(f"Счет игрока {name} обновлен!")
            return
    print(f"Игрок {name} не найден!")

def delete_player(name):
    data = read_file()
    data = [entry for entry in data if entry[0] != name]
    write_file(data)
    print(f"Игрок {name} удален!")
add_player("Dave", 250)
update_player("Alice", 300)
delete_player("Charlie")
print(read_file())




