import qrcode
from PIL import Image

link = input("Enter the link for which you want to generate a qr code: ")
name = input("Enter the name for the qr code: ")
boxsize=int(input("Enter the size of the qrcode: "))
bordersize= int(input("Enter the size of the border: "))
fillcolor = input("Enter the color of the qrcode: ")
bg = input("Enter the background color for the qrcode: ")

qr = qrcode.QRCode(version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                    box_size= boxsize, border=bordersize)



qr.add_data(link)
qr.make(fit=True)
img=qr.make_image(fill_color = fillcolor, back_color = bg)
img.save(name+".png")

