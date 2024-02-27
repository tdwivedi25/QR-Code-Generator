import qrcode as qr

link = input("Enter the link for which you want to generate a qr code: ")
name = input("Enter the name for the qr code: ")
img = qr.make(link)
img.save(name + ".png")

