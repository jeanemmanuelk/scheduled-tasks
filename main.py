# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

# 2. Check if today matches a birthday in the birthdays.csv
bd_file = pd.read_csv("birthdays.csv").to_dict("records")
now = dt.datetime.now()
for bd in bd_file:
    bd_month = int(bd["month"])
    bd_day = int(bd["day"])
    bd_name = bd["name"]
    bd_email = bd["email"]
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    if bd_month == now.month and bd_day == now.day:
        # 4. Send the letter generated in step 3 to that person's email address.
        # selecting and interacting with a random letter
        # folder_path = 'letter_templates'
        # file_pattern = '*.txt'
        # letters = glob.glob(os.path.join(folder_path, file_pattern)) #get all .txt letters files
        # random_letter = random.choice(letters) # select random letter file

        #method 2 to get a random file
        file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

        # open and update the letter
        with open(file_path, 'r') as f:
            content = f.read() # get letter content as a list
            content = content.replace('[NAME]',f'{bd_name}') #replace the name

        # send the updated letter content to the person's email address
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=bd_email,
                                msg=f"Subject:Happy Birthday!\n\n{content}")
