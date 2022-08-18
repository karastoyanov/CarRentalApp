import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from PyQt5 import QtCore
from addCustomer import CreateCustomerForm
import addCustomer

class LoginForm(QWidget):
    switch_windows = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Welcome to Car Rental App')
        self.resize(500, 120)

        layout = QGridLayout()

        label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)
        

    def check_password(self):
        msg = QMessageBox()

        if self.lineEdit_username.text() == 'admin' and self.lineEdit_password.text() == 'Password1':
            msg.setText(f'Welcome {self.lineEdit_username.text()}')
            msg.exec_()
            return True
            # app.quit()
        else:
            msg.setText('Incorrect Login Credentials')
            msg.exec_()
            return False

    def switch(self):
        self.switch_windows.emit(self.button_login)
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = LoginForm()
    form.show()
    # sys.exit(app.exec_())
    app.exec_()
