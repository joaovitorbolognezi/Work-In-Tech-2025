from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

def conversao_dollar():
    navegador = webdriver.Chrome()
    navegador.get('https://www.bcb.gov.br/conversao')
    print("Conversao de R$10,00 para dollar!")

    try:
        wait = WebDriverWait(navegador, 10)

        campo_valor = wait.until(EC.presence_of_element_located((By.NAME, "valorBRL")))
        campo_valor.send_keys("1000")
        time.sleep(2)

        botoes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".btn.btn-primary.w-100")))
        botoes[1].click() 
        time.sleep(2)

        resultado = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.card-body")))
        texto = resultado.text

        match = re.search(r"Resultado da conversão:\s*([\d,]+)", texto)
        if match:
            valor_convertido = match.group(1)
            print(f"R$10,00 equivalem a ${valor_convertido}")
        else:
            print("Nao foi possivel extrair o valor convertido.")

    except Exception as e:
        print(f"Erro: {e}")

    navegador.quit()

if __name__ == "__main__":
    conversao_dollar()
