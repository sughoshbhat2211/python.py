!pip install qrcode[pil]

import qrcode
from IPython.display import display
import ipywidgets as widgets
from IPython.display import clear_output

# Input box
text_box = widgets.Text(
    value='https://www.google.com',
    description='Link:',
    layout=widgets.Layout(width='500px')
)

# Button
button = widgets.Button(
    description='Generate QR',
    button_style='success'
)

# Output area
output = widgets.Output()

# Function
def generate_qr(b):

    with output:

        clear_output()

        # Get input value
        data = text_box.value

        # Create QR
        qr = qrcode.QRCode(
            version=4,
            box_size=10,
            border=5
        )

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(
            fill_color="black",
            back_color="white"
        )

        img.save("website_qr.png")

        display(img)

# Button click event
button.on_click(generate_qr)

# Show UI
display(text_box)
display(button)
display(output)
