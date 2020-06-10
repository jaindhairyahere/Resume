from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import logging
# url = "https://www.iima.ac.in/web/faculty/faculty-profiles/rakesh-basant"
logging.basicConfig(level = logging.INFO,filename='contact_push.log')

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheets = client.open("Contacting")
sheet = sheets.sheet1
        

names = []
emails = []
phones= []
websites = []
departments = []

'''IIM INDORE'''
# response = requests.get(url)
# soup = BeautifulSoup(response.text, features='html.parser')
# // IIT Indore
# name_class = soup.find_all('div', {'class': 'box-card-header'})
# email_class = soup.find_all('p', {'class': 'p-14x'})
# i= 0

# for name_objects in name_class:
#     for name in name_objects.find_all('h3'):
#         names.append(name.text)
# for email_objects in email_class:
#     i +=1
#     if i % 2 == 0:
#         phones.append(email_objects.text[:-6])
#     for email in email_objects.find_all('a'):
#         emails.append(email['href'][7:])

# for i in range(13):
#     sheet.append_row([names[i],emails[i],phones[i]]) 

'''IIM AHMEDABAD'''
# f = open("emails.txt", "r")
# urls = f.readlines()
# urls = urls[0].split(",")
# for url in urls[10:]:
#     f = []
#     url = url[1:-1]
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, features='html.parser')
#     name_class = soup.select_one('div.tab-inr-box-right h1')
#     department = soup.select_one('div.tab-inr-box-right >h3')
#     left = soup.select('div.tab-inr-box-left a[href]')
#     ph = soup.select('div.tab-inr-box-left p:nth-child(3)')
#     try:
#         n = name_class.text.strip()
#     except:
#         n = ""
#     try:
#         p = ph[0].text.strip()
#     except:
#          p = ""
#     try:
#         e = left[0].text
#     except:
#         e = ""
#     try:
#         w = left[1].text
#     except:
#         w = ""
#     try:
#         d = department.text
#     except:
#         d = ""      
#     sheet.append_row([n, e, p, w, d])
#     logging.info("Inserted in sheet : {} {} {} {} {}".format(n, e, p, w, d))
print("Job done")
