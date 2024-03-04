# encoding: UTF-8

from objectmaphelper import *

address_Book_MainWindow = {"type": "MainWindow", "unnamed": 1, "visible": 1, "windowTitle": Wildcard("Address Book*")}
address_Book_New_QToolButton = {"text": "New", "type": "QToolButton", "unnamed": 1, "visible": 1, "window": address_Book_MainWindow}
address_Book_Add_QToolButton = {"text": "Add", "type": "QToolButton", "unnamed": 1, "visible": 1, "window": address_Book_MainWindow}
address_Book_Add_Dialog = {"type": "Dialog", "unnamed": 1, "visible": 1, "windowTitle": "Address Book - Add"}
address_Book_Add_Forename_QLabel = {"text": "Forename:", "type": "QLabel", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
forename_LineEdit = {"buddy": address_Book_Add_Forename_QLabel, "type": "LineEdit", "unnamed": 1, "visible": 1}
address_Book_Add_Surname_QLabel = {"text": "Surname:", "type": "QLabel", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
surname_LineEdit = {"buddy": address_Book_Add_Surname_QLabel, "type": "LineEdit", "unnamed": 1, "visible": 1}
address_Book_Add_Email_QLabel = {"text": "Email:", "type": "QLabel", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
email_LineEdit = {"buddy": address_Book_Add_Email_QLabel, "type": "LineEdit", "unnamed": 1, "visible": 1}
address_Book_Add_Phone_QLabel = {"text": "Phone:", "type": "QLabel", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
phone_LineEdit = {"buddy": address_Book_Add_Phone_QLabel, "type": "LineEdit", "unnamed": 1, "visible": 1}
address_Book_Add_OK_QPushButton = {"text": "OK", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": address_Book_Add_Dialog}
address_Book_File_QToolBar = {"type": "QToolBar", "unnamed": 1, "visible": 1, "window": address_Book_MainWindow, "windowTitle": "File"}
address_Book_File_QTableWidget = {"aboveWidget": address_Book_File_QToolBar, "type": "QTableWidget", "unnamed": 1, "visible": 1, "window": address_Book_MainWindow}

make_Payment_MainWindow = {"type": "MainWindow", "unnamed": 1, "visible": 1, "windowTitle": "Make Payment"}
make_Payment_This_Payment_QLabel = {"text": "This Payment:", "type": "QLabel", "unnamed": 1, "visible": 1, "window": make_Payment_MainWindow}
this_Payment_QSpinBox = {"buddy": make_Payment_This_Payment_QLabel, "type": "QSpinBox", "unnamed": 1, "visible": 1}
make_Payment_qt_spinbox_lineedit_QLineEdit = {"name": "qt_spinbox_lineedit", "type": "QLineEdit", "visible": 1, "window": make_Payment_MainWindow}

