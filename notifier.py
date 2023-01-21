import smtplib
from dotenv import load_dotenv
import os

load_dotenv()


def send_mail(to_ad, massage, from_ad=os.environ.get("FROM_EMAIL"), password=os.environ.get("FROM_EMAIL_PASS")):
    with smtplib.SMTP("smtp.gmail.com") as con:
        # securing
        con.starttls()
        # login
        con.login(user=from_ad, password=password)
        con.sendmail(from_addr=from_ad, to_addrs=to_ad, msg=massage)


def msg_format(from_p="", to="", body="", subject=""):
    msg = f"Subject: {subject}\n\n{body}"
    return msg


if __name__ == "__main__":
    # send_mail(to_ad=os.environ.get("TO_EMAIL"), massage="hello1")
    pass
