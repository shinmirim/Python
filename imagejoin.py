from turtle import width
from PIL import Image, ImageFilter
from numpy import imag

image = Image.open('image.jpg')




image_resize=image.resize((200,200))
#image_resize.show()
image.save("image_resize.jpg")

#회전
image_rotated = image.rotate(45,expand=1)
#image_rotated.show()
image.save("image_rotated.jpg")


#블러처리
image_blur= image.filter(ImageFilter.GaussianBlur(5))
#image_blur.show()
image.save("image_blur.jpg")


result = Image.new("RGB",(1800, 1800))

result.paste(im=image, box=(0, 0))

result.paste(im=image_resize, box=(1000, 500))

result.paste(im=image_rotated, box=(0, 1000))
result.paste(im=image_blur, box=(1000, 1000))

result.show()