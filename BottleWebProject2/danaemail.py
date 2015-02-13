import smtplib

def sendit():
    textfile = "textfile.txt"

    fp = open("textfile.txt", 'rb')

    msg = fp.read()
    fp.close()

    me = "dana.freer@gmail.com"
    you = "dfreer@outlook.com"

    server = smtplib.SMTP('relay.plus.net', 25)
    
    server.ehlo()
    server.login("dfreer", "dana1504")
    text = msg
    server.sendmail(me, you, text)

