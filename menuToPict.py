from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import locale
jours = {
    'Monday': 'Lundi',
    'Tuesday': 'Mardi',
    'Wednesday': 'Mercredi',
    'Thursday': 'Jeudi',
    'Friday': 'Vendredi',
    'Saturday': 'Samedi',
    'Sunday': 'Dimanche'
}

mois = {
    'January': 'janvier',
    'February': 'février',
    'March': 'mars',
    'April': 'avril',
    'May': 'mai',
    'June': 'juin',
    'July': 'juillet',
    'August': 'août',
    'September': 'septembre',
    'October': 'octobre',
    'November': 'novembre',
    'December': 'décembre'
}



def makePict(menu, moment):
    image = Image.open("Const/Menu.png")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("Const/Allura.ttf", 50)
    text_color = (0,0,0)
    width, height = image.size


    #date
    locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
    date_actuelle = datetime.now()
    date_formatee = date_actuelle.strftime("%A %d %B") + f" : {moment}"
    for jour_anglais, jour_francais in jours.items():
        date_formatee = date_formatee.replace(jour_anglais, jour_francais)
    for mois_anglais, mois_francais in mois.items():
        date_formatee = date_formatee.replace(mois_anglais, mois_francais)
    text = date_formatee
    text_size = draw.textsize(text, font=font)
    text_width = text_size[0]
    x = (float(width) - float(text_width)) / 2
    y = 250
    draw.text((x, y), text, fill=text_color, font=font)



    font = ImageFont.truetype("Const/Allura.ttf", 36)
    #entrée
    text = menu["entree"]
    text_size = draw.textsize(text, font=font)
    text_width = text_size[0]
    x = (float(width) - float(text_width)) / 2
    y = 500
    draw.text((x, y), text, fill=text_color, font=font)

    #plat
    text = menu["plat"]
    text_size = draw.textsize(text, font=font)
    text_width = text_size[0]
    x = (float(width) - float(text_width)) / 2
    y = 675
    draw.text((x, y), text, fill=text_color, font=font)

    #+
    text = "+"
    text_size = draw.textsize(text, font=font)
    text_width = text_size[0]
    x = (float(width) - float(text_width)) / 2
    y = 725
    draw.text((x, y), text, fill=text_color, font=font)

    #condiment
    text = menu["condiment"]
    text_size = draw.textsize(text, font=font)
    text_width = text_size[0]
    x = (float(width) - float(text_width)) / 2
    y = 775
    draw.text((x, y), text, fill=text_color, font=font)

    #desser
    text = menu["dessert"]
    text_size = draw.textsize(text, font=font)
    text_width = text_size[0]
    x = (float(width) - float(text_width)) / 2
    y = 930
    draw.text((x, y), text, fill=text_color, font=font)

    image = image.convert("RGB")
    image.save("Temp/menu.jpg")
    image.close()
    return date_formatee