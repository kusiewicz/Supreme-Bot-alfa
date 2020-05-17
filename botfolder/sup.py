import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from datetime import datetime 
from selenium.common.exceptions import NoSuchElementException


keys = {
        "categories": "sweatshirts",
        "name": "cross",
        "colour": "black",
        "size": "large",
         }


payment = {
        "name": "John Doe",
        "email": "johndoe@gmail.com",
        "phone_number": "731693602",
        "street_address": "Zachodnia 8 11",
        "zip_code": "53 621",
        "city": "Wroclaw",
        "card_cvv": "123",
        "card_number": "5169 2811 0291 9422",
        "card_type": "Mastercard",
        "card_expiration_year": "2021",
        "card_expiration_month": "08"
            }

timer = {
    "hour": "17",
    "minute": "25",
        }

start = timer["hour"] + " " + timer["minute"]

def timer(func):
    def wrapper(*args, **kwargs):
        now = datetime.now()
        while now != start:
            now = datetime.now()
            now = str(now.hour) + " " + str(now.minute)
        func(*args, **kwargs)
    return wrapper  
         
        

#@timer
def bot(keys, payment):
    

    # Go to category.
    chrome.get("https://www.supremenewyork.com/shop/all/" + keys["categories"])
     
    # Go to item.
    while True:
        try:
            # "//div[contains(h1, 'Cutout') and p='Red']"
            chrome.find_element_by_xpath("//div[contains(h1," + "'" + keys["name"].title() + "') and p=" + "'" + keys["colour"].title() + "']")
        except NoSuchElementException:
            chrome.refresh()
            time.sleep(2)
        else:
            chrome.find_element_by_xpath("//div[contains(h1," + "'" + keys["name"].title() + "') and p=" + "'" + keys["colour"].title() + "']").click()
            break 
 

    # Wait for fully load.
    time.sleep(2) 

    # Pick a size. 
    Select(chrome.find_element_by_id("size")).select_by_visible_text(keys["size"].title())
       
    # Add to cart.
    chrome.find_element_by_name('commit').click()
        
    # Wait for checkout button to load.
    time.sleep(1)
        
    # Submit checkout.
    chrome.find_element_by_class_name('checkout').click()
        
    # Fill out checkout screen fields.
    chrome.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(payment["name"])
    chrome.find_element_by_xpath('//*[@id="order_email"]').send_keys(payment["email"])
    chrome.find_element_by_xpath('//*[@id="order_tel"]').send_keys(payment["phone_number"])
    chrome.find_element_by_xpath('//*[@id="bo"]').send_keys(payment["street_address"])
    chrome.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(payment["zip_code"])
    chrome.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(payment["city"])
    chrome.find_element_by_xpath('//*[@id="vval"]').send_keys(payment["card_cvv"])
    chrome.find_element_by_xpath('//*[@id="cnb"]').send_keys(payment["card_number"])
        
    # Select the country.
    Select(chrome.find_element_by_id("order_billing_country")).select_by_visible_text("GERMANY")
        
    # Select the card type.
    Select(chrome.find_element_by_id("credit_card_type")).select_by_visible_text(payment["card_type"])
        
    # Select card expiration date.
    Select(chrome.find_element_by_id("credit_card_month")).select_by_visible_text(payment["card_expiration_month"])
    Select(chrome.find_element_by_id("credit_card_year")).select_by_visible_text(payment["card_expiration_year"])

    # Accept terms & conditions.
    chrome.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p/label/div/ins').click()

    # Checkout.
    chrome.find_element_by_name('commit').click()
        

    
       
if __name__ == "__main__":
    # Open browser.
    chrome = webdriver.Chrome('./chromedriver.exe')
    
    # Open Supreme website.
    chrome.get("https://www.supremenewyork.com/")
    bot(keys, payment)
