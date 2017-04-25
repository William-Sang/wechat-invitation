#!/usr/bin/env python
# encoding: utf-8
from utils import add_text_to_image
import yaml

# 加载配置文件
config =  yaml.load(open('config.yml'))

# 中心点坐标
x = config.get('x')
y = config.get('y')

# 字体文件位置
fonts_size = config.get('fonts_size')
fonts_path = config.get('fonts_path')
image_path = config.get('image_path')

# 解析颜色
color = config.get('color')
color_rgba = (color['r'], color['g'], color['b'], color['a'])

# 输出
out_dir = config.get('out_dir')

# 使用 text 拼接而成
with open('./names.txt') as f:
    for line in f:
        text = line.strip()
        out_path = out_dir + text + '.jpg'
        add_text_to_image((x,y), text, fonts_path, fonts_size, image_path, color_rgba, out_path)
        print ('输出文件成功: ' + out_path)