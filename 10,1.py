from PIL import Image

holidays = {
    "Новый год": "new_year.jpg",
    "8 марта": "march8.jpg",
    "23 февраля": "feb23.jpg",
    "День рождения": "birthday.jpg",
    "День Победы": "victory.jpg"
}

holiday = input("К какому празднику нужна открытка? ")

if holiday in holidays:
    img = Image.open(holidays[holiday])
    img.show()
else:
    print("Такого праздника нет в списке!")