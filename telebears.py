#!/usr/bin/python

import mechanize
import auth

class telebears:

    def __init__(self):
        self.br = mechanize.Browser(factory = mechanize.RobustFactory())
        self.br.set_handle_robots(False)
        self.br.set_handle_refresh(False)
        self.sem = None
        self.year = None
        self.sem_dict = {'sp': 'Spring', 'fa': 'Fall', 'su': 'Summer'}
        
    def login(self):
        auther = auth.authenticator(self.br) 
        auther.prompt('https://telebears.berkeley.edu')
 
    def logout(self):
        self.home()
        link = self.br.find_link(text='Logout')
        self.br.follow_link(link)   

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
        self.sem = sem
        self.year = year
        self.semester_home()

    def semester_prompt(self):
        sem = raw_input('Semester: ')
        year = raw_input('Year: ')
        self.pick_semester(sem, year)
        
    def semester_home(self):
        if self.sem == None:
            self.semester_prompt()
        else:
            self.home()
            link = self.br.find_link(text_regex=self.sem_dict[self.sem] + ' ' + str(self.year)) 
            self.br.follow_link(link)

    def add_class(self, ccn, for_grade = True, units = None, code = None):
        self.semester_home()
        link = self.br.find_link(text = 'Add Class')
        self.br.follow_link(link)
        self.br.select_form(nr=0)
        self.br['_InField1'] = str(ccn)
        if not for_grade:
            self.br['_InField2'] = str(2)
        if units:
            self.br['_InField3'] = str(units)
        if code:
            self.br['_InField4'] = str(code)
        self.br.submit()
        #need to handle discussion selection
        self.confirm()

    def switch_sections(self, lec_ccn, sec_ccn):
        self.semester_home()
        link = self.br.find_link(text = 'Switch Sections')
        self.br.follow_link(link)
        self.br.select_form(nr=0)
        self.br['_InField'] = str(lec_ccn)
        self.br.submit()
        self.br['_InField'] = str(sec_ccn)
        self.br.submit()
        self.confirm()

    def confirm(self):
        self.br.select_form(nr=0)
        self.br.submit()

    def _links(self):
        for link in self.br.links():
            print link

    def _forms(self):
        for form in self.br.forms():
            print form

