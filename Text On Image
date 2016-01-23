from PIL import Image
import stepic

im=Image.open('I:/FYP/Lenna.png');
im1=stepic.encode(im,'Hello world')
im1.save('StegoLenna.jpg','JPEG')
im.show()
im1.show()

s=stepic.decode(im1)
data=s.decode()
print data
