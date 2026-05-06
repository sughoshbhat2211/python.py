import qrcode
from matplotlib import pyplot as plt
from urllib.parse import quote

upi_id = "8660972945@ptsbi"
name = "Sughosh"
amount = "10000"

# Encode name properly
name = quote(name)

# Create UPI payment link
upi_link = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR"

print(upi_link)

# Generate QR code
img = qrcode.make(upi_link)

# Display QR
plt.imshow(img)
plt.axis("off")
plt.show()
