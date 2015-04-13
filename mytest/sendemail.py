# -*- coding: utf-8 -*-
#!/usr/bin/python

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
'''
Test data
'''
username = "916311350"
password = "shuigaojian"

SERVER = 'smtp.qq.com'
sender = '916311350@qq.com'
receivers = ['linjiangxiangj@sina.cn']

SUBJECT = u'测试UTF8编码'
TEXT = u'ABCDEFG一二三四五六七'

def email_pack(SUBJECT, TEXT, sender, receivers):
    print "packing...\n"
    msg = MIMEMultipart('alternative')
    # 注意包含了非ASCII字符，需要使用unicode
    msg['Subject'] = SUBJECT
    msg['From'] = sender
    msg['To'] = ', '.join(receivers)
    part = MIMEText(TEXT, 'plain', 'utf-8')
    msg.attach(part)
    return msg

def email_send(SERVER):
    try:
        server = smtplib.SMTP_SSL()
        server.connect(SERVER)
        server.login(username,password)
        msg = email_pack(SUBJECT, TEXT, sender, receivers)
        server.sendmail(sender, receivers, msg.as_string())#.encode('ascii'))         
        print "Successfully sent email\n"
        server.quit()
    except Exception, e:
        print str(e)
        print "Error: unable to send email\n"

if __name__ == "__main__":
    print "This is my mail send box\n"
    email_send(SERVER)
