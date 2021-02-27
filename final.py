import os

from PIL import Image   #PIL is the python image library which needs to be preinstalled before you can run this code
import random

chr_ascii={}        #dictionary conatining characters as keys and ascii values as values
ascii_chr={}        #dictionary containing ascii values as keys and characters as values

for i in range(0,256):
    chr_ascii[chr(i)]=i
    ascii_chr[i]=chr(i)
    
def encrypt():
    img=input("\nEnter the name of the image you want the message to be encoded in, with the extension\n\n")

    path=os.path.abspath(img)    #this gives the absolute path of the given file

    image=Image.open(path)

    height=image.height
    width=image.width
    print(height,width)


    password=input("\n\nEnter security key\n\n")

    text=input("\n\nEnter the message you wanna encode\n\n")


    p=0
    j=0
    
    z=0
    text_length=len(text)
    image.putpixel((0,0),(text_length//255, text_length%255,0))
    random.seed(password)
    for i in range(text_length):
        x=random.randint(1,width)
        y=random.randint(1,height)
        RGB=image.getpixel((x,y))
        rgb_mutable=list(RGB)
        rgb_mutable[z]=chr_ascii[text[p]]^chr_ascii[password[j]]
        rgb_tuple=tuple(rgb_mutable)
        image.putpixel((x,y),rgb_tuple)
        
        
        z=(z+1)%3
        j=(j+1)%len(password)
        p+=1

        
    image.show()
    image1=image.save("encrypted.png")


    print("\n\nData hiding in image is successful\n\n")



def decrypt():
    img=input("\nEnter the name of the image you want the message to be encoded in, with the extension\n\n")

    path=os.path.abspath(img)    #this gives the absolute path of the given file

    image=Image.open(path)

    height=image.height
    width=image.width
    print(height,width)

    j1=0
    
    z1=0
    password=input("\n\nEnter your key\n\n")
    message=''
    raw=list(image.getpixel((0,0)))
    print(raw)
    length = raw[0]*255 + raw[1]
    print(length)
    
    random.seed(password)

    for i in range(length):
        x1=random.randint(1,width)
        y1=random.randint(1,height)
        RGB2=image.getpixel((x1,y1))
        coded=RGB2[z1]
        
        message+=ascii_chr[coded^chr_ascii[password[j1]]]
        
        z1=(z1+1)%3
        j1=(j1+1)%len(password)
        
    print("\n\nEncrypted text was\n\n",message)   

user = input("Type 'encrypt' if you want encryption \nType 'decrypt' if you want decryption\n" )

if user == 'encrypt':
    encrypt()
elif user == 'decrypt':
    decrypt()
else:
    print("Invalid entry")
