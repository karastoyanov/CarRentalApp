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
        self.resize(1024, 768)
        self.buttons()
        
        self.labels()
        self.show()
        
    def buttons(self):    
            create_cust_button = QPushButton("Create Customer", self)
            # create_cust_button.clicked.connect() # add func
            create_cust_button.setText("Create \n Customer")
            create_cust_button.setGeometry(10, 10, 200, 80)
            
            view_cust_button = QPushButton("View Customers", self)
            # view_cust_button.clicked.connect() # add func
            view_cust_button.setText("View \n Customers")
            view_cust_button.setGeometry(10, 100, 200, 80)
            
            add_vehicle_button = QPushButton("Add Vehicle", self)
            # add_vehicle_button.clicked.connect() # add func
            add_vehicle_button.setText("Add \n Vehicle")
            add_vehicle_button.setGeometry(10, 190, 200, 80)
            
            view_vehicles_button = QPushButton("View Vehicles", self)
            # view_vehicles_button.clicked.connect() # add func
            view_vehicles_button.setText("View \n Vehicles")
            view_vehicles_button.setGeometry(10, 280, 200, 80)
    
            contact_button = QPushButton(self)
            # contact_button.clicked.connect() #add func    
            contact_button.setText("Contact Form")
            contact_button.setGeometry(700, 700, 300, 40)
            
    def labels(self):   
        datetime_label = QPushButton(self)
        timer = QTimer(self)
        # timer.setInterval(100)
        timer.timeout.connect(self.showDateTime)
        timer.start()
        datetime_label.setText(self.showDateTime())
        datetime_label.setGeometry(700, 600, 300, 40)
        
    def showDateTime(self):
        # label_one = QLabel(self)
        # font = QFontDatabase.addApplicationFont(r'carrentalapp\fonts\Clearview Font.ttf')
        # font_families = QFontDatabase.applicationFontFamilies(font)
        # label_one.setFont(QFont(font_families[0], 10))
        current_time = QTime.currentTime()
        label_time = current_time.toString('hh:mm:ss')
        current_date = QDateTime.currentDateTime()
        label_date = current_date.toString('dd/mm/yyyy')
        # label_one.setText(f"Today is: {label_time} {label_date}")
        # label_one.setGeometry(20, 480, 500, 500)
        result = f'Today is {label_time} {label_date}'
        return result
    

        

    
app = QApplication(sys.argv)
win = MainWindow()
# win.show()
sys.exit(app.exec_())