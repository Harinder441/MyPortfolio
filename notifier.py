import smtplib


def send_mail(to_ad, massage,from_ad="harryautoemail@gmail.com", password="dgtkeudhnbowvhli"):
    with smtplib.SMTP("smtp.gmail.com") as con:
        # securing
        con.starttls()
        # login
        con.login(user=from_ad, password=password)
        con.sendmail(from_addr=from_ad, to_addrs=to_ad, msg=massage)


def msg_format(from_p="", to="", body="",subject=""):
    msg = f"Subject: {subject}\n\n{body}"
    return msg

if __name__ == "__main__":
    pass
