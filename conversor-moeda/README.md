<h1><strong><em>Conversor de Real para Dólar</em></strong></h1>

## 📕 Sobre

- Este é um projeto iniciante desenvolvido em um WorkShop de 2 dias com foco em Automação Web. 
- O Script automatiza a tarefa de conversão de moedas a partir do site do Banco Central, insere o valor e extrai o valor convertido na outra moeda.

## 🔁 O que o Script Faz

1. Acessa o site do Banco Central;<br>
2. Insere automaticamente o valor desejado em reais;<br>
3. Clica no botão de conversão;<br>
4. Lê o valor convertido em dólar da tela;<br>
5. Copia o valor automaticamente e exibe no terminal.<br>

## 🔨 Ferramentas

- [Python](https://www.python.org/)
- [Selenium](https://www.selenium.dev/)

##  🔹 Como Utilizar

O site utilizado possui como característica a vírgula de forma fixa **00,00** ou seja, para convertermos **10 reais** precisamos inserir **1000** = **10,00**, como alterar para o valor desejado?<br>
Na linha:<br>
<pre>
    campo_valor.send_keys("1000")
</pre>
Troque o valor '1000' dentro do: '(" ")' para o valor que desejar.<br> 
Sendo assim:<br>
- 1000 = R$10,00;
- 100 = R$01,00;
- 10 = R$00,10;
- 1 = R$00,01

## 📚 Aprendizados

Este projeto foi meu primeiro contato com automação web, sendo utilizado Python e Selenium, aprendi sobre:

- Extração de dados diretamente da interface de uma página
- Interação automatizada com sites
- WebDriver
- Localização de Elementos pelo DevTools com **CSS_Selector** e **XPath**<br>

---

***Desenvolvido por João Vitor Bolognezi durante o 1º semestre do curso de Engenharia de Software.***

