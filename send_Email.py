#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author TheLost

'''
发送简单文本邮件
'''
import smtplib
import config
from email.mime.text import MIMEText

class SendEmail:

    def send_Emails(self, from_name, to_list, sub, content):
        me = from_name + '<' + config.mail_user + '@' + config.mail_postfix + '.com' + '>'
        msg = MIMEText(content, _subtype = 'plain', _charset = 'utf-8')
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = ";".join(to_list)

        try:
            server = smtplib.SMTP()
            server.connect(config.mail_host)
            server.login(config.mail_user, config.mail_pass)
            server.sendmail(me, to_list, msg.as_string())
            server.close()
            return True
        except Exception, e:
            print str(e)
            return False

if __name__ == '__main__':

    mailto_list = ['hacker_email@qq.com']
    result = SendEmail().send_Emails('TheLost', mailto_list, 'Hello', 'Hi, nice to meet you!')
