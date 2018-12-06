from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import getpass

userStr = input("Votre username :")
passwordStr = getpass.getpass("votre password:")

browser = webdriver.Chrome()
browser.get('https://auth.mines-paristech.fr/cas/login')

username = browser.find_element_by_id('username')
username.send_keys(userStr)

password = browser.find_element_by_id('password')
password.send_keys(passwordStr)

signInButton = browser.find_element_by_class_name('btn-submit')
signInButton.click()

URL = "https://tom.mines-paristech.fr:8443/ninja/index.jsp"
browser.get(URL)

URL = "https://tom.mines-paristech.fr:8443/ninja/pages/listPersons!listPersons.action?personUid=amaury.breheret"
browser.get(URL)

table = browser.find_element_by_xpath('//*[@id="form"]/table/tbody')

persons = []
for r,row in enumerate(table.find_elements_by_xpath('.//tr')):
    if r == 0 : 
        continue
        
    cols = row.find_elements_by_xpath('.//th')
    if cols[5].get_attribute('innerHTML') == 'eleve' :
        continue
        
    Uid = cols[1].find_element_by_xpath('.//a')
    person = {
    'nom' : cols[2].get_attribute('innerHTML'),
    'prenom' : cols[3].get_attribute('innerHTML'),
    'type' : cols[5].get_attribute('innerHTML'),
    'Uid' : Uid.get_attribute('innerHTML'),
    'link' : Uid.get_attribute('href')
    }
    
    print(person['nom'])
    persons.append(person)
    
for i,person in enumerate(persons):
    browser.get(person['link'])
    
    table = browser.find_element_by_xpath('//*[@id="form"]/table/tbody/tr/td[2]/table/tbody')
    for r,row in enumerate(table.find_elements_by_xpath('.//tr')):
        if r == 0 : 
            continue
            
        cols = row.find_elements_by_xpath('.//td')
        key = cols[0].find_element_by_xpath('.//label').get_attribute('innerHTML')
        value = cols[1].find_element_by_xpath('.//label').get_attribute('innerHTML')
        persons[i][key] = value
    
    print(persons[i])

# browser.close()






























