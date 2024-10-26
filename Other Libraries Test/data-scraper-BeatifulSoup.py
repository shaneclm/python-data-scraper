###############################################################################################
# Program: Data Scraping with BeautifulSoup
# Author: Shania Francine T. Cloma
# Purpose: This program is created for self-study and practice in web scraping.
#
# Requirements:
# To install the BeautifulSoup library, open the terminal (or command prompt) and enter:
#     pip install beautifulsoup4
# 
# To install the Requests library for sending HTTP requests, enter:
#     pip install requests
###############################################################################################

# import libary
from bs4 import BeautifulSoup		# parsing HTML content
import requests						# sending HTTP requests
import sys							
import io

# allows special characters (peso symbol) to be displayed in the output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# URL of the target product page
url = "https://ecommerce.datablitz.com.ph/products/steelseries-arctis-1-all-platform-wired-gaming-headset-ps5-ps4-pc-xbox-switch-pn61425"

# send an HTTP GET request to the specified URL
# the HTML content of the page is retrieved and stored in the 'result' variable
result = requests.get(url)

# parse the HTML content using BeautifulSoup and specify the parser as "html.parser"
doc = BeautifulSoup(result.text, "html.parser")

# locates the span element with the specific class and text "Price:"
price_label = doc.find("span", class_="product-form__info-title text--strong", string="Price:")
if price_label:
    price_container = price_label.find_next("div", class_="price-list")
    
    if price_container:
        price_value = price_container.find("span", class_="price")
        
        if price_value:
            print("Price:", price_value.text.strip())
            
        else:
            print("Price value not found.")
            
    else:
        print("Price container not found.")
        
else:
    print("Price label not found.")
    

# Key Takeaways: It is important to have a good understanding of basic HTML structure to accurately locate and extract the target data.
