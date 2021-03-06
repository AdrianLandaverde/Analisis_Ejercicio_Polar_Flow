from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

PATH= "C:\Program Files (x86)\chromedriver.exe"
driver= webdriver.Chrome(PATH)

correo= input("Correo del usuario: ")
contraseña = input("Contraseña del usuario: ")
sesionInicial=input("Liga de la sesión inicial: ")
sesionFinal=input("Link de la sesión final: ")

driver.get(sesionInicial)

time.sleep(5)
email = driver.find_element_by_id("email")
email.send_keys(correo)
password = driver.find_element_by_id("password")
password.send_keys(contraseña)

time.sleep(5)
password.send_keys(Keys.RETURN)

Deportes=[]
Fechas=[]
Tiempos=[]
Distancias=[]
FrecuenciasMedia=[]
Calorias=[]
TiemposZona1=[]
TiemposZona2=[]
TiemposZona3=[]
TiemposZona4=[]
TiemposZona5=[]

while(True):
    time.sleep(3)
    tiempo= driver.find_element_by_class_name("basic-data-panel__value-container")
    distancia= driver.find_element_by_id("BDPDistance")
    frecuenciaMedia= driver.find_element_by_id("BDPHrAvg")
    calorias= driver.find_element_by_id("BDPCalories")
    zonas= driver.find_elements_by_class_name("supergraph-zonebar__text")
    deporte= driver.find_element_by_id("sportHeading")
    
    Deportes.append((deporte.text).split("\n")[0])
    Fechas.append((deporte.text).split("\n")[1])
    Tiempos.append(tiempo.text)
    Distancias.append(distancia.text)
    FrecuenciasMedia.append(frecuenciaMedia.text)
    Calorias.append(calorias.text)
    TiemposZona1.append(zonas[4].text)
    TiemposZona2.append(zonas[3].text)
    TiemposZona3.append(zonas[2].text)
    TiemposZona4.append(zonas[1].text)
    TiemposZona5.append(zonas[0].text)
    
    flechas= driver.find_element_by_css_selector("i.icon.icon-arrow-right")
    time.sleep(3)
    linkn=driver.current_url
    
    if(linkn!=sesionFinal):
        flechas.click()
    else:
        print("Se ha llegado a la última sesión")
        break
driver.quit()
print("Web scrapping finalizado")

df_datos=pd.DataFrame(
    {"Deporte": Deportes,
     "Fecha": Fechas,
     "Tiempo": Tiempos,
     "Distancia": Distancias,
     "Frecuencia Media": FrecuenciasMedia,
     "Calorias": Calorias,
     "Tiempo Zona 1": TiemposZona1,
     "Tiempo Zona 2": TiemposZona2,
     "Tiempo Zona 3": TiemposZona3,
     "Tiempo Zona 4": TiemposZona4,
     "Tiempo Zona 5": TiemposZona5})

df_datos.to_csv('datos_entrenamiento.csv',index=False, encoding="utf-8-sig")






