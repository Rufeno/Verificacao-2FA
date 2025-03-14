# Autenticação de Dois Fatores (2FA) com PyOTP e QR Code

Este projeto implementa um sistema de **Autenticação de Dois Fatores (2FA)** utilizando **PyOTP** para gerar códigos de verificação baseados no tempo (**TOTP**) e **QRCode** para facilitar a configuração em aplicativos autenticadores como Google Authenticator ou Authy.

## Tecnologias Utilizadas
- **Python 3**
- **PyOTP** (Geração e verificação de códigos OTP)
- **QRCode** (Geração do QR Code para facilitar a configuração do OTP)

## Como Funciona
O programa realiza a autenticação em duas etapas:
1. **Login inicial:** O usuário insere seu nome e senha.
2. **Configuração do 2FA:** Se o login for bem-sucedido, o sistema gera um segredo único e cria um **QR Code** com a URL do OTP.
3. **Validação do código:** O usuário escaneia o QR Code em um aplicativo autenticador e insere o código gerado para verificação.

## Estrutura do Código

### 1. Dicionário de Usuários
```python
usuarios = {"teste1": "senha123"}  # Dicionário com usuários e senhas
```
- Simula um banco de dados, armazenando usuários e senhas.

### 2. Solicitação de Login
```python
usuario = input("Usuário: ")
senha = input("Senha: ")
```
- Solicita o nome de usuário e senha para autenticação.

### 3. Geração do Segredo e QR Code
```python
secret = pyotp.random_base32()
issuer_name = "teste"
account_name = usuario
uri = pyotp.totp.TOTP(secret).provisioning_uri(name=account_name, issuer_name=issuer_name)
```
- **pyotp.random_base32()**: Gera um segredo único para cada usuário.
- **provisioning_uri()**: Cria uma URI OTP, compatível com aplicativos autenticadores.

```python
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
```
- Gera um **QR Code** com a URI OTP e salva a imagem como **qrcode.png**.

### 4. Verificação do Código OTP
```python
def verificar_codigo(secret, codigo_usuario):
    totp = pyotp.TOTP(secret)
    return totp.verify(codigo_usuario)
```
- **pyotp.TOTP(secret)**: Inicializa o gerador OTP baseado no segredo fornecido.
- **verify(codigo_usuario)**: Compara o código inserido pelo usuário com o código OTP gerado no momento.

```python
codigo_usuario = input("Digite o código gerado pelo aplicativo autenticador: ")
if verificar_codigo(secret, codigo_usuario):
    print("Código válido! Autenticação bem-sucedida.")
else:
    print("Código inválido. Tente novamente.")
```
- Solicita ao usuário que digite o código gerado pelo aplicativo autenticador.
- Verifica se o código é válido e exibe a mensagem correspondente.

## Como Executar o Projeto
### 1. Instale as Dependências
Certifique-se de ter o Python 3 instalado e execute:
```sh
pip install pyotp qrcode[pil]
```

### 2. Execute o Código
```sh
python nome_do_arquivo.py
```

### 3. Siga o Fluxo:
1. Insira o nome de usuário e senha.
2. Escaneie o QR Code gerado usando um autenticador como Google Authenticator ou Authy.
3. Insira o código gerado no autenticador para verificar a autenticação.

## Melhorias Futuras
- Armazenamento do segredo OTP em um banco de dados.
- Implementação de uma interface gráfica (GUI) para facilitar o uso.
- Integração com um backend para uso em aplicações web.

---
