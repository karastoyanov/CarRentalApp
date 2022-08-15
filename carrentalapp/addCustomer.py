import sys
import random
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from PyQt5.QtCore import (QDateTime, QDate, QTime, Qt)
import aws_sql_credentials as awsdb


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
        
        button_submit_customer = QPushButton('Save Customer')
        button_submit_customer.clicked.connect(self.save_customerQuery)
        layout.addWidget(button_submit_customer, 6, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)
        
        
        buton_exit = QPushButton('Exit')
        buton_exit.clicked.connect(sys.exit)
        layout.addWidget(buton_exit, 7, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)
        
        
        
        self.setLayout(layout)
        
        
    # Function to create a new random customer ID -- > \
        # Frist two chars are capital letters followed by 8 digits  
    def generate_id(lenght):
        while True:
            customer_id= []
            for i in range(lenght):
                if i == 0 or i == 1:
                    customer_id.append(chr(random.randrange(65, 90)))
                else:
                    customer_id.append(chr(random.randrange(48, 57)))
            generated_id  = ''.join(customer_id)
            awsdb.cursor.execute("""SELECT * FROM customers""")
            query_result = awsdb.cursor.fetchall()
            for row in query_result:
                to_check = row[0]
                if generated_id == to_check:
                    continue
                else:
                    return generated_id

    # Function to verify if another customer with same ID already exists
    def check_for_doubles(customer_id):
        awsdb.cursor.execute("""SELECT * FROM customers""")
        result = awsdb.cursor.fetchall()
        for row in result:
            to_check = row[0]
            if customer_id == to_check:
                return True
            else:
                continue
        return False
    
    
    def save_customerQuery(self):
        db = awsdb.db
        cursor = db.cursor()
        with cursor:
            sql_query = "INSERT INTO customers (cust_id, first_name, second_name, phone, \
                email, cust_status, date_created) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql_query, (CreateCustomerForm.generate_id(10), self.lineEdit_first_name.text(), self.lineEdit_last_name.text(), \
                self.lineEdit_phone_number.text(), self.lineEdit_email_address.text(), self.lineEdit_customer_status.text(), self.lineEdit_date_created.text()))
            db.commit()   
                    
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = CreateCustomerForm()
    form.show()
    sys.exit(app.exec_())