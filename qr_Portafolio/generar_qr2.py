import qrcode

# URL de tu portafolio
url = "https://emmaderac.github.io/portfolio"  # Cambia por tu enlace real

# Generar QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Guardar imagen
img = qr.make_image(fill_color="black", back_color="white")
img.save("portafolio_qr.png")

print("✅ QR generado como 'portafolio_qr.png'")
