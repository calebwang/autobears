#!/usr/bin/python

import os
import re
import shutil
import mechanize
import auth

class telebears:

    def __init__(self):
        self.br = mechanize.Browser(factory = mechanize.RobustFactory())
        self.br.set_handle_robots(False)
        self.br.set_handle_refresh(False)
        
    def login(self):
        auther = auth.authenticator(self.br) 
        auther.prompt()
    
    def home(self):
        self.br.open('https://telebears.berkeley.edu')

    def pick_semester(self, sem, year=2013):
        """
        Pick a semester to register for.
        Valid choices:
            sp - Spring
            fa - Fall
            su - Summer
        Year is optional.
        """
        sem_dict = {'sp': 'Spring', 'fa': 'Fall', 'su': 'Summer'}
        self.home()
        self.follow_link(sem_dict(sem)) 
        
    
    def _showlinks(self):
        for link in self.br.links():
            print link

