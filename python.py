import qrcode
from IPython.display import display

qr = qrcode.QRCode(
    version=4,
    box_size=10,
    border=5
)

qr.add_data("https://www.google.com")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("website_qr.png")

display(img)
