import time 
from datetime import datetime

from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk 


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException



class App(tk.Tk):

    def __init__(self):
        super().__init__()
        
        HEIGHT = 500
        WIDTH = 700 
        self.canvas = tk.Canvas(self, height=HEIGHT, width=WIDTH)
        self.canvas.pack()

        # Top frame.
        self.var_1 = StringVar()
        self.intro_label= tk.Label(self.canvas, font=("arial",13), textvariable=self.var_1, fg="navy")
        self.intro_label.grid(row=0, column=1, columnspan=2, sticky=N+S+W+E, pady=5)
        self.var_1.set("SUPREME BOT HELPER")
        


        # Payment frame.
        self.payment = tk.LabelFrame(self.canvas, padx=15, pady=10, text="payment data", font=("Courier", 11), fg="blue")
        self.payment.grid(row=1, column=0, columnspan=2, rowspan=11, sticky=N+S+W+E)

        
        self.name = tk.Entry(self.payment, font=("Courier",10))
        self.name.grid(row=0, column=1)

        self.label_name = tk.Label(self.payment, font=("Courier",10), text="Full name:")
        self.label_name.grid(row=0, column=0)


        self.email = tk.Entry(self.payment, font=("Courier",10))
        self.email.grid(row=1, column=1)

        self.label_email = tk.Label(self.payment, font=("Courier",10), text="E-mail:")
        self.label_email.grid(row=1, column=0)

        
        self.phone = tk.Entry(self.payment, font=("Courier",10))
        self.phone.grid(row=2, column=1)

        self.label_phone = tk.Label(self.payment, font=("Courier",10), text="Phone number:")
        self.label_phone.grid(row=2, column=0)



        self.street_address = tk.Entry(self.payment, font=("Courier",10))
        self.street_address.grid(row=3, column=1)

        self.label_street_address = tk.Label(self.payment, font=("Courier",10), text="Street + num:")
        self.label_street_address.grid(row=3, column=0)



        self.zip_code = tk.Entry(self.payment, font=("Courier",10))
        self.zip_code.grid(row=4, column=1)

        self.label_zip_code = tk.Label(self.payment, font=("Courier",10), text="ZIP code:")
        self.label_zip_code.grid(row=4, column=0)


        
        self.city = tk.Entry(self.payment, font=("Courier",10))
        self.city.grid(row=5, column=1)

        self.label_city = tk.Label(self.payment, font=("Courier",10), text="City:")
        self.label_city.grid(row=5, column=0)



        self.card_cvv = tk.Entry(self.payment, font=("Courier",10))
        self.card_cvv.grid(row=6, column=1)

        self.label_card_cvv = tk.Label(self.payment, font=("Courier",10), text="Card CVV:")
        self.label_card_cvv.grid(row=6, column=0)



        self.card_number = tk.Entry(self.payment, font=("Courier",10))
        self.card_number.grid(row=7, column=1)

        self.label_card_number = tk.Label(self.payment, font=("Courier",10), text="Card Number:")
        self.label_card_number.grid(row=7, column=0)


        self.card_type = tk.Label(self.payment, font=("Courier",10), text="Card type:")
        self.card_type.grid(row=8, column=0)
        
        self.combobox_card_value = tk.StringVar() 
        self.combobox_card = ttk.Combobox(self.payment, textvar=self.combobox_card_value)
        self.combobox_card.grid(row=8, column=1)
        self.combobox_card["values"] = ("Visa", "Mastercard")
        self.combobox_card.current(1)
        

        self.combobox_card_year = tk.StringVar() 
        self.combobox_card_year = ttk.Combobox(self.payment, textvar=self.combobox_card_year)
        self.combobox_card_year.grid(row=9, column=1)
        self.combobox_card_year["values"] = ("2020", "2021", "2022", "2023", "2024", "2025")
        self.combobox_card_year.current(3)

        self.combobox_card_month = tk.StringVar()
        self.combobox_card_month = ttk.Combobox(self.payment, textvar=self.combobox_card_month)
        self.combobox_card_month.grid(row=10, column=1) 
        self.combobox_card_month["values"] = ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
        self.combobox_card_month.current("5")


        self.label_card_year = tk.Label(self.payment, font=("Courier",10), text="Card Year:")
        self.label_card_year.grid(row=9, column=0)


        self.label_card_month = tk.Label(self.payment, font=("Courier",10), text="Card Month:")
        self.label_card_month.grid(row=10, column=0)

        # Product frame. 
        self.product = tk.LabelFrame(self.canvas, padx=15, pady=10, 
        text="product data", font=("Courier", 11), fg="blue")
        
        self.product.grid(row=1, column=2, rowspan=3, sticky=N+S+W+E) 

        self.keyword = tk.Entry(self.product, font=("Courier",10))
        self.keyword.grid(row=0, column=1)

        self.label_keyword = tk.Label(self.product, font=("Courier",10), text="Keyword:")
        self.label_keyword.grid(row=0, column=0)


        self.color = tk.Entry(self.product, font=("Courier",10))
        self.color.grid(row=1, column=1)

        self.label_color = tk.Label(self.product, font=("Courier",10), text="Color:")
        self.label_color.grid(row=1, column=0)


        self.size = tk.Label(self.product, font=("Courier",10), text="Size:")
        self.size.grid(row=2, column=0)
      

        self.combobox_size_value = tk.StringVar() 
        self.combobox_size = ttk.Combobox(self.product, textvar=self.combobox_size_value)
        self.combobox_size.grid(row=2, column=1)
        self.combobox_size["values"] = ("Medium", "Large", "XLarge")
        self.combobox_size.current("1")
        
        self.combobox_card_year = tk.StringVar() 
        self.combobox_card_year = ttk.Combobox(self.payment, textvar=self.combobox_card_year)
        self.combobox_card_year.grid(row=9, column=1)
        self.combobox_card_year["values"] = ("2020", "2021", "2022", "2023", "2024", "2025")
        self.combobox_card_year.current(3)
        

        self.category = tk.Label(self.product, font=("Courier",10), text="Category:")
        self.category.grid(row=3, column=0)
        

        self.combobox_category_value = tk.StringVar() 
        self.combobox_category = ttk.Combobox(self.product, textvar=self.combobox_category_value)
        self.combobox_category.grid(row=3, column=1)
        self.combobox_category["values"] = ("jackets", "shirts", "tops/sweaters", "sweatshirts", "pants", "shorts", "hats", "bags", "accessories", "shoes", "skate")
        self.combobox_category.current("3")

         # Timer frame. 
        self.timer = tk.LabelFrame(self.canvas, padx=15, pady=10, text="timer", font=("Courier", 11), fg="blue")
        self.timer.grid(row=4, column=2, rowspan=2, sticky=N+S+W+E) 
        
        self.hour = tk.Entry(self.timer, font=("Courier",10))
        self.hour.grid(row=0, column=1)

        self.label_hour = tk.Label(self.timer, font=("Courier",10), text="Hour [0-23]:")
        self.label_hour.grid(row=0, column=0)
        
        self.minute = tk.Entry(self.timer, font=("Courier",10))
        self.minute.grid(row=1, column=1)

        self.label_minute = tk.Label(self.timer, font=("Courier",10), text="Minute [00-59]:")
        self.label_minute.grid(row=1, column=0)

        # Submit button. 
        self.button_frame = tk.LabelFrame(self.canvas)
        self.button_frame.grid(row=7, column=2, rowspan=6, sticky=N+S+W+E)

        self.button = tk.Button(self.button_frame, text="Start", font=15, command=lambda: self.get_data())
        self.button.pack(ipadx=5, ipady=8)
        self.button.config(width=33, height=2)

        
    # timer. 
    def timer(func):
        def wrapper(self, *args, **kwargs):
            start = self.hour.get() + " " + self.minute.get() 
            now = datetime.now()
            while now != start:
                now = datetime.now()
                now = str(now.hour) + " " + str(now.minute)
            return func(self, *args, **kwargs)
        return wrapper

    
    @timer 
    def get_data(self):
        item_data = {"categories": self.combobox_category.get(),
                "keyword": self.keyword.get().title(),
                "colour": self.color.get().title(),
                "size": self.combobox_size.get(),}

        payment_data = {"name": self.name.get(),
                        "email": self.email.get(),
                        "phone_number": self.phone.get(),
                        "street_address": self.street_address.get(),
                        "zip_code": self.zip_code.get(),
                        "city": self.city.get(),
                        "card_cvv": self.card_cvv.get(),
                        "card_number": self.card_number.get(),
                        "card_type": self.combobox_card.get(),
                        "card_expiration_year": self.combobox_card_year.get(),
                        "card_expiration_month": self.combobox_card_month.get(),}
            
        self.bot(item_data, payment_data)
    
    


   
    def bot(self, keys, payment): 
        # Open browser.
        chrome = webdriver.Chrome('./chromedriver.exe')
        
        # Open Supreme website.
        chrome.get("https://www.supremenewyork.com/")
        
        # Go to category.
        chrome.get("https://www.supremenewyork.com/shop/all/" + keys["categories"])
        
        # Go to item.
        while True:
            try:
                # "//div[contains(h1, 'Cutout') and p='Red']"
                chrome.find_element_by_xpath("//div[contains(h1," + "'" + keys["keyword"].title() + "') and p=" + "'" + keys["colour"].title() + "']")
            except NoSuchElementException:
                chrome.refresh()
                time.sleep(2)
            else:
                chrome.find_element_by_xpath("//div[contains(h1," + "'" + keys["keyword"].title() + "') and p=" + "'" + keys["colour"].title() + "']").click()
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
        Select(chrome.find_element_by_id("order_billing_country")).select_by_visible_text("POLAND")
            
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
    app = App()
    app.title("@@kusy")
    app.wm_resizable(0,0)
    app.wm_iconbitmap("./xaxa.ico") 
    app.mainloop()
    