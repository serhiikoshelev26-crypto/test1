while True:
    try:
        week = input("Введіть усі значення темератури через кому: ").replace(",", " ").split()
        week1 = [int(w) for w in week]
    except ValueError :
        print("Помилка, спробуйте знову.")
    if len(week1) == 7 :
        break
    else :
        print("Введіть значення температури для кожного дня тижня.")
cels = [round((x - 32) * (5 / 9)) for x in week1]
days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Нд"]
wdict = {days[a] : cels[a] for a in range(7)}
j1 = "Холодно"
j2 = "Тепло"
j3 = "Спекотно"
j4 = "Дуже спекотно"
dicres = {days[a] : j1 if cels[a] < 10 else j2 if 10 <= cels[a] <= 28 else j3 if 28 < cels[a] < 36 else j4  for a in range(7)}
for a in range(7):
    print(f"{days[a]}: {dicres[days[a]]}, ({cels[a]}°C)")
mid = int(sum(cels) / 7)
cels1 = sorted(cels)
min = cels1[0]
max = cels1[-1]

print(f"Максимальна температура: {max}°C")
print(f"Мінімальна температура: {min}°C")
print(f"Середня температура: {mid}°C")
