# -*- coding: UTF-8 -*-
'''
import os
from gi.repository import Gtk,Pango
import email
import poplib

    def parse_mail(self, file):
        fp = open(file, "r")
        msg = email.message_from_file(fp) # 直接文件创建message对象，这个时候也会做初步的解码
        mail_subject = msg.get("subject") # 取信件头里的subject,　也就是主题
        # 下面的三行代码只是为了解码象=?gbk?Q?=CF=E0=C6=AC?=这样的subject
        try:
            h = email.Header.Header(mail_subject)
            dh = email.Header.decode_header(h)
            mail_subject = dh[0][0]
        except UnicodeDecodeError:
            mail_subject = mail_subject.decode('gb2312')
 
        mail_from =  email.utils.parseaddr(msg.get("from"))[1] # 取from
        mail_to = email.utils.parseaddr(msg.get("to"))[1] # 取to
 
        for par in msg.walk():
            if not par.is_multipart(): # 这里要判断是否是multipart，是的话，里面的数据是无用的，至于为什么可以了解mime相关知识。
                name = par.get_param("name") #如果是附件，这里就会取出附件的文件名
                if name:
                    #有附件
                    # 下面的三行代码只是为了解码象=?gbk?Q?=CF=E0=C6=AC.rar?=这样的文件名
                    h = email.Header.Header(name)
                    dh = email.Header.decode_header(h)
                    fname = dh[0][0]
                    print '附件名:', fname
                    data = par.get_payload(decode=True) #　解码出附件数据，然后存储到文件中
                    
                    try:
                        f = open(fname, 'wb') #注意一定要用wb来打开文件，因为附件一般都是二进制文件
                    except:
                        print '附件名有非法字符，自动换一个'
                        f = open('aaaa', 'wb')
                    f.write(data)
                    f.close()
                else:
                    #不是附件，是文本内容
                    mail_content = par.get_payload(decode=True) # 解码出文本内容，直接输出来就可以了。
                    break
                
        try:
            mail_subject = mail_subject.decode('gb2312')
        except UnicodeDecodeError:
            pass
 
        try:
            mail_from = mail_from.decode('gb2312')
        except UnicodeDecodeError:
            pass
 
        try:
            mail_to = mail_to.decode('gb2312')
        except UnicodeDecodeError:
            pass
 
        try:
            mail_content = mail_content.decode('gb2312')
        except UnicodeDecodeError:
            pass
 
        self.textbuffer.delete(self.textbuffer.get_start_iter(), self.textbuffer.get_end_iter())
        iter = self.textbuffer.get_iter_at_offset(0)
        self.textbuffer.insert_with_tags_by_name(iter, "标题：", "big")
        self.textbuffer.insert(iter, "%s\n" % mail_subject)
        self.textbuffer.insert_with_tags_by_name(iter, "发件人：", "big")
        self.textbuffer.insert(iter, "%s\n" % mail_from)
        self.textbuffer.insert_with_tags_by_name(iter, "收件人：", "big")
        self.textbuffer.insert(iter, "%s\n\n" % mail_to)
        self.textbuffer.insert_with_tags_by_name(iter, "正文：", "big")
        self.textbuffer.insert(iter, "\n%s" % mail_content)
 
        fp.close()
'''

import poplib
import email
import cStringIO
import base64
import os
def showMessage( msg ):
    if msg.is_multipart():
        for part in msg.get_payload():
            showMessage( part )
    else:
        types = msg.get_content_type()
        if types=='text/plain':
            try:
               body =msg.get_payload(decode=True)
               print body
            except:
               print '[*001*]BLANK'
        elif types=='text/base64':
            try:
               body = base64.decodestring(msg.get_payload())
               print body
            except:
               print '[*001*]BLANK'
               
def PareMessageAttachMent( msg ):
    path = "E:/email/"
    for part in msg.walk():
        contenttype = part.get_content_type()
        filename = part.get_filename()
        if filename==None:
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


server   = 'pop.sina.cn'
username = 'linjiangxiangj@sina.cn'
password = 'gaojian'
try:  
    p=poplib.POP3(server)  
    p.user(username)  
    p.pass_(password)  
    totalNum, totalSize = p.stat() #返回一个元组:(邮件数,邮件尺寸)
    print "Login success"
    print "totalNum, totalSize:",totalNum, totalSize,"\n"
    for i in range(totalNum, totalNum-5, -1):
        print "\nThis is No.%d email,and content is:" % i
        m = p.retr(i)
        buf = cStringIO.StringIO()
        for j in m[1]:
            print >>buf,j
        buf.seek(0)

        # 形成mail message对象
        msg = email.message_from_file( buf )
        # 取出邮件中基本属性数据
        subject = email.Header.decode_header(msg['subject'])[0][0]
        subcode =email.Header.decode_header(msg['subject'])[0][1]
        sender = email.Header.decode_header(msg['From'])[0][0]
        receiver = email.Header.decode_header(msg['To'])[0][0]

        PareMessageAttachMent( msg )
        showMessage( msg )
        #p.retr('邮件号码')方法返回一个元组:(状态信息,邮件,邮件尺寸)    
except poplib.error_proto,e:  
    print "Login failed:",e  
    sys.exit(1)

#if __name__ == "__main__":
