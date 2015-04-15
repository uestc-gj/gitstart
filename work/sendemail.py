# -*- coding: utf-8 -*-
#!/usr/bin/python

import smtplib
from Account import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
'''
Test data


username = "916311350@qq.com"
password = "shuigaojian"

SERVER = 'smtp.qq.com'
sender = root.username
receivers = ['linjiangxiangj@sina.cn']

SUBJECT = u'测试UTF8编码'
TEXT = u'ABCDEFG一二三四五六七'
'''
def email_pack(sender, receivers, SUBJECT, TEXT):
    print "packing...\n"
    msg = MIMEMultipart('alternative')
    # 注意包含了非ASCII字符，需要使用unicode
    msg['Subject'] = SUBJECT
    msg['From'] = sender
    msg['To'] = ', '.join(receivers)
    part = MIMEText(TEXT, 'plain', 'utf-8')
    msg.attach(part)
    return msg

def email_send(user, receivers, SUBJECT, TEXT):
    try:
        sender = user.username
        #authentication
        server = smtplib.SMTP_SSL()
        server.connect(user.sendserver)
        server.login(user.username,user.password)

        #make prepare content
        msg = email_pack(sender, receivers, SUBJECT, TEXT)
        server.sendmail(sender, receivers, msg.as_string())#.encode('ascii'))        
        print "Successfully send email\n"
        server.quit()
        return True
    except Exception, e:
        print str(e)
        print "Error: unable to send email\n"
        return False

def email_verification( username, password ):
    '''
    :param username:
    :param password:
    :return:False:invalid address
            True: valid address
    '''
    try:
        server = username.split('@')
        sendserver = "smtp."+server[1]
        #authentication
        server = smtplib.SMTP_SSL()
        server.connect(sendserver)
        server.login(username, password)

        return True
    except Exception, e:
        print str(e)
        print "Error: invalid email address\n"
        return False

if __name__ == "__main__":
    print "This is my mail send box\n"
    #prepare data info
    root = Account("916311350@qq.com")
    receivers = ['linjiangxiangj@sina.cn']
    SUBJECT = u'测试UTF8编码'
    TEXT = u'ABCDEFG一二三四五六七'
    #call send func
    #email_send(root, receivers, SUBJECT, TEXT)
