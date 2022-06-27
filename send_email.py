#from selenium import webdriver  #Import Webdriver
import time
import config # Reading values from config file
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def enter_mail(driver ) :
    """Enter Email Part"""
    user_email = driver.find_element(By.XPATH,'//*[@id="identifierId"]')
    user_email.send_keys(config.user_email)  #Enter Email
    time.sleep(2)
    next_button = driver.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button')
    next_button.click()

def enter_password(driver ) :
    """Enter Password Part"""
    pwd = driver.find_element(By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input')
    pwd.send_keys(config.password)   #Enter Password
    next_button = driver.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button')
    next_button.click()
    time.sleep(5)

def send_mail(driver):
    driver.find_element(By.XPATH,'/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div').click()
    time.sleep(2)
    to = driver.find_element(By.NAME,'to')
    to.send_keys(config.to_email)    #Enter Receiver Mail
    time.sleep(2)
    subject=driver.find_element(By.NAME,'subjectbox')
    subject.send_keys("OneAssure Selenium Assignment")  #Enter Subject
    text=WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Message Body"]'))
)                                                                                     
    driver.implicitly_wait(3)
    text.send_keys(f" Hi,\n This is an email generated from selenium.\n\n Regards,\n {config.first_name} {config.last_name}")  #Enter Your Message
    time.sleep(2)
    #Click on Send
    send = driver.find_element(By.XPATH,'//*[@id=":q0"]')        
    send.click()
    time.sleep(2)
    
if __name__ == '__main__':
    """ Using undetected_chromedriver to undetected selenium by chrome"""
    driver = uc.Chrome(use_subprocess=True)
    driver.implicitly_wait(1)
    #launch URL
    driver.get("https://mail.google.com/")
    time.sleep(3)

    """Calling Functions"""
    enter_mail(driver)
    time.sleep(3)

    enter_password(driver)
    time.sleep(15)

    send_mail(driver)
    time.sleep(10)