#!/usr/bin/python
#-*- coding: utf-8 -*-

# This is a class of sendmail
# Author: Ryan 2013-11-04

from smtplib import SMTP
from email.MIMEText import MIMEText as mimetext
from email.MIMEMultipart import MIMEMultipart as mimemultipart
from email.MIMEBase import MIMEBase as mimebase


class Connectsmtp(object):
    """"""
    fromaddr = "dyw564@gmail.com"
    toaddr = "ryan@deliveryherochina.com"
    username = "dyw564@gmail.com"
    password = "xxxxxxx"
    subject = "Send email and attachment"
    smtpser = "smtp.gmail.com:587"

    def __init__(self):
        self.smtp = SMTP(self.smtpser)
        self.smtp.starttls()
        self.smtp.login(self.username, self.password)

    def sendit(self, cont, att, attname):
        self.msg = mimemultipart()
        self.content = mimetext(cont, "plain", "utf-8")
        self.msg.attach(self.content)
        self.attachment = mimebase('application', 'octet-stream')
        self.attachment.set_payload(att)
        self.attachment.add_header('Content-Disposition', 'attachment; filename="%s"' % attname)
        self.msg.attach(self.attachment)
        self.msg["subject"] = self.subject
        self.smtp.sendmail(self.fromaddr, self.toaddr, self.msg.as_string())
        return True

    def __del__(self):
        self.smtp.quit()

# Lets test it
msg = "test content"
att = "test attachment"
attn = "attname"
con = Connectsmtp()

if con:
    print "Connectsmtp and login"
    if con.sendit(msg, att, attn):
        print "Send mail!"
    else:
        print "Fail sendit"
else:
    print "Fail con"
