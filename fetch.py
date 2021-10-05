import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import getpass
import json
from agefromname import AgeFromName


age_from_name = AgeFromName()

userStr = input("Votre username :")
passwordStr = getpass.getpass("votre password:")

browser = webdriver.Chrome()
#browser.get('https://auth.mines-paristech.fr/cas/login')
browser.get('https://auth-par.mines-paristech.fr/cas/login?service=https%3A%2F%2Fldap-ihm.mines-paristech.fr%2Fninja%2Findex.jsp')
time.sleep(2)

username = browser.find_element_by_id('username')
username.send_keys(userStr)

password = browser.find_element_by_id('password')
password.send_keys(passwordStr)

#signInButton = browser.find_element_by_class_name('btn-submit')
#signInButton = browser.find_element_by_class_name('mdc-button mdc-button--raised')
#signInButton.click()
password.send_keys(Keys.RETURN)
time.sleep(2)

URL = "https://tom.mines-paristech.fr:8443/ninja/index.jsp"
browser.get(URL)

#URL = "https://tom.mines-paristech.fr:8443/ninja/pages/listPersons!listPersons.action?personUid=amaury.breheret"

URL ="https://ldap-ihm.minesparis.psl.eu/ninja/pages/listPersons!listPersons.action?personUid=amaury.breheret"
browser.get(URL)

table = browser.find_element_by_xpath('//*[@id="form"]/table/tbody')

persons = []
for r,row in enumerate(table.find_elements_by_xpath('.//tr')):
    if r == 0 : 
        continue
        
    cols = row.find_elements_by_xpath('.//th')
    type = cols[5].get_attribute('innerHTML')
    if type == 'eleve' or type == 'vacataire' :
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
        
    prenom = persons[i]["givenName:"]
    prob = age_from_name.prob_male(prenom, minimum_age=20, maximum_age=70 )
    print("prob(",prenom,")=====>",prob)
    if prob > 0.4 :
        prenom = persons[i]["sex_estimation"] = "male"
    else :
        prenom = persons[i]["sex_estimation"] = "female"
    
    print(persons[i])

with open('persons.json', 'w') as outfile:
    json.dump(persons, outfile,indent=4)

browser.close()






























