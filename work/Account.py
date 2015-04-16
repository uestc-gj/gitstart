# -*- coding:utf-8 -*-

class User( object ):
    def __init__(self, name, password):
        self.username = name
        self.password = password

    def set_user_info(self, name, password):
        self.username = name
        self.password = password

    def get_user_info(self):
        return self.username , self.password

class Account( User ):
    '''
    username —— emailaddress(just like :alfred@163.com)
    password —— emailpassword(just like :alfred)
    sendserver —— emailserver
        we use smtp protocol for sending emails, so sendserver is just like :smtp.163.com)
    receiveserver —— emailserver(just like :alfred@163.com)
        we use pop3 protocol for receiving emails, so receiveserver is just like :pop.163.com)
    these info are used for login and authentication
    '''
    def __init__(self, name):
        '''
        initalize object from file info
        '''
        password = get_userpswd_from_file( name )
        User.__init__(self, name, password)
        
        server = self.username.split('@')
        self.sendserver = "smtp."+server[1]
        self.receiveserver = "pop."+server[1]

    def get_user_info(self):
        return self.username , self.password, self.sendserver, self.receiveserver

'''
Account file manager
'''
def save_an_account( username, password):
    if not check_username(username):#if exist, refuse save
        print "Your account has already exist, don't regist again!"
    else:
        list_of_text_strings = "account:" + username + "\n" + password + "\n" + "\n"
        filename = "./Accounts.txt"
        file_object = open(filename, 'a')
        file_object.writelines(list_of_text_strings)
        file_object.close( )

def remove_an_account( name ):
    filename = "./Accounts.txt"
    file_object = open(filename, 'r')
    #content is a list
    content = file_object.readlines()
    for line in content:
        username = line.split(':',1)
        if username[0] == "account":
            if username[1].strip() == name:
                index = content.index(line)
                content.pop(index)#delete username
                content.pop(index)#delete password
                break
    file_object.close( )

    file_object = open(filename, 'w')
    file_object.writelines(content)
    file_object.close()

def check_username( name ):
    '''
    read file and check duplicate emailaddress
    return False means already exists, True means not.
    '''
    fh = open('./Accounts.txt')
    for line in fh.readlines():
        username = line.split(':',1)
        if username[0] == "account":
            checkname = username[1].strip()
            if checkname == name :#exist
                fh.close()
                return False
    fh.close()
    return True

def get_userpswd_from_file( name ):
    '''
    read file and get password from file
    return password if already exists, False means account not exists.
    '''
    fh = open('./Accounts.txt')
    password = None
    content = fh.readlines()
    for line in content:
        username = line.split(':',1)
        if username[0] == "account":
            checkname = username[1].strip()
            if checkname == name :#exist,checkname is username
                password = content[content.index(line)+1]#the next line of username
                password = password.strip()
                fh.close()
                return password
    if password == None:
        print "Your account is not exist, please regist!"
        return False

