import qrcode
def qr_code(text,file_name):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 10,
        border = 4,

    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "#6aff9b",background_color = "black")
    img.save(file_name)

text = "https://github.com/dashboard"
file_name = "githubcode3.png"

qr_code(text,file_name)

