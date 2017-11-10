import getpass
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

USERNAME = input('Username: ')
PASSWORD = getpass.getpass()
print('Chrome is opening, please wait...')

driver = webdriver.Chrome()
driver.set_page_load_timeout(30)
driver.get('https://inside.process-solutions.hu/')
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element_by_id('LoginUser_UserName').send_keys(USERNAME)
driver.find_element_by_id('LoginUser_Password').send_keys(PASSWORD)
driver.find_element_by_id('LoginUser_Password').send_keys(Keys.ENTER)
# driver.find_element_by_id('LoginUser_LoginButton').click()
driver.find_element_by_id('profile_2_ico').click()
# driver.execute_script("document.body.style.zoom='90%'")

table = driver.find_element_by_xpath(
    "//table[@class='htCore']/tbody/tr[1]/td[2]/div[@class='htAutocomplete']/div[@class='htAutocompleteArrow']")
table.click()
sleep(2)
table2 = driver.find_element_by_xpath("//div[@class='handsontableInputHolder']/ul/li/a")
table2.click()
sleep(2)

table3 = driver.find_element_by_xpath(
    "//table[@class='htCore']/tbody/tr[1]/td[4]/div[@class='htAutocomplete']/div[@class='htAutocompleteArrow']")
table3.click()
sleep(2)
table4 = driver.find_element_by_xpath("//div[@class='handsontableInputHolder']/ul/li[1]/a")  # work time li[3] TIL
table4.click()
sleep(2)

table5 = driver.find_element_by_xpath(
    "//table[@class='htCore']/tbody/tr[1]/td[7]/div[@class='htAutocomplete']/div[@class='htAutocompleteArrow']")
table5.click()
sleep(2)
table6 = driver.find_element_by_xpath("//div[@class='handsontableInputHolder']/ul/li[1]/a")
table6.click()
sleep(2)

table7 = driver.find_element_by_xpath("//table[@class='htCore']/tbody/tr[1]/td[10]")
table7.click()
table7.click()
sleep(2)
# driver.execute_script("document.getElementsByClassName('current fill').innerHTML = '8.00'")
table7 = driver.find_element_by_xpath(
    "//div[@class='smartContainerBodyContent handsontable']/div[@class='handsontableInputHolder'][2]/textarea")
table7.send_keys('8.00')
table7.send_keys(Keys.ENTER)

submit = driver.find_element_by_xpath("//div[@class='btn-group']/a[@class='combined-btn q-tooltip'][2]")
submit.click()
submit.send_keys(Keys.TAB)
submit.send_keys(Keys.TAB)
submit.send_keys(Keys.TAB)
submit.send_keys(Keys.TAB)
submit.send_keys(Keys.TAB)
submit.send_keys(Keys.TAB)
submit.send_keys(Keys.TAB)
# submit.send_keys(Keys.SPACE)
# for i in range(7):
#     submit.send_keys(Keys.TAB)
# submit.send_keys(Keys.ENTER)

# table7 = driver.find_element_by_xpath("//textarea[@class='handsontableInput']")
# sleep(2)
# table = driver.find_element_by_xpath("//table[@class='htCore']/tbody/tr[2]/td[2]/div[@class='htAutocomplete']/div[@class='htAutocompleteArrow']")
# table.click()
# sleep(2)
# table2 = driver.find_element_by_xpath("//div[@class='handsontableInputHolder']/ul/li/a")
# table2.click()
# sleep(2)
#
# table3 = driver.find_element_by_xpath("//table[@class='htCore']/tbody/tr[2]/td[4]/div[@class='htAutocomplete']/div[@class='htAutocompleteArrow']")
# table3.click()
# sleep(2)
# table4 = driver.find_element_by_xpath("//div[@class='handsontableInputHolder']/ul/li[3]/a")
# table4.click()
# sleep(2)
#
# table5 = driver.find_element_by_xpath("//table[@class='htCore']/tbody/tr[2]/td[7]/div[@class='htAutocomplete']/div[@class='htAutocompleteArrow']")
# table5.click()
# sleep(2)
# table6 = driver.find_element_by_xpath("//div[@class='handsontableInputHolder']/ul/li[1]/a")
# table6.click()
#
