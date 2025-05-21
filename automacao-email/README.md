<h1><strong><em>Automação Envio de Email</em></strong></h1>

## 📕 Sobre

- Projeto desenvolvido no primeiro dia de um WorkShop de Automação Web;
- O Script automatiza a tarefa de abrir o Gmail, escrever destinatário, assunto, corpo do texto e enviá-lo, atravez do controle de mouse e teclado<br>

## 🔁 O que o Script Faz

1. Abre o navegador no Gmail automaticamente;<br>
2. Navega até o botão "Escrever";<br>
3. Clica no botão e vai para os campos de envio de Email;<br>
4. Preenche destinatário, assunto e corpo do email;<br>
5. Envia o email.<br>

## 🔨 Ferramentas

- [Python](https://www.python.org/)
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
- [PyperClip](https://pypi.org/project/pyperclip/)<br>


##  🔹 Como Utilizar

1. Instale as bibliotecas:
<pre>
  pip install pyautogui pyperclip
</pre>

2. Execute o Script
<pre>
  python automacao_email.py
</pre><br>

⚠️ **Observações:**

**1. Tenha o navegador aberto no momento da execução do script.**

<br>**2. Mudar o campo de url de email:**
<pre>
  link = 'https://mail.google.com/mail/u/0/#inbox'
</pre>
- Caso tenha mais de uma conta no navagador, será necessario logar o email com a sua conta e pegar o URL da tela apos o login ser concluido.

<br>**3. Localização do Mouse**
<pre>
  py.click(59, 177)
</pre>
- Neste codigo foi utilizado estas posições (X,Y), entretanto pode variar sendo necessario executar o código abaixo com o mouse posicionado sobre o botão de "Escrever":<br>
<pre>
  import pyautogui
  x, y = pyautogui.position()
  print(f"Posiçao do mouse: X={x}, Y={y}")
</pre>
- Com isso será retornado a posição X e Y que voce deverá subsitituir em suas devidas posições respectivamente:
<pre>
  py.click(X, Y)
</pre>

<br>**4. Mudar o campo de destinatário:**
<pre>
  email = "teste@gmail.com"
</pre>
- No lugar de 'teste@gmail.com' escreva o email do destinatário.

<br>**5. Mudar campo de Assunto:**
<pre>
  py.write("teste Assunto")
</pre>
- Substitua 'teste Asunto' pelo texto que voce deseja que apareça no campo Assunto.

<br>**6. Mudar corpo do Email:**
<pre>
  py.write("teste Campo de Texto")
</pre>

- Substitua 'teste Campo de Texto' pelo texto que voce deseja que apareça no corpo do Email.<br>


## <br>📚 Aprendizados

Este projeto foi meu primeiro contato com automação desktop, sendo utilizado Python, PyAutoGui, PyperClip. Aprendi sobre:

- Manipulação de texto com PyperClip;
- Controle programático do mouse e teclado;
- Uso de temporizadores, cliques, pressionamento de teclas e movimentação do cursor com PyAutoGUI.<br>

---<br>

***Desenvolvido por João Vitor Bolognezi durante o 1º semestre do curso de Engenharia de Software.***
