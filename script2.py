with open("notes.txt") as f:
    lines = f.readlines()  # замініть на f.readlines()
    line_count = 0
    word_count = 0
    for line in lines:
        line_count += 1

    for line in lines:
        for word in line.split():
            word_count += 1





print(f"Кількість рядків: {line_count}")
print(f"Кількість слів: {word_count}")
