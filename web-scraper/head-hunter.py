from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.upwork.com/ab/account-security/login').text
soup = BeautifulSoup(html_text, 'lxml')

login = soup.find('div', class_ = 'up-form-group mb-20')

print(login)