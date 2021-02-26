import os

from PIL import Image   #PIL is the python image library which needs to be preinstalled before you can run this code
import random

img=input("\nEnter the name of the image you want the message to be encoded in, with the extension\n\n")

path=os.path.abspath(img)    #this gives the absolute path of the given file

image=Image.open(path)

text=input("\n\nEnter the message you wanna encode\n\n")
text_length=len(text)
print(text_length)
length = [text_length//255, text_length%255, 0]
print(length)
image.putpixel((0,0),tuple(length))
image.show()
image1=image.save("encrypted.jpg")

#Decryption getting length part
img2=input("\nEnter the name of the image you want the message to be decoded in, with the extension\n\n")

path2=os.path.abspath(img2)    #this gives the absolute path of the given file

image2=Image.open(path2)

raw=list(image2.getpixel((0,0)))
print(raw)
length_final = raw[0]*255 + raw[1]
print(length_final)