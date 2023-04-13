""" Scraper de el precio del dolar
    Por medio de selenium extraemos el dato y lo imprimimos en pantalla"""

from selenium import webdriver #Importamos el Webdriver para trabajar con el navegador
from selenium.webdriver.common.by import By #By permite seleccionar a donde apuntamos en el html

driver=webdriver.Firefox()

# Navigate to Url
driver.get("https://dolarhoy.com/")

# Get element compra blue
blue_compra=driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]')
blue_compra=blue_compra.text #Elemento -> string
blue_compra=blue_compra.split("\n") #Split compra-value

# Get element venta blue
blue_venta=driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]')
blue_venta=blue_venta.text #Elemento -> string
blue_venta=blue_venta.split("\n") #Splir venta-value

print("El valor de compra del dolar blue hoy es de", blue_compra[1], "Y de", blue_venta[1], "para la venta")

driver.close() #Cierre de conexion