# from PIL import Image,ImageFilter

# im = Image.open('123.png')

# w,h = im.size

# print('Original image size: %sx%s' %(w,h))

# im.thumbnail((w//2,h//2))

# print('Resize image to: %sx%s' % (w//2, h//2))

# im.save('thumbail.jpg','jpeg')

# im2 = im.filter(ImageFilter.BLUR)

# im2.save('blur.jpg','jpeg')

# from PIL import Image,ImageDraw,ImageFont,ImageFilter

# import random

# def rndChar():
#     return chr(random.randint(65,90))

# # 随机颜色1:
# def rndColor():
#     return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# # 随机颜色2:
# def rndColor2():
#     return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# # 240 x 60:
# width = 60 * 4
# height = 60
# image = Image.new('RGB', (width, height), (255, 255, 255))
# # 创建Font对象:
# font = ImageFont.truetype('Arial.ttf', 36)

# # 创建Draw对象:
# draw = ImageDraw.Draw(image)

# # 填充每个像素:
# for x in range(width):
#     for y in range(height):
#         draw.point((x, y), fill=rndColor())

# # 输出文字:
# for t in range(4):
#     draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# # 模糊:
# image = image.filter(ImageFilter.BLUR)
# image.save('code.jpg', 'jpeg')

# import requests

# # r = requests.get('https://www.douban.com/',params={'q':'python','cat':'1001'})
# # print(r.url,r.content)

# r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(r.json())
import chardet
print(chardet.detect(b'Hello,world!'))

