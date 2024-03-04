# -*- coding: utf-8 -*-

import names

def main():
    startApplication("addressbook")
    startApplication("addressbook")
    sendEvent("QMoveEvent", waitForObject(names.address_Book_MainWindow), 61, 246, 459, 263)
    
    for appContext in applicationContextList():
        if appContext.isRunning:
            setApplicationContext(appContext)
            test.log("Interacting with application (pid: %d)" % appContext.pid)
            clickButton(waitForObject(names.address_Book_New_QToolButton))
            clickButton(waitForObject(names.address_Book_Add_QToolButton))
            type(waitForObject(names.forename_LineEdit), "John")
            type(waitForObject(names.forename_LineEdit), "<Tab>")
            type(waitForObject(names.surname_LineEdit), "Smith")
            type(waitForObject(names.surname_LineEdit), "<Tab>")
            type(waitForObject(names.email_LineEdit), "john@m.com")
            type(waitForObject(names.email_LineEdit), "<Tab>")
            type(waitForObject(names.phone_LineEdit), "123123")
            clickButton(waitForObject(names.address_Book_Add_OK_QPushButton))
            test.vp("VP1")