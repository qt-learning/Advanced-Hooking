# -*- coding: utf-8 -*-

import names

def main():
    startApplication("addressbook")
    
    clickButton(waitForObject(names.address_Book_New_QToolButton))
    
    for i in range(5):
        clickButton(waitForObject(names.address_Book_Add_QToolButton))
        type(waitForObject(names.forename_LineEdit), "John")
        type(waitForObject(names.forename_LineEdit), "<Tab>")
        type(waitForObject(names.surname_LineEdit), "Smith")
        type(waitForObject(names.surname_LineEdit), "<Tab>")
        type(waitForObject(names.email_LineEdit), "john@m.com")
        type(waitForObject(names.email_LineEdit), "<Tab>")
        type(waitForObject(names.phone_LineEdit), "123123")
        type(waitForObject(names.phone_LineEdit), "<Return>")