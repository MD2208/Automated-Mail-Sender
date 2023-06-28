import smtplib, random
import datetime as dt
import pandas
# Replace the login details below

MY_MAIL='sender@mail.com'
PASSWORD = "sender_password"

now = dt.datetime.now()
this_month = now.month
today = now.day

file = pandas.read_csv("birthdays.csv")
for index, row in file.iterrows():
    if int(row['month'])==this_month and int(row['day'])==today:
        name = row['name']
        reciever = row['email']
        letters = ['letter_1.txt','letter_2.txt','letter_3.txt']
        letter = random.choice(letters)
        with open(f"letter_templates/{letter}",mode='r') as draft:
            birthday_msg = draft.read().replace('[NAME]', name)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            # Dumyy data creates an error! Change login details. 
            connection.login(user=MY_MAIL,password=PASSWORD)
            connection.sendmail(
                from_addr=MY_MAIL,
                to_addrs=reciever,
                msg=f"Subject:Happy Birthday!\n\n{birthday_msg}"
            )



