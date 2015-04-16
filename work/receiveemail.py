# -*- coding: UTF-8 -*-

import poplib
import email
from Account import *
import cStringIO
import base64
import os

def get_content( msg ):
    if msg.is_multipart():
        contentstr = ""
        for part in msg.get_payload():
            content = get_content( part)
            #print content
            contentstr += content
        return contentstr
    else:
        types = msg.get_content_type()
        body = ""
        if types=='text/plain':
            try:
               body = msg.get_payload(decode=True)
               #print body
            except:
               print '[*001*]BLANK'
        elif types=='text/base64':
            try:
               body = base64.decodestring(msg.get_payload())
               #print body
            except:
               print '[*001*]BLANK'
        return body

def get_attachment( msg ):
    path = "E:/email/"
    for part in msg.walk():
        contenttype = part.get_content_type()
        filename = part.get_filename()
        if filename == None:
            continue
        filename = email.Header.decode_header(filename)[0][0]
        filename = os.path.split(filename)[1]
        # 防止文件名出现全路径错误
        #print filename

        ###解析邮件的附件内容
        fn = path+filename
        if os.path.exists(fn)==False:
            f=open(fn,'wb')
            try:
                f.write(base64.decodestring(part.get_payload()))
            except:
                pass
            f.close()
        else:
            continue

'''
Test data

server   = 'pop.sina.cn'
username = 'linjiangxiangj@sina.cn'
password = 'gaojian'
'''
def email_get( user ,recentnumber = 10):
    '''
    method for showing recent n messages,with input value of account and
    recentnumber shows the number of messages you want
    '''
    email_list = list()
    try:  
        p=poplib.POP3(user.receiveserver)  
        p.user(user.username)
        p.pass_(user.password)
        totalNum, totalSize = p.stat() #返回一个元组:(邮件数,邮件尺寸)
        #print "Login success"
        #print "totalNum, totalSize:",totalNum, totalSize,"\n"
        for i in range(totalNum, totalNum-recentnumber, -1):
            print "\nThis is No.%d email,and content is:" % i
            #p.retr('邮件号码')方法返回一个元组:(状态信息,邮件,邮件尺寸)
            m = p.retr(i)
            buf = cStringIO.StringIO()
            for j in m[1]:
                print >>buf,j
            buf.seek(0)

            # 形成mail message对象
            msg = email.message_from_file( buf )
            # 取出邮件中基本属性数据,待处理
            messagelist = list()
            subject = email.Header.decode_header(msg['subject'])[0][0]
            #subcode = email.Header.decode_header(msg['subject'])[0][1]
            sender = email.Header.decode_header(msg['From'])[0][0]
            receiver = email.Header.decode_header(msg['To'])[0][0]
            content = get_content( msg )

            messagelist.append(subject)
            #messagelist.append(subcode)
            messagelist.append(sender)
            messagelist.append(receiver)
            messagelist.append(content)

            email_list.append(messagelist)
            #print messagelist[4]

            #get_attachment( msg )
        return email_list

    except poplib.error_proto,e:  
        print "Login failed:",e  
        return False

if __name__ == "__main__":
    print "This is my mail receive box\n"
    #prepare data info
    root = Account("linjiangxiangj@sina.cn")

    #call receive func
    email_get(root, 4)
