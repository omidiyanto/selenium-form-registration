from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
import requests  # Import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

# Static variables
phoneNumber = "+6285127242728"
department = "Research"
Role = "Student"
CompanyName = "Infinite Learning Indonesia"
RegionName = "Indonesia"
PostalCode = "29124"
City = "Batam"

# Read CSV file using pandas
csv_file_path = 'data.csv'
df = pd.read_csv(csv_file_path)

# Iterate through data
for index, row in df.iterrows():
    email = row['Email IL']
    password = row['Password IL']
    username = row['Username RHNID']
    
    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    
    # 1. Open Chrome and navigate to webmail
    web = webdriver.Chrome(options=chrome_options)
    web.get('https://webmail.infinitelearningstudent.id')
    
    # Wait for the page to load and elements to appear
    wait = WebDriverWait(web, 20)  # Max wait time 20 seconds
    
    # 2. Fill in email
    emailInput = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[3]/div/div/div[2]/div[2]/form/div[2]/input')))
    emailInput.send_keys(email)
    
    # 3. Fill in password
    passwordInput = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[3]/div/div/div[2]/div[2]/form/div[4]/input')))
    passwordInput.send_keys(password)
    
    # 4. Click Login
    LoginButton = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[3]/div/div/div[2]/div[2]/form/div[5]/div/button')))
    LoginButton.click()
    time.sleep(3)
    
    # 5. Click Open
    ClickOpen = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="launchActiveButton"]')))
    ClickOpen.click()
    
    # 6. Click Recent Email
    ClickRecentEmail = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="rcmrowMQ"]')))
    ClickRecentEmail.click()
    
    # Wait for the page to load
    time.sleep(2)
    
    # Capture the URL after clicking Recent Email
    current_url = web.current_url
    print(f"Captured URL: {current_url}")
    
    # Parse the URL and modify query parameters
    parsed_url = urlparse(current_url)
    query_params = parse_qs(parsed_url.query)
    query_params['_action'] = 'show'
    query_params['_uid'] = '1'
    query_params['_extwin'] = '1'
    
    # Construct the new URL
    new_query_string = urlencode(query_params, doseq=True)
    new_url = urlunparse(parsed_url._replace(query=new_query_string))
    
    # Navigate to the modified URL
    web.get(new_url)
    
    # Optionally, add a wait to ensure the new page has loaded
    time.sleep(1)

    # 7. Click given link
    ClickGivenLink = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="message-htmlpart1"]/p[2]/a')))
    ClickGivenLink.click()
    time.sleep(3)  # Increase time to ensure page fully loads
    
    # 8. Verify Process
    url = f"https://script.google.com/macros/s/AKfycbyxlCOsUmZ5kss43xpUseC7EsHxiFNHdILwr-lBPp_xowZF5Hgp82X3nSsdJe-EizB2Dw/exec?recipient={email}&value=VERIFIED"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    print(f"For {email} --> Response: {response.text}")
    
   
    time.sleep(2)
    web.quit()
