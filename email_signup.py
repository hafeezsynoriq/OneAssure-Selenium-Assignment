from selenium import webdriver  #Import Webdriver
import time
import config # Reading values from config file
from selenium.webdriver.common.by import By

def create_google_acoount_page(driver ) :
    """Creating New Account"""
    first_name = driver.find_element(By.ID,"firstName")
    first_name.send_keys(config.first_name)     #Enter First Name
    last_name = driver.find_element(By.ID,"lastName")
    last_name.send_keys(config.last_name)     #Enter Last Name
    user_name = driver.find_element(By.ID,"username")
    user_name.send_keys(config.user_email)    #Enter Email
    password = driver.find_element(By.NAME,"Passwd")
    password.send_keys(config.password)     #Enter Password
    confirm = driver.find_element(By.NAME,"ConfirmPasswd")
    confirm.send_keys(config.password)     #Confirm Password
    #Submit form Button
    next_button = driver.find_elements_by_class_name("VfPpkd-vQzf8d")[1]
    next_button.click()
  
def verify_phone_number(driver) :
    phone_number=driver.find_element_by_tag_name("input")
    phone_number.send_keys(config.phone_number)   #Enter Phone Number
    next_button = driver.find_elements_by_class_name("VfPpkd-vQzf8d")[0]
    next_button.click()

def verify_code(driver) :
    time.sleep(50)
    """Enter OTP to verify in  chrome UI manualy"""
    verify_button = driver.find_elements_by_class_name("VfPpkd-vQzf8d")[1]
    verify_button.click()
    """After giving password don't click UI manually to verify. It can happen automatically, Pls wait """
   
def welcome_page(driver) :
    """Date of Birth And Gender Part"""
    day = driver.find_element(By.XPATH,'//*[@id="day"]')
    day.send_keys(config.day)       #Enter Day
    year = driver.find_element(By.XPATH,'//*[@id="year"]')
    year.send_keys(config.year)       #Enter Year
    month = driver.find_elements_by_class_name("UDCCJb")[0]
    month.send_keys(config.month)    #Enter Month
    gender = driver.find_elements_by_class_name("UDCCJb")[1]
    gender.send_keys(config.gender)   #Enter Gender
    #Submit Button
    next_button = driver.find_elements_by_class_name("VfPpkd-vQzf8d")[0]
    next_button.click()

def more_from_number_page(driver):
    """Term & Condition Part"""
    yes_button = driver.find_elements_by_class_name("VfPpkd-vQzf8d")[1]
    yes_button.click()
    print("completed more_page")
    
def privacy_and_termpage(driver):
    """Term & Condition Part"""
    agree_button = driver.find_elements_by_class_name("VfPpkd-vQzf8d")[1]
    agree_button.click()
    print("completed privacy_and_termpage")

driver = webdriver.Chrome(executable_path="./chromedriver.exe") #Webdriver Path
#implicit wait
driver.implicitly_wait(0.5)
#launch URL
driver.get("https://accounts.google.com/signup")

"""Calling Functions"""
create_google_acoount_page(driver)
time.sleep(4)

verify_phone_number(driver)
time.sleep(4)

verify_code(driver)
time.sleep(4)

welcome_page(driver)
time.sleep(4)

more_from_number_page(driver)
time.sleep(4)


privacy_and_termpage(driver)
time.sleep(15)
