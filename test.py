#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author TheLost

from send_Email import SendEmail

if __name__ == '__main__':
	send_test = SendEmail()
	send_to_list = ['the_losts@163.com', 'hacker_email@qq.com']
	
	send_test.send_Emails('Hacker', send_to_list, 'Hello', 'Work !')
