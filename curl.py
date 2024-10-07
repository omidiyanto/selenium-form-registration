import requests

email = "ookemidiyanto@infinitelearningstudent.id"
url = f"https://script.google.com/macros/s/AKfycbyxlCOsUmZ5kss43xpUseC7EsHxiFNHdILwr-lBPp_xowZF5Hgp82X3nSsdJe-EizB2Dw/exec?recipient={email}&value=REGISTERED"

response = requests.get(url)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
