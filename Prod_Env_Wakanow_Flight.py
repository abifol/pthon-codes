import time
import codecs
import pyperclip
import data as data
import requests
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

start = time.time()
driver = webdriver.Chrome(r"C:\Users\Yewande Odukomaiya\chromedriver.exe")
options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
driver.get('https://www.wakanow.com')

driver.maximize_window()

try:
    WebDriverWait(driver, 3000).until(EC.element_to_be_clickable(
        (By.ID, "itinerary_0_departure")))
finally:
    print('First Element Found!')

from_where = driver.find_element_by_id("itinerary_0_departure").send_keys("Lagos")

try:
    WebDriverWait(driver, 3000).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="ngb-nav-0-panel"]/div/app-flight-search-widget/form/div[3]/div/div[1]/div/div['
                   '1]/app-auto-complete-input/div/div/div/div/div[1]/a/div[1]/p[1]')))
finally:
    print('Second Element Found!')

from_where = driver.find_element_by_xpath(
    '//*[@id="ngb-nav-0-panel"]/div/app-flight-search-widget/form/div[3]/div/div[1]/div/div['
    '1]/app-auto-complete-input/div/div/div/div/div[1]/a/div[1]/p[1]').click()

to_where = driver.find_element_by_id("itinerary_0_destination").send_keys("Abuja")

try:
    WebDriverWait(driver, 3000).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="ngb-nav-0-panel"]/div/app-flight-search-widget/form/div[3]/div/div[2]/div/div['
                   '1]/app-auto-complete-input/div/div/div/div/div/a/div[1]/p[1]')))
finally:
    print('Third Element Found!')

to_where = driver.find_element_by_xpath(
    '//*[@id="ngb-nav-0-panel"]/div/app-flight-search-widget/form/div[3]/div/div[2]/div/div['
    '1]/app-auto-complete-input/div/div/div/div/div/a/div[1]/p[1]').click()

date_leave_on = driver.find_element_by_xpath('//*[@id="ngb-nav-0-panel"]/div/app-flight-search-widget/form/div['
                                             '3]/div/div[3]/div/div[1]/div/div[1]/input').click()

date_leave_on = driver.find_element_by_xpath(
    '//*[@id="ngb-nav-0-panel"]/div/app-flight-search-widget/form/div[3]/div/div[3]/div/div['
    '1]/div/ngb-datepicker/div[2]/div/ngb-datepicker-month/div[5]/div[4]/span').click()

date_return_on = driver.find_element_by_xpath('//*[@id="ngb-nav-0-panel"]/div/app-flight-search-widget/form/div['
                                              '3]/div/div[3]/div/div[1]/div/ngb-datepicker/div[2]/div['
                                              '1]/ngb-datepicker-month/div[5]/div[7]/span').click()

search = driver.find_element_by_xpath('//*[@id="ngb-nav-0-panel"]/div/app-flight-search-widget/form/div[3]/div/div['
                                      '3]/div/div[1]/button/span').click()

try:
    WebDriverWait(driver, 3000).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="ngb-nav-3-panel"]/div/div/button')))
finally:
    print('Fourth Element Found!')

# Selecting preferred airline and flight.

view_flight = driver.find_element_by_xpath('//*[@id="ngb-nav-3-panel"]/div/div/button').click()

book_flight = driver.find_element_by_xpath('/html/body/app-root/app-culture-wrapper/app-flights-listing/div/div/div'
                                           '/div/div[3]/app-flight-details[1]/a/div[2]/div[2]/div[1]/div[2]/div/div['
                                           '2]/button').click()

# Fill in passenger's information.

try:
    WebDriverWait(driver, 3000).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/app-root/app-culture-wrapper/app-booking/div/app-customer'
                   '-info/div/div/div[1]/form/div[1]/div[2]/div/div[1]/div[1]/div['
                   '1]/div/div/select/option[2]')))
finally:
    print('Fifth Element Found!')

select_title = driver.find_element_by_xpath('/html/body/app-root/app-culture-wrapper/app-booking/div/app-customer'
                                            '-info/div/div/div[1]/form/div[1]/div[2]/div/div[1]/div[1]/div['
                                            '1]/div/div/select/option[2]').click()

enter_surname = driver.find_element_by_xpath('/html/body/app-root/app-culture-wrapper/app-booking/div/app-customer'
                                             '-info/div/div/div[1]/form/div[1]/div[2]/div/div[1]/div[1]/div['
                                             '1]/div/input').send_keys('Akala')

enter_first_name = driver.find_element_by_xpath('/html/body/app-root/app-culture-wrapper/app-booking/div/app-customer'
                                                '-info/div/div/div[1]/form/div[1]/div[2]/div/div[1]/div[1]/div['
                                                '2]/input').send_keys('Anuoluwapo')

enter_middle_name = driver.find_element_by_xpath('/html/body/app-root/app-culture-wrapper/app-booking/div/app'
                                                 '-customer-info/div/div/div[1]/form/div[1]/div[2]/div/div[1]/div['
                                                 '2]/div[1]/input').send_keys('Akin')

enter_yob = driver.find_element_by_xpath('/html/body/app-root/app-culture-wrapper/app-booking/div/app-customer-info'
                                         '/div/div/div[1]/form/div[1]/div[2]/div/div[1]/div[2]/div[3]/div/div['
                                         '1]/select/option[21]').click()
enter_mob = driver.find_element_by_xpath('/html/body/app-root/app-culture-wrapper/app-booking/div/app-customer-info'
                                         '/div/div/div[1]/form/div[1]/div[2]/div/div[1]/div[2]/div[3]/div/div['
                                         '2]/select/option[7]').click()
enter_dob = driver.find_element_by_xpath('/html/body/app-root/app-culture-wrapper/app-booking/div/app-customer-info'
                                         '/div/div/div[1]/form/div[1]/div[2]/div/div[1]/div[2]/div[3]/div/div['
                                         '3]/select/option[19]').click()
enter_email = driver.find_element_by_xpath('/html/body/app-root/app-culture-wrapper/app-booking/div/app-customer-info'
                                           '/div/div/div[1]/form/div[2]/div[2]/div/div/div[1]/input').send_keys(
    'wakanowtester@gmail.com.com')
enter_phone_no = driver.find_element_by_xpath('/html/body/app-root/app-culture-wrapper/app-booking/div/app-customer'
                                              '-info/div/div/div[1]/form/div[2]/div[2]/div/div/div['
                                              '2]/div/input').send_keys('08068777272')

check_tc = driver.find_element_by_xpath('/html/body/app-root/app-culture-wrapper/app-booking/div/app-customer-info'
                                        '/div/div/div[1]/form/div[3]/div/div/div/label').click()

proceed = driver.find_element_by_xpath('/html/body/app-root/app-culture-wrapper/app-booking/div/app-customer-info/div'
                                       '/div/div[1]/form/div[3]/div/button').click()

# time.sleep(10)
# check_full_payment = driver.find_element_by_xpath('/html/body/app-root/app-culture-wrapper/app-booking/div/app'
# '-additional-services/div/div/div[1]/div[1]/div[2]/div/div['
# '1]/div/label').click()

try:
    WebDriverWait(driver, 3000).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/app-root/app-culture-wrapper/app-booking/div/app'
                   '-additional-services/div/div/div[1]/div[2]/div/button/span')))
finally:
    print('Sixth Element Found')

essentials_proceed = driver.find_element_by_xpath('/html/body/app-root/app-culture-wrapper/app-booking/div/app'
                                                  '-additional-services/div/div/div[1]/div[2]/div/button/span').click()
try:
    WebDriverWait(driver, 300).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="ngb-nav-17"]/div')))
finally:
    print('Seventh Element Found')

select_payment_method = driver.find_element_by_xpath('//*[@id="ngb-nav-17"]/div').click()

payment_proceed = driver.find_element_by_xpath('//*[@id="ngb-nav-17-panel"]/div/div[2]/button/span').click()

try:
    WebDriverWait(driver, 3000).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/app-root/app-culture-wrapper/app-booking/div/app-summary'
                   '/div/div[1]/div[1]/a')))
finally:
    print('Eighth Element Found!')

copy_booking_id = driver.find_element_by_xpath('/html/body/app-root/app-culture-wrapper/app-booking/div/app-summary'
                                               '/div/div[1]/div[1]/a').click()

booking_id = pyperclip.paste()

file = r"C:\Users\Yewande Odukomaiya\PycharmProjects\pythonProject\bookingid"
f = codecs.open(file, encoding='utf-8', mode='a+')
end = time.time()
total_time = (end - start)//60
env = 'ProdEnv'

# Write a unicode string to the file.
f.write(env + ' = ' + booking_id + ',' + ' ' + 'Date & Time: ' + str(datetime.datetime.now()) + ',' + ' ' + 'Time '
                                                                                                            'taken to'
                                                                                                            ' run in '
                                                                                                            'minutes: '
                                                                                                            '' + str(
    total_time) + '\n')

print('Your booking id : ' + booking_id + ' has been logged and ran for ' + str(total_time))

driver.close()