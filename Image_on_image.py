import sys
from PIL import Image
from PIL import ImageOps

def extract_image(from_image, s=4):
    data = Image.open(from_image)
    for x in range(data.size[0]):
        for y in range(data.size[1]):
            p = data.getpixel((x,y))
            red   = (p[0] % s) * 255 / s
            green = (p[1] % s) * 255 / s
            blue  = (p[2] % s) * 255 / s
            data.putpixel((x, y), (red, green, blue))
    return data

def hide_image(public_img, secret_img, s=4):
    data = Image.open(public_img)
    key = ImageOps.autocontrast(Image.open(secret_img).resize(data.size))
    for x in range(data.size[0]):
        for y in range(data.size[1]):
            p = data.getpixel((x,y))
            q = key.getpixel((x,y))
            red   = p[0] - (p[0] % s) + (s * q[0] / 255)
            green = p[1] - (p[1] % s) + (s * q[1] / 255)
            blue  = p[2] - (p[2] % s) + (s * q[2] / 255)
            data.putpixel((x, y), (red, green, blue))
    return data

if __name__ =="__main__":
    
    hide_image("Emma.jpg", "Desitakes1.jpg").save("hidden.png")
    print "successfully hide the image"

    extract_image("hidden.png").save("extracted.png");
    print "image saved as extracted.png";
