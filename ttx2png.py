#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image, ImageFont, ImageDraw
import os
#получаем список со всеми шрифтами
path= "/home/gantzer/work/Fonts/"
allfonts = os.listdir(path)

def unicode_in_symbol(startrange, endrange): #преобразует unicode в символы, возвращает список символов
    letter = ""
    for i in range(startrange, endrange): #range берем номера символов +1 из таблице unicode
        letter = letter + chr(i)
    symbol = list(letter)
    return symbol
listsymbol = unicode_in_symbol(1040,1104) #русские буквы верхнего и нижнего регистра
listsymbol = listsymbol + unicode_in_symbol(1105,1106) #буква ё
listsymbol = listsymbol + unicode_in_symbol(1025,1026) #буква Ё
listsymbol = listsymbol + unicode_in_symbol(65,91) #анлийски буквы верхнего регистра
listsymbol = listsymbol + unicode_in_symbol(97,123) #анлийски буквы ниженого регистра
listsymbol = listsymbol + unicode_in_symbol(48,58) #цифры

for k in allfonts:
    os.chdir(path)
    print(k)
    try:
        font = ImageFont.truetype(k, 500, encoding="unic")
    except OSError:
<<<<<<< HEAD
        print('ошибка с файлом %s' % k)
        pathlog = "/home/gantzer/work/ttx2png/"
=======
        print('системная ошибка с файлом %s' % k)
        pathlog = "/home/gantzer/work/"
>>>>>>> df5d5691512ee42d59c5e3e4b7a477993750e3d7
        os.chdir(pathlog)
        log = open('log.txt', 'a+')
        log.write('системная ошибка с файлом %s' % k + '\n')
        log.close()
    else:
        path2= "/home/gantzer/work/png/%s" % k
        os.makedirs(path2, exist_ok=True)
        os.chdir(path2)
        for i in listsymbol:
            text_width, text_height = font.getsize(i)
            im = Image.new('RGB', (text_width + 200, text_height + 200), "white")
            draw = ImageDraw.Draw(im)
            draw.text((100, 100), i, 'black', font=font)
<<<<<<< HEAD
            im.save('%s.png' % i, 'PNG')
=======
            im.save('%s.png' % i, 'PNG')
>>>>>>> df5d5691512ee42d59c5e3e4b7a477993750e3d7
