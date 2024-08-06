import win32com.client as win32


class RecebimentoEmail:
    def __init__(self, email):
        self.email = email

    def envio_email(self):
        outlook = win32.Dispatch("outlook.application")

        # criar um email
        email = outlook.CreateItem(0)
        email.To = self.email
        email.Subject = "Confirmação de email"
        email.HTMLBody = f"""
        <h1>Confirmação de E-mail</h1>

        <p>Se recebeu esse email, quer dizer que se email foi cadastrado no sistema com sucesso</p>
        <p>Tenha um ótimo Dia/Noite</p>

        <p>Para feedback sobre o email</p>
        <p>Entre em contato: (48)998345181</p>
        """
        email.Send()
        print("Email Enviado")
