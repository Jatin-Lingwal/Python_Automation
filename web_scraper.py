import requests # For https req
from email.mime.multipart import MIMEMultipart # Email body
from email.mime.text import MIMEText # Email body
from bs4 import BeautifulSoup # For scraping
import smtplib # For sending email
import datetime

updated_time = datetime.datetime.now()
body = '' # email content

def news(url):
    print('Extracting news from hacker news stories........')
    cnt = '' #it is used to assign value to Golbal var = body
    cnt += ('<b>HN TOP Stories:</b>\n'+'<br>'+'-'*50+'<br>') # cnt += --> cnt = cnt + ("")
    response = requests.get(url)
    content = response.content # storing content of web page
    soup = BeautifulSoup(content, 'html.parser')
    for i,tags in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})): # where looking for td where class and title is there. valign is empty coz to eleminate junk.
          cnt += F'{str(i+1)}--->>>>{tags.text}\n <br>'

    return cnt

result = news('https://news.ycombinator.com/')
body += result
body += ("For more please let us know!")
body += ('<br>----------------<br>')
body += ('<br<br>END OF MESSAGE.......')



print('Composing Email...')

# Email details
Server = 'smtp.gmail.com'
Port = 587
From = '' #can your account and make sure to disable (your account ---> security -->Less secure app access!)
To = '' # can provide multiple accounts in a list
Pass = '&!(@^#(*)@^#@()&*@#!()#&'

Message = MIMEMultipart() # empty object, message body

Message['Subject'] = F'Top News in town from HACKER NEWS [Automated Email] @ {str(updated_time.day) }-{str(updated_time.month)}-{str(updated_time.year) } '
Message['From'] = From
Message['To'] = To

Message.attach(MIMEText(body, 'html')) # attaching email body & html is for making email in html format like we have used <br>, <b>

print('Initializing server..')

s = smtplib.SMTP(Server, Port)
s.set_debuglevel(1) # If the server has issue in connecting so , it through an error by providing '0' no error.
s.ehlo() # to initiate the server
s.starttls() # for connection using tls
s.login(From, Pass)
s.sendmail(From, To, Message.as_string())

print('email sent....')
s.quit()






