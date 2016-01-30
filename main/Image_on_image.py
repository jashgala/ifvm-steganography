import sys
from PIL import Image
from PIL import ImageOps

def extract_image(from_image, s=8):
    data = Image.open(from_image)
    for x in range(data.size[0]):
        for y in range(data.size[1]):
            p = data.getpixel((x,y))
            red   = (p[0] % s) * 255 / s
            green = (p[1] % s) * 255 / s
            blue  = (p[2] % s) * 255 / s
            data.putpixel((x, y), (red, green, blue))
    return data

def hide_image(public_img, secret_img, s=8):
    data = public_img
    key = ImageOps.autocontrast(secret_img.resize(data.size))
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
    
    hide_image("Emma.jpg", "Desitakes_02_02.png").save("hidden.png")
    print "Successfully hid the image"

    extract_image("hidden.png").save("extracted4.png");
    print "Image saved as extracted.png";
