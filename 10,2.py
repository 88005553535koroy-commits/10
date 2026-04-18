from PIL import Image, ImageDraw, ImageFont

holidays = {
    "Новый год": "new_year.jpg",
    "8 марта": "march8.jpg",
    "23 февраля": "feb23.jpg",
    "День рождения": "birthday.jpg"
}

holiday = input("К какому празднику нужна открытка? ")
name = input("Кого поздравляем? ")

if holiday in holidays:
    img = Image.open(holidays[holiday])

    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arialbd.ttf", 50)  # arialbd - жирный
    except:
        try:
            font = ImageFont.truetype("Arial Bold.ttf", 50)
        except:
            font = ImageFont.load_default()


    text = f"{name}, поздравляю!"

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]

    x = (img.width - text_width) // 2
    draw.text((x, 50), text, fill=(255, 0, 0, 255), font=font)

    img.save('greeting_card.png')
    img.show()
    print("Открытка сохранена как 'greeting_card.png'")
else:
    print("Такого праздника нет в списке!")