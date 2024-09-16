from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import config

def checkFinish():
    while True:
        choice = input("Are you done? (y/n):")
        if choice.lower() == 'y':
            break
def readDataFromExcel():
    df = pd.read_excel(config.excelFileName)
    rows = []
    for _, row in df.iterrows():
        nom = row[config.nameClientColumn]
        domain = row[config.domainColumn]
        telephone = row[config.telephoneColumn]
        if pd.isna(nom) or pd.isna(domain) or pd.isna(telephone):
            continue
        nom = str(nom).strip()
        domain = str(domain).strip()
        telephone = str(telephone).strip()
        rows.append([nom, domain, telephone])
    return rows


def filterData(data):
    dataFilter = []
    for row in data:
        telephone = row[2]
        lenRow2 = len(telephone)

        if lenRow2 == 11:
            secondInt = int(telephone[1])
            firstInt = int(telephone[0])
            if secondInt != 5:
                if secondInt != 8:
                    if firstInt == 0:
                        row[2] = '+212 ' + row[2][1:]
                    dataFilter.append(row)
        elif lenRow2 == 15:
            fiveInt = int(telephone[5])
            if fiveInt != 5:
                if fiveInt != 8:
                    dataFilter.append(row)
    return dataFilter


def generateMessage(fullName, domaine):
    message = f"Cher(e) responsable {fullName},%0ANous somme ApexWeb, une agence spécialisée dans la création de sites web. Aujourd'hui, une présence en ligne est essentielle pour toute entreprise, y compris {domaine}. Un site web peut améliorer votre visibilité, faciliter les réservations pour vos clients et renforcer votre image de marque. En étant plus présent en ligne, vous paraîtrez plus légitime et attirerez ainsi davantage de clients.%0AContactez-nous pour discuter de la manière dont nous pouvons aider votre entreprise de {domaine} à se développer en ligne.%0AEmail : inbox@apexweb.live,%0ANum téléphone : 0612-441246,%0ANotre Site: https://apexweb.live"
    return message


if __name__ == '__main__':
    data = readDataFromExcel()
    data = filterData(data)
    driver = wd.Chrome()
    driver.get(config.adminApexWebCopyImage)
    time.sleep(2)
    driver.find_element(By.ID, 'imageInput').send_keys(config.imageFileToCopping)
    driver.find_element(By.CSS_SELECTOR, 'div.card-body button').click()
    driver.get("https://web.whatsapp.com/")
    time.sleep(2)
    checkFinish()
    for row in data:
        fullName = row[0]
        domaine = row[1]
        telephone = row[2]
        message = generateMessage(fullName, domaine)
        driver.get(f"https://web.whatsapp.com/send?phone={telephone}&text={message}")
        time.sleep(15)
        messageInput = driver.find_elements(By.CLASS_NAME, 'x1hx0egp.x6ikm8r.x1odjw0f.x1k6rcq7.x6prxxf')[1]
        messageInput.send_keys(Keys.CONTROL, 'v')
        time.sleep(5)
        btnSend = driver.find_element(By.CLASS_NAME, 'x78zum5.x6s0dn4.xl56j7k.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1f6kntn.xk50ysn.x7o08j2.xtvhhri.x1rluvsa.x14yjl9h.xudhj91.x18nykt9.xww2gxu.xu306ak.x12s1jxh.xkdsq27.xwwtwea.x1gfkgh9.x1247r65.xng8ra')
        btnSend.send_keys(Keys.RETURN)
        time.sleep(2)

