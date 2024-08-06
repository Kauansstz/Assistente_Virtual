import win32com.client as win32

outlook = win32.Dispatch("outlook.application")

# criar um email
email = outlook.CreateItem(0)
send_email = input("digite seu email: ")
email.To = send_email
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
