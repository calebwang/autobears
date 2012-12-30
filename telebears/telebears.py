#!/usr/bin/python

import mechanize
import auth

class RegistrationError(Exception):
    def __init__(self, value = ''):
        self.value = value

    def __str__(self):
        return str(self.value)

class Telebears:

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

    def add_class(self, ccn, dl, for_grade = True, units = None, code = None):
        """
        Parameters
        ---------
            ccn:
                course control number
                five digit string or int e.g. 12345
            dl:
                pick discussion, lab
                tuple e.g. (12346, 12347)
                or (12346, None) if no lab or lab/discussion grouped together
                or (None, 12347) if no discussion
            for_grade:
                is the class for a grade?
            units:
                for variable unit classes
            code:
                class entry code
        """

        self.semester_home()
        link = self.br.find_link(text = 'Add Class')
        self.br.follow_link(link)
        self.handle_class_dialogue(ccn, for_grade, units, code)
        self.handle_discussion_dialogue(dl[0])
        self.handle_lab_dialogue(dl[1])
        self.confirm()

    def waitlist(self, ccn, dl, for_grade = True, units = None, code = None)
        """
        see docstring for add_class 
        """
        self.semester_home()
        link = self.br.find_link(text = 'Add Class')
        self.br.follow_link(link)
        self.handle_class_dialogue(ccn, for_grade, units, code)
        self.handle_discussion_dialogue(dl[0])
        self.handle_lab_dialogue(dl[1])
        self.confirm()

    def handle_class_dialogue(self, ccn, for_grade, units, code)
        self.br.select_form(nr=0)
        self.br['_InField1'] = str(ccn)
        if not for_grade:
            self.br['_InField2'] = str(2)
        if units:
            self.br['_InField3'] = str(units)
        if code:
            self.br['_InField4'] = str(code)
        self.br.submit()
        if not self.check_success():
            raise RegistrationError("Error")

    def handle_discussion_dialogue(self, section):
        if not section:
            return
        self.br.select_form(nr=0)
        #stuff goes here 
        self.br.submit() 
        if not self.check_success():
            raise RegistrationError("Error")

    def handle_lab_dialogue(self, section):
        if not section:
            return
        self.br.select_form(nr=0)
        #stuff goes here
        self.br.submit()
        if not self.check_success():
            raise RegistrationError("Error")

    def switch_sections(self, lec_ccn, sec_ccn):
        """
        Parameters
        ---------
            lec_ccn:
                ccn of lecture
            sec_ccn:
                ccn of section you want to switch into
        """
        self.semester_home()
        link = self.br.find_link(text = 'Switch Sections')
        self.br.follow_link(link)
        self.br.select_form(nr=0)
        self.br['_InField'] = str(lec_ccn)
        self.br.submit()
        self.br['_InField'] = str(sec_ccn)
        self.br.submit()
        self.confirm()

    def check_success(self):
        """regex for error messages"""
        return False

    def confirm(self):
        self.br.select_form(nr=0)
        self.br.submit()

    def _links(self):
        for link in self.br.links():
            print link

    def _forms(self):
        for form in self.br.forms():
            print form

