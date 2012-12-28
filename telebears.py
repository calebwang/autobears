#!/usr/bin/python

import os
import re
import shutil
from mechanize import Browser
import auth
from getpass import getpass

class telebears:
    def __init__(self):
        self.br = Browser(factory = mechanize.RobustFactory())
        self.br.set_handle_robots(False)
        self.br.set_handle_refresh(False)
        
    def login(self):
        user = raw_input('username: ')
        password = getpass('password: ')
        authenticator = auth.authenticator(self.br) 
        authenticator.authenticate('https://telebears.berkley.edu', user, password)
        
    
