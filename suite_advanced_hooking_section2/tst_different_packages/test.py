# -*- coding: utf-8 -*-

import names
import os

def main():
    #AUTs name to use
    qt65AutName = "addressbook"
    qt515AutName = "paymentform"
    
    #Paths to the Squish installation
    qt65Package = r"C:\Squish\Squish_for_Qt65x_7_2_0"
    qt515Package = r"C:\Squish\Squish_for_Qt515x_7_2_0"
    
    #Ports and hosts to use
    qt65Host = "localhost"
    qt515Host = "localhost" 
    qt65Port = 4327
    qt515Port = 4328
       
    #Starting the servers via the command line
    #SQUISHDIR/bin/squishserver --port=qt65Port --host=qt65Host
    #SQUISHDIR/bin/squishserver --port=qt515Port --host=qt515Host
    
    #Starting the Qt 6.5 app
    os.environ["SQUISH_PREFIX"] = qt65Package
    testSettings.setWrappersForApplication(qt65AutName, ["Qt"])
    qt65Context = startApplication(qt65AutName, qt65Host, qt65Port)

    #Testing the Qt 6.5 app
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
    
    #Starting Qt 5.15 app
    os.environ["SQUISH_PREFIX"] = qt515Package
    testSettings.setWrappersForApplication(qt515AutName, ["Qt"])
    qt515Context = startApplication(qt515AutName, qt515Host, qt515Port)

    #Testing Qt 5.15 app
    spinUp(waitForObject(names.this_Payment_QSpinBox))
    spinUp(waitForObject(names.this_Payment_QSpinBox))
    doubleClick(waitForObject(names.this_Payment_QSpinBox), 226, 7, Qt.NoModifier, Qt.LeftButton)
    spinUp(waitForObject(names.this_Payment_QSpinBox))
    doubleClick(waitForObject(names.this_Payment_QSpinBox), 226, 7, Qt.NoModifier, Qt.LeftButton)
    test.compare(str(waitForObjectExists(names.make_Payment_qt_spinbox_lineedit_QLineEdit).text), "$ 107")
    
    #Switching to the Qt 6.5 app
    setApplicationContext(qt65Context)
    sendEvent("QMoveEvent", waitForObject(names.address_Book_MainWindow), 61, 246, 459, 263)

    #Switching to the Qt 5.15 app
    setApplicationContext(qt515Context)
       
    #Closing the servers
    #Ctrl + c
