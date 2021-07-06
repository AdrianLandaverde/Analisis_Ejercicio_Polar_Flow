from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH= "C:\Program Files (x86)\chromedriver.exe"
driver= webdriver.Chrome(PATH)

correo= "usuario"
contraseña = "cpntraseña"
sesionInicial="link"
sesionFinal="link2"

driver.get(sesionInicial)

time.sleep(5)
email = driver.find_element_by_id("email")
email.send_keys(correo)
password = driver.find_element_by_id("password")
password.send_keys(contraseña)

time.sleep(5)
password.send_keys(Keys.RETURN)

Deportes=[]
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
        break
driver.quit()





