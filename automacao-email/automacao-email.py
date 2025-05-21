import pyautogui as py
import time
import pyperclip

time.sleep(2)
py.click()
py.PAUSE = 1

# Com o navegador utilizado para a automação com o email ja logado, cole aqui a url dele (estar com o navegador aberto!)
link = 'https://mail.google.com/mail/u/0/#inbox'
pyperclip.copy(link)

py.hotkey("ctrl", "n")

py.hotkey("ctrl", "v")

py.press("enter")

time.sleep(2)
# Aqui a localização do mouse para clilcar no botão Escrever (medidas para um monitor 1920x1080 com navegaror full screen e 90%)
py.click(59, 177)

# Aqui o destinatario
email = "teste@gmail.com"
pyperclip.copy(email)
py.hotkey("ctrl", "v")
py.press("tab")

# Aqui é o campo Assunto
py.write("teste Assunto")
py.press("tab")

# Aqui é o campo de texto
py.write("teste Campo de Texto")
py.hotkey("ctrl", "enter")
