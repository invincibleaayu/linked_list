import MySQLdb
import csv
import ssl
import smtplib                     #smtp is mail server and ssl is for security purpose
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="getinvolved")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()
# Use all the SQL you like
cur.execute("SELECT name,phoneNo,email FROM nepal_blood_getinvolved")
# print all the first cell of all the rows
dblist=cur.fetchall()
lastRow=dblist[-1]
print(lastRow[0],lastRow[1],lastRow[2])
with open("emailsend.csv","a",newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(lastRow[0:3])

with open("help.txt","r") as file:
    message=file.read().strip()
subject="BloodNepal ask you for your help now"
sameMessage='Subject: {}\n\n{}'.format(subject,message)
fromMail='bloodnepal22@gmail.com'
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login('bloodnepal22@gmail.com', 'teamsprit123')
    with open("emailsend.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, phoneNo, email in reader:
            server.sendmail(
                fromMail,
                email,
                sameMessage,
            )
