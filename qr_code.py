import qrcode

data = input("Enter the text or link: ")

img = qrcode.make(data)

img.save("qrcode.png")

print("QR code generated successfully!")