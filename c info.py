import requests
from bs4 import BeautifulSoup

url = "https://exchange.xforce.ibmcloud.com/threat-group/apt28"  # Example: APT28 (Fancy Bear)

headers = {
    "User-Agent": "Mozilla/5.0"  # To avoid being blocked
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

# Look at the page source (Ctrl+U) to find actual elements
# For now just extract page title as test:
title = soup.find("title").text
print("Page Title:", title)
import requests
from bs4 import BeautifulSoup

url = "https://exchange.xforce.ibmcloud.com/campaigns"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

# Find all campaign names (IBM X-Force may use dynamic JS – this may not work fully)
campaigns = soup.find_all("a", class_="link")  # update class based on inspection

for c in campaigns:
    print("📌 Campaign:", c.text.strip())
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#  Make sure you have Chrome + ChromeDriver installed
driver_path = "D:\\chromedriver.exe"  # ✅ update this to your path

service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# 1. Open IBM X-Force Campaigns Page
driver.get("https://exchange.xforce.ibmcloud.com/campaigns")
time.sleep(10)  # wait for JS to load

# 2. Get campaign titles (adjust selector as needed)
elements = driver.find_elements(By.CSS_SELECTOR, 'div.tile-title')  # Update CSS if needed

print("\n Found Campaigns:\n")
for el in elements:
    print("📌", el.text)

driver.quit()
