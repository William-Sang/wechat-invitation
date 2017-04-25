#!/usr/bin/env python
# encoding: utf-8

from PIL import Image,ImageDraw,ImageFont

# sample text and font
# text = u"商渭清"
# color_rgba = (135, 206, 255, 255)
# fonts_path = "./fonts/SourceHanSansSC-Bold.otf"
# fonts_size = 85
# image_path = './images/wtm-templete.JPG'
# x = 375
# y = 570
# out_path = 'xxxxxxx.jpg'

def add_text_to_image((x,y), text, fonts_path, fonts_size, image_path, color_rgba, out_path):


    font = ImageFont.truetype(fonts_path, fonts_size)
    # 获取实际占用大小
    text_width, text_height = font.getsize(text)

    image = Image.open(image_path)

    # 左上角其实位置
    x_start = x - text_width/2
    y_start = y - text_height/2

    draw = ImageDraw.Draw(image)
    draw.text((x_start, y_start), text, font=font, fill=color_rgba)

    image.save(out_path)