import sys
import random
from time import strftime
import datetime
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QVBoxLayout, QPlainTextEdit, QComboBox, QMainWindow)
from PyQt5.QtGui import (QIcon, QFont, QFontDatabase)
from PyQt5.QtCore import (QDateTime, QDate, QTime, Qt, QTimer)
import aws_sql_credentials as awsdb
# from mainWindow import MainMenu
import __main__
class CreateCustomerForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create New Customer - Car Rental App")
        self.setWindowIcon(QIcon(r"carrentalapp\images\car-rental.png"))
        self.setFixedSize(1024, 768)
        self.first_name()
        self.last_name()
        self.phone_number()
        self.email_address()
        self.customer_status()
        self.date_created()
        self.back_button()
        self.save_customer()
        self.show()
    
    def openAddCustomer(self):
        self.window = QMainWindow()
        self.ui = __main__.CreateCustomerForm
        self.ui(self.window)
        self.window.show()        

    def first_name(self):
        first_name_label = QLabel(self)
        first_name_label.move(20, 10)
        first_name_label.setText('First Name')
        first_name_label.resize(300, 30)
        first_name_field = QLineEdit(self)
        first_name_field.setText('Enter Customer\'s First Name')
        first_name_field.move(200, 10)
        first_name_field.resize(300, 30)
        
    def last_name(self):
        last_name_label = QLabel(self)
        last_name_label.move(20, 50)
        last_name_label.setText('Last Name')
        last_name_label.resize(300, 30)
        last_name_field = QLineEdit(self)
        last_name_field.setText('Enter Customer\'s Last Name')
        last_name_field.move(200, 50)
        last_name_field.resize(300, 30)

    def phone_number(self):
        phone_number_label = QLabel(self)
        phone_number_label.move(20, 90)
        phone_number_label.setText('Phone Number')
        phone_number_label.resize(300, 30)
        phone_number_layout = QLineEdit(self)
        phone_number_layout.setText('Enter Customer\'s Phone Number')
        phone_number_layout.move(200, 90)
        phone_number_layout.resize(300, 30)
    
    def email_address(self):
        email_address_label = QLabel(self)
        email_address_label.move(20, 130)
        email_address_label.setText('Enter Email Address')
        email_address_label.resize(300, 30)
        email_address_layout = QLineEdit(self)
        email_address_layout.setText('Enter Customer\'s Email Address')
        email_address_layout.move(200, 130)
        email_address_layout.resize(300, 30)
    
    def customer_status(self):
        customer_status_label = QLabel(self)
        customer_status_label.move(20, 170)
        customer_status_label.setText('Customer\'s Status')
        customer_status_label.resize(300, 30)
        status_menu = QComboBox(self)
        status_menu.addItems(['New Customer', 'Bronze Customer', 'Silver Customer', 'Gold Customer', 'Platinum Customer'])
        status_menu.move(200, 170)
        status_menu.resize(300, 30)
    
    def date_created(self):
        date_created_label = QLabel(self)
        date_created_label.move(20, 210)
        date_created_label.setText('Date Created')
        date_created_label.resize(300, 30)
        date_created_layout = QLineEdit(self)
        now = datetime.datetime.now()
        time_string = now.strftime('%H:%M:%S %p %d/%m/%y %A')
        date_created_layout.setText(time_string) # add code here
        date_created_layout.move(200, 210)
        date_created_layout.resize(300, 30)

    def back_button(self):
        back_button = QPushButton(self)
        # back_button.clicked.connect(self.openAddCustomer()) # add code
        back_button.setText("Main Menu")
        back_button.setGeometry(800, 700, 200, 40)
    
    def save_customer(self):
        save_customer = QPushButton(self)
        # save_customer.clicked.connect() # add code
        save_customer.setText("Save Customer")
        save_customer.setGeometry(590, 700, 200, 40)
    
    
    

app = QApplication(sys.argv)
win = CreateCustomerForm()
win.show()
sys.exit(app.exec_())