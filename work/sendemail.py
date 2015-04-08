#!/usr/bin/env python
# -*- coding: utf-8 -*-
#导入smtplib和MIMEText

import smtplib
from email.mime.text import MIMEText
'''
要发给谁，这里发给2个人
'''
mailto_list=["winson.zhou@gmail.com","122167504@qq.com"]
'''
设置服务器，用户名、口令以及邮箱的后缀
'''
mail_host="smtp.126.com"
mail_user="lvs071103"
mail_pass="*************"
mail_postfix="126.com"
'''
-----------------initial finished-------------------
'''
def send_mail(to_list,sub,content):
    '''
    to_list:发给谁
    sub:主题
    content:内容
    send_mail("lvs071103@126.com","sub","content")
    '''
    address=mail_user+"&lt;"+mail_user+"@"+mail_postfix+"&gt;"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = address
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(address, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    if send_mail(mailto_list,"测试","这是一个测试邮件，将来会被用作程序的邮件警报"):
        print "发送成功"
    else:
        print "发送失败"
