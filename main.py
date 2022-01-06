from datetime import datetime
import pandas
import random
import smtplib

SMTP = "smtp.yopmail.com"
FROM_EMAIL = "enter your email here"
PASSWORD = "enter your password here"
TO_EMAIL = "enter email to send"

# got today date
today = (datetime.month, datetime.day)

# read all birthday details
bdays = pandas.read_csv("birthdays.csv")

# created bday dict
birthdays = {(bday["month"], bday["day"]): bday for (index, bday) in bdays.iterrows()}

print(birthdays)
# find if today is any bday
if today in birthdays:

    # get today bday detail
    person = birthdays[today]

    # get name of bday person
    name = person["name"]

    # pick random  bday wishes
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter:
        contents = letter.read()
        # replace PLACE_HOLDER with real name
        contents = contents.replace("[NAME]", name)

    with smtplib.SMTP(SMTP) as connection:
        connection.starttls()
        connection.login(FROM_EMAIL, PASSWORD)
        # SEND mail
        connection.sendmail(from_addr=FROM_EMAIL, to_addrs=TO_EMAIL, msg=f"Subject:Happy birthday {name}\n\n{connection}")





