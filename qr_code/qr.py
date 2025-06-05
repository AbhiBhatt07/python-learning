# import qr library
import qrcode
import qrcode.constants

data = input("Enter any text or URL for get QR code.")

qr = qrcode.QRCode(
    version=1, 
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color = "black", back_color="white")

file_name = 'portfolio_QR.png'
img.save(file_name)

print(f"QR Code saved successfully as '{file_name}'!")