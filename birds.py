import json
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.wikiaves.com.br/especies.php?t=t")
elems = driver.find_elements(By.XPATH, '//a[@title="Descrição da espécie"]/i | //a[@class="font-green-dark"]')

out = open("brazilBirds.json", "w+")

dict = {
    "birds": []
}

for idx, elem in enumerate(elems):
    if (idx % 2) == 0:
        obj = {
            "scientific": elem.get_attribute('innerHTML'),
            "common": elems[idx + 1].get_attribute('innerHTML')
        }
        dict["birds"].append(obj)

y = json.dumps(dict)

out.write(y)

out.close()

driver.close()
