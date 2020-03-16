import smtplib
import functions
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendHtmlMail(content):
    gmail_user = "siemprepe@gmail.com"
    gmail_password = "ifosvnutoqrqmzan"
    # me == my email address
    # you == recipient's email address
    me = "siemprepe@gmail.com"
    you = "siemprepe@gmail.com"

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Gamescraper results " + functions.getToday()
    msg['From'] = me
    msg['To'] = you

    # Create the body of the message (a plain-text and an HTML version).
    text = content
    html = content

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.ehlo()
    s.login(gmail_user, gmail_password)
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(me, you, msg.as_string())
    s.quit()

def sendMail(content):
    gmail_user = "siemprepe@gmail.com"
    gmail_password = "ifosvnutoqrqmzan"

    sent_from = gmail_user
    to = ["siemprepe@gmail.com"]
    subject = "Game summary for " + functions.getToday()
    body = content.encode("utf-8")

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print ('Email sent!')
    except:
        print ('Something went wrong...')