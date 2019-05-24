from PIL import Image, ImageDraw, ImageFont
import random


def new_img(width, height, color='white'):
    img = Image.new('RGB', (width, height), color=color)
    img.save("new.png", "PNG")


def random_str():
    return chr(random.randint(65, 90))


def random_color():
    tup = ()
    for i in range(3):
        n = random.randint(64, 255)
        tup1 = (n,)
        tup += tup1
    return tup


def draw_img():
    s = random_str()
    img = Image.open('new.png')
    img_size = img.size
    # 必须创建一个draw对象
    draw = ImageDraw.Draw(img)
    font_size = 40
    fnt = ImageFont.truetype('arial.ttf', font_size)
    fnt_size = fnt.getsize(s)
    # 随机颜色的字符
    x = (img_size[0] - fnt_size[0]) / 4
    for i in range(4):
        y = random.randint(0, img_size[1] - fnt_size[1])
        draw.text((x, y), random_str(), random_color(), font=fnt)
        x += font_size
    # 随机噪点
    for i in range(100):
        img_x = random.randint(0, img_size[0])
        img_y = random.randint(0, img_size[1])
        draw.point((img_x, img_y), fill=random_color())

    img.save('new.png', 'PNG')


if __name__ == '__main__':
    new_img(200, 50)
    draw_img()
