import time
from PIL import ImageDraw, Image, ImageFont
from datetime import datetime, timedelta

FONT_SIZE = 450
TEXT_Y_POSITION = 600
TEXT_X_POSITION = 400
Tashkent_UTC = 5 #укажите ваш часовой пояс 

def convert_time_to_string(dt):
    dt += timedelta(hours=Tashkent_UTC)
    return f"{dt.hour}:{dt.minute:02}"

def change_img():
    start_time = datetime.utcnow()
    text = convert_time_to_string(start_time)
    row = Image.new('RGBA', (800, 800), "black")# Цвет фона black,white тд
    parsed = ImageDraw.Draw(row)
    font = ImageFont.truetype("HEADPLANE.ttf", FONT_SIZE)#стиль шрифта
    font2 = ImageFont.truetype("HEADPLANE.ttf", 100)
    font3 = ImageFont.truetype("HEADPLANE.ttf", 100)
    parsed.text((int(row.size[0]*0.07), int(row.size[1]*0.22)), f'{text}', 
                 align="center", color="GREEN", font=font, fill=(239,185,13))
    parsed.text((210, 550),'Tashkent time', # подтекст
                 align="center", font=font2, fill=(239,185,13))
    parsed.text((180, 650),'design by ENiKEN', # подтекст
                 align="center", font=font3, fill=(239,185,13))
    row.save(f'time.png', "PNG")

if __name__ == '__main__':
    change_img()
