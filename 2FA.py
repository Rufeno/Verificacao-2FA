import pyotp
import qrcode

# Gerar um segredo para o usuário
secret = pyotp.random_base32()

# Criar um URI para o QR Code (usando o formato otpauth://)
issuer_name = "teste"
account_name = "teste1"
uri = pyotp.totp.TOTP(secret).provisioning_uri(name=account_name, issuer_name=issuer_name)

# Gerar o QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(uri)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")

print(f"Segredo: {secret}")
print("QR Code gerado e salvo como 'qrcode.png'.")

# Verificar o código inserido pelo usuário
def verificar_codigo(secret, codigo_usuario):
    totp = pyotp.TOTP(secret)
    return totp.verify(codigo_usuario)

# Exemplo de uso
codigo_usuario = input("Digite o código gerado pelo aplicativo autenticador: ")
if verificar_codigo(secret, codigo_usuario):
    print("Código válido! Autenticação bem-sucedida.")
else:
    print("Código inválido. Tente novamente.")