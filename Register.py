from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import requests

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
    firstName = row['First Name']
    lastName = row['Last Name']
    username = row['Username RHNID']
    password = row['Password RHNID']

    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    # 1. Open Chrome and go to rol.redhat.com
    web = webdriver.Chrome(options=chrome_options)
    web.get('https://rol.redhat.com/rol/app/login')
    # Wait until the page is fully loaded
    wait = WebDriverWait(web, 20)  # Maximum wait time of 20 seconds

    # 2. Click Register Account
    RegisterButton = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div/div[1]/div[3]/div/a/button')))
    RegisterButton.click()

    # 3. Fill USERNAME RHNID
    usernameInput = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div/main/section/div/div/form/div[3]/section[1]/div[1]/div[2]/input')))
    usernameInput.send_keys(username)

    # 4. Fill password RHNID
    passwordInput = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div/main/section/div/div/form/div[3]/section[1]/div[2]/div[2]/div[1]/input')))
    passwordInput.send_keys(password)

    # 5. Fill Confirmation Password RHNID
    passConfirmInput = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div/main/section/div/div/form/div[3]/section[1]/div[4]/div[2]/div/input')))
    passConfirmInput.send_keys(password)

    # 6. Fill First Name
    firstNameInput = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div/main/section/div/div/form/div[3]/section[2]/div/div[1]/div/div[2]/input')))
    firstNameInput.send_keys(firstName)

    # 7. Fill Last Name
    lastNameInput = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div/main/section/div/div/form/div[3]/section[2]/div/div[2]/div/div[2]/input')))
    lastNameInput.send_keys(lastName)

    # 8. Fill email
    emailInput = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div/main/section/div/div/form/div[3]/section[2]/div/div[3]/div/div[2]/input')))
    emailInput.send_keys(email)

    # 9. Fill Phone Number
    phoneNumberInput = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div/main/section/div/div/form/div[3]/section[2]/div/div[4]/div/div[2]/input')))
    phoneNumberInput.send_keys(phoneNumber)

    # 10. Fill Department
    departmentInput = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div/main/section/div/div/form/div[3]/section[2]/div/div[5]/div[2]/select')))
    departmentInput.send_keys(department)

    # 11. Fill Job Role
    RoleInput = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div/main/section/div/div/form/div[3]/section[2]/div/div[6]/div[2]/select')))
    RoleInput.send_keys(Role)

    # 12. Fill account type
    accountTypeButton = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div/main/section/div/div/form/div[3]/section[3]/div[2]/div[2]/div[1]/input')))
    accountTypeButton.click()

    # 13. Fill company name
    CompanyNameInput = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div/main/section/div/div/form/div[3]/section[4]/div[2]/div[2]/input')))
    CompanyNameInput.send_keys(CompanyName)

    # 14. Fill region
    RegionNameInput = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div/main/section/div/div/form/div[3]/section[4]/div[3]/div[2]/select')))
    RegionNameInput.send_keys(RegionName)
    time.sleep(1)

    # 15. Fill address
    AddressInput = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div/main/section/div/div/form/div[3]/section[4]/div[4]/div[1]/div[2]/input')))
    AddressInput.send_keys(RegionName)
    time.sleep(1)

    # 16. Fill postal code
    PostalCodeInput = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="user.attributes.addressPostalCode"]')))
    PostalCodeInput.send_keys(PostalCode)

    # 17. Use Tab key to move to city
    PostalCodeInput.send_keys(Keys.TAB)

    # 18. Fill city
    CityInput = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="user.attributes.addressCity"]')))
    CityInput.send_keys(City)

    # 19. Disable ads
    AdsButton = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div/main/section/div/div/form/div[3]/section[5]/section/div[2]/div/div[2]/input')))
    AdsButton.click()

    # 20. Click Submit
    SubmitButtom = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div/main/section/div/div/form/div[4]/div/div/button')))
    SubmitButtom.click()
    time.sleep(2)

    # 21. Keep Entered Address
    KeepAddress = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/footer/button[2]')))
    KeepAddress.click()

    # 22. Agree
    AgreeCheckbox = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/main/div/app-root/div/app-sso-terms/div/div/div/form/div[1]/div[3]/input')))
    AgreeCheckbox.click()

    # 23. Submit Agree
    SubmitAgree = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/main/div/app-root/div/app-sso-terms/div/div/div/form/div[2]/p/span/input')))
    SubmitAgree.click()

    # 24. Verify Process
    StatusRegistration = wait.until(EC.presence_of_element_located((By.XPATH, "//h4[contains(@class, 'pf-c-alert__title') and contains(text(), 'Verification email sent')]")))
    full_text = StatusRegistration.text
    verification_message = full_text.split('Info alert:')[1].strip()
    print("Status Registration:", verification_message)
    if verification_message == "Verification email sent":
        url = f"https://script.google.com/macros/s/AKfycbyxlCOsUmZ5kss43xpUseC7EsHxiFNHdILwr-lBPp_xowZF5Hgp82X3nSsdJe-EizB2Dw/exec?recipient={email}&value=REGISTERED"
    else:
        url = f"https://script.google.com/macros/s/AKfycbyxlCOsUmZ5kss43xpUseC7EsHxiFNHdILwr-lBPp_xowZF5Hgp82X3nSsdJe-EizB2Dw/exec?recipient={email}&value=FAILED"
    
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    print(f"For {email} --> Response: {response.text}")

    time.sleep(3)
    web.quit()
