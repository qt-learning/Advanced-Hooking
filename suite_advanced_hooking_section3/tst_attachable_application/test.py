# -*- coding: utf-8 -*-

import names

def main():
    #Application must be started from a command-line tool:
    #SQUISHDIR\bin>startaut --port={port} {path to aut}
    #e.g.: %SQUISHDIR%\bin\startaut --port=8081 %SQUISHDIR%\examples\qt\addressbook\addressbook.exe
    
    app = attachToApplication("addressBookAtt")
    test.log("%s has been attached with id %d on port %d with host %s" % (app.name, app.pid, app.port, app.host))
    if (waitForObjectExists(names.address_Book_Add_QToolButton).enabled == False):
        clickButton(waitForObject(names.address_Book_New_QToolButton))
    
    for i in range(5):
        if not app.isRunning:
            app = attachToApplication("addressBookAtt")
            test.log("%s has been attached with id %d on port %d with host %s" % (app.name, app.pid, app.port, app.host))
        clickButton(waitForObject(names.address_Book_Add_QToolButton))
        type(waitForObject(names.forename_LineEdit), "John")
        type(waitForObject(names.forename_LineEdit), "<Tab>")
        type(waitForObject(names.surname_LineEdit), "Smith")
        type(waitForObject(names.surname_LineEdit), "<Tab>")
        type(waitForObject(names.email_LineEdit), "john@m.com")
        type(waitForObject(names.email_LineEdit), "<Tab>")
        type(waitForObject(names.phone_LineEdit), "123123")
        type(waitForObject(names.phone_LineEdit), "<Return>")
        pid = app.pid
        app.detach()
        test.log("Squish detached from app with id %d" % (pid))
