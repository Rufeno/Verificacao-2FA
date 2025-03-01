import pyotp
import qrcode

# Dados simulados de login
usuarios = {"teste1": "senha123"}  # Dicionário com usuários e senhas

# Solicitar login do usuário
usuario = input("Usuário: ")
senha = input("Senha: ")  # Substituído getpass.getpass por input normal

if usuario in usuarios and usuarios[usuario] == senha:
    print("Login bem-sucedido! Agora, configure a autenticação de dois fatores.")
    
    # Gerar um segredo para o usuário
    secret = pyotp.random_base32()
    issuer_name = "teste"
    account_name = usuario
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
else:
    print("Usuário ou senha incorretos. Acesso negado.")
