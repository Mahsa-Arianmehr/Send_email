import smtplib, ssl 
from getpass import getpass
import _mysql_connector

mydb = _mysql_connector.connect(
    host = "local host" 
    user = "root"
    password = "Mahs@1374"
    database = "emaillist"
    table = "emaillist"
)
mycursor = mydb.coursor()
mycursor.execute(" selesct * from emaillist")
rs = mycursor.fetchall()
# mycursor.execute("Creat database my database')


smtp_server = 'smtp.gmail.com'
port = 465

sender_email = 'mahsaarianmehr1374@gmail.com'
password = getpass(prompt= "enter your password:")

while person_id != null:
    receiver_email = "email" 

message = '''\
subject: test
this message sent from python!
'''

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message )