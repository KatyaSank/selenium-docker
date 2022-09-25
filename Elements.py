from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium import webdriver


driver = webdriver.Remote(
   command_executor="http://localhost:4444/wd/hub",
   desired_capabilities={
            "browserName": "chrome",
            "browserVersion": "96.0",
            "platformName": "Linux",
        })

#service = Service('C:\\Users\\Admin\\Desktop\\Python\\chromedriver.exe')
#driver: WebDriver = Chrome()

driver.get("https://demoqa.com/elements")
driver.maximize_window()

action = ActionChains(driver)

driver.find_element(By.ID, 'item-0').click()
driver.find_element(By.ID, 'userName').send_keys("Kate Sankovich")
driver.find_element(By.ID, 'userEmail').send_keys("Kate@gmail.com")
driver.find_element(By.ID, 'currentAddress').send_keys("Klaipeda")
driver.find_element(By.ID, 'permanentAddress').send_keys("World")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element(By.ID, 'submit').click()

driver.find_element(By.ID, 'item-1').click()
driver.find_element(By.CLASS_NAME, 'rct-icon').click()
driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[2]/span/label/span[3]').click()
driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/span/label/span[3]').click()
driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/span/label/span[3]').click()
driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/span/label/span[3]').click()

driver.find_element(By.ID, 'item-2').click()
driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]/label').click()
driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/label').click()

driver.find_element(By.ID, 'item-3').click()

driver.find_element(By.ID, 'addNewRecordButton').click()
driver.find_element(By.ID, 'firstName').send_keys("Katie")
driver.find_element(By.ID, 'lastName').send_keys("Sankovich")
driver.find_element(By.ID, 'userEmail').send_keys("Katya@gmail.com")
driver.find_element(By.ID, 'age').send_keys("99")
driver.find_element(By.ID, 'salary').send_keys("999")
driver.find_element(By.ID, 'department').send_keys("QA")
driver.find_element(By.ID, 'submit').click()

driver.find_element(By.XPATH, '//*[@id="delete-record-1"]').click()

driver.find_element(By.XPATH, '//*[@id="edit-record-3"]').click()
driver.find_element(By.ID, 'age').clear()
driver.find_element(By.ID, 'age').send_keys("0")
driver.find_element(By.ID, 'firstName').clear()
driver.find_element(By.ID, 'firstName').send_keys("S")
driver.find_element(By.ID, 'submit').click()

driver.find_element(By.ID, 'searchBox').send_keys("S")
driver.find_element(By.XPATH, '//*[@id="basic-addon2"]/span').click()

driver.find_element(By.ID, 'item-4').click()
driver.find_element(By.ID, 'doubleClickBtn')
action.double_click()




#driver.close()
