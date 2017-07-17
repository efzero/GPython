import urllib3
import re
from bs4 import BeautifulSoup
import requests
import json
import time
import smtplib
import random



url='https://courses.illinois.edu/schedule/2017/fall/CS/225'
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6','Cache-Control':'max-age=0','Connection':'keep-alive','Cookie':'__utma=44258684.185246010.1497327305.1498358117.1499550382.3; __utmz=44258684.1498358117.2.2.utmcsr=isss.illinois.edu|utmccn=(referral)|utmcmd=referral|utmcct=/students/employment/f1cpt.html; __unam=bd29ceb-15cb42a1a8f-127de5df-26; JSESSIONID=39DE2DDDED2C8DE96DBAF54304083DC2; _ga=GA1.2.185246010.1497327305; _gid=GA1.2.648699230.1500139865','Host':'courses.illinois.edu','Referer':'https://courses.illinois.edu/schedule/2017/fall/CS','User-Agent' :'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36'}

s = requests.Session()

def sendemail(sub,msg):
    gmail_user = 'tripofsea@gmail.com'
    gmail_password = '918000aA'

    sent_from = gmail_user
    to = ['dchen48@illinois.edu','math441ishard@gmail.com']
    subject = 'CS225 is available'+sub
    body = msg
    email_text = '\r\n'.join([
        'From: %s' % sent_from,
        'To: %s' % ', '.join(to),
        'Subject: %s' % subject,
        '',  # Blank line to signal end of headers
        body
    ])

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')
count = 0

while True:
    response = s.get(url, headers=headers)
    soup = BeautifulSoup(response.content,'html.parser')
    scripts = soup.find_all("script")[2].string
    scripts = str(scripts)
    pattern = re.compile('var sectionDataObj = (.*?);')
    data = pattern.search(scripts)
    courses = json.loads(data.groups()[0])
    print (count)
    count += 1
    print("the first section is :",courses[0]['availability'])
    print("the second section is :", courses[1]['availability'])
    print("please register at https://eas.admin.uillinois.edu/eas/servlet/EasLogin?redirect=https://webprod.admin.uillinois.edu/ssa/servlet/SelfServiceLogin?appName=edu.uillinois.aits.SelfServiceLogin&dad=BANPROD1")

    msg = 'the 11:00 am section is '+ courses[0]['availability']+'\n\n' + 'the 2:00 pm section is '+ courses[1]['availability'] + "please register at https://eas.admin.uillinois.edu/eas/servlet/EasLogin?redirect=https://webprod.admin.uillinois.edu/ssa/servlet/SelfServiceLogin?appName=edu.uillinois.aits.SelfServiceLogin&dad=BANPROD1"
    sub = str(random.randint(1,100))
    if courses[0]['availability'] == 'Closed' or courses[1]['availability'] == 'Closed':
        sendemail(sub,msg)
    time.sleep(60)
