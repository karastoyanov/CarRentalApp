import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QVBoxLayout, QDateEdit)
from PyQt5.QtGui import (QIcon, QFont, QFontDatabase)
from PyQt5.QtCore import (QDateTime, QDate, QTime, Qt, QTimer, QSize)
import aws_sql_credentials as awsdb


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Welcome to Car Rental App")
        self.setWindowIcon(QIcon(r"carrentalapp\images\car-rental.png"))
        self.setFixedSize(1024, 768)
        self.create_customer()
        self.view_customers()
        self.add_vehicle()
        self.view_vehicles()
        self.contact_form()
        # self.timerLayout = QLabel()
        # time_layout = QVBoxLayout()
        # self.timerLayout.resize(100, 100)
        # self.timerLayout.move(10, 700)
        # time_layout.addWidget(self.timerLayout)
        # self.setLayout(time_layout)
        # timer = QTimer(self)
        # timer.timeout.connect(self.clock)
        # timer.start()
        self.show()
        
    def create_customer(self):    
        create_cust_button = QPushButton("Create Customer", self)
        # create_cust_button.clicked.connect() # add func
        create_cust_button.setText("Create \n Customer")
        create_cust_button.setGeometry(10, 10, 200, 80)
        
    def view_customers(self):            
        view_cust_button = QPushButton("View Customers", self)
        # view_cust_button.clicked.connect() # add func
        view_cust_button.setText("View \n Customers")
        view_cust_button.setGeometry(10, 100, 200, 80)
    
    def add_vehicle(self):             
        add_vehicle_button = QPushButton("Add Vehicle", self)
        # add_vehicle_button.clicked.connect() # add func
        add_vehicle_button.setText("Add \n Vehicle")
        add_vehicle_button.setGeometry(10, 190, 200, 80)
            
    def view_vehicles(self):         
        view_vehicles_button = QPushButton("View Vehicles", self)
        # view_vehicles_button.clicked.connect() # add func
        view_vehicles_button.setText("View \n Vehicles")
        view_vehicles_button.setGeometry(10, 280, 200, 80)

    def contact_form(self):
        contact_button = QPushButton(self)
        # contact_button.clicked.connect() #add func    
        contact_button.setText("Contact Form")
        contact_button.setGeometry(700, 700, 300, 40)
    
    def clock(self):        
        current_time = QTime.currentTime()
        current_date = QDateTime.currentDateTime()
        time = current_time.toString('hh:mm:ss AP')
        date = current_date.toString("dd-MM-yyyy dddd")
        result = f'Today is : {time}\n{date}'
        self.timerLayout.setText(result)
    

        

    
app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())