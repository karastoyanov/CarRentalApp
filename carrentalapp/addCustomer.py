import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from PyQt5.QtCore import (QDateTime, QDate, QTime, Qt)

class CreateCustomerForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create New Customer")
        self.resize(1024, 768)
        
        layout = QGridLayout()
        
        label_first_name = QLabel('<font size="4"> Customer\'s First Name </font>')
        self.lineEdit_first_name = QLineEdit()
        self.lineEdit_first_name.setPlaceholderText("Enter Customer\'s First Name")
        layout.addWidget(label_first_name, 0, 0)
        layout.addWidget(self.lineEdit_first_name, 0, 1)

        label_last_name = QLabel('<font size="4"> Customer\'s Last Name </font>')
        self.lineEdit_last_name = QLineEdit()
        self.lineEdit_last_name.setPlaceholderText("Enter Customer\'s Last Name")
        layout.addWidget(label_last_name, 1, 0)
        layout.addWidget(self.lineEdit_last_name, 1, 1)
        
        label_phone_number = QLabel('<font size="4"> Customer\'s Phone Number </font>')
        self.lineEdit_phone_number = QLineEdit()
        self.lineEdit_phone_number.setPlaceholderText("Enter Customer\'s Phone Number'")
        layout.addWidget(label_phone_number, 2, 0)
        layout.addWidget(self.lineEdit_phone_number, 2, 1)

        label_email_address = QLabel('<font size="4"> Customer\'s Email Address </font>')
        self.lineEdit_email_address = QLineEdit()
        self.lineEdit_email_address.setPlaceholderText("Enter Customer\'s Email Address'")
        layout.addWidget(label_email_address, 3, 0)
        layout.addWidget(self.lineEdit_email_address, 3, 1)
        
        label_customer_status = QLabel('<font size="4"> Customer\'s Status </font>')
        self.lineEdit_customer_status = QLineEdit()
        self.lineEdit_customer_status.setText("NEW")
        self.lineEdit_customer_status.setReadOnly(True)        
        layout.addWidget(label_customer_status, 4, 0)
        layout.addWidget(self.lineEdit_customer_status, 4, 1)
        
        label_date = QLabel('<font size="4"> Date Created </font>')
        self.lineEdit_date_created = QLineEdit()
        date = QDate().currentDate()
        time = QTime().currentTime()
        self.lineEdit_date_created.setText(date.toString(Qt.ISODate) + ' ' + time.toString(Qt.ISODate))
        self.lineEdit_date_created.setReadOnly(True)
        layout.addWidget(label_date, 5, 0)
        layout.addWidget(self.lineEdit_date_created, 5, 1)
        
        
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = CreateCustomerForm()
    form.show()
    sys.exit(app.exec_())