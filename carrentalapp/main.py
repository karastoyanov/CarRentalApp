import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QFont, QFontDatabase
from addCustomer import CreateCustomerForm


class LoginForm(QWidget):
    switch_windows = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Welcome to Car Rental App')
        self.resize(500, 120)

        layout = QGridLayout()
        
        font = QFontDatabase.addApplicationFont(r'carrentalapp\fonts\KGRedHands.ttf')
        font_families = QFontDatabase.applicationFontFamilies(font)

        label_name = QLabel('<font size="4"> Username </font>')
        label_name.setFont(QFont(font_families[0], 12))
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel('<font size="4"> Password </font>')
        label_password.setFont(QFont(font_families[0], 12))
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton()
        
        # button_login.setText("Log In")
        button_login.setIcon(QIcon(r'carrentalapp\images\login.png'))
        button_login.clicked.connect(self.check_password)
        # layout.addWidget(button_login, 2, 0)
        button_login.setGeometry(100, 100, 2, 0)
        layout.addWidget(button_login)
        # layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)
        

    def check_password(self):
        msg = QMessageBox()

        if self.lineEdit_username.text() == 'admin' and self.lineEdit_password.text() == 'Password1':
            msg.setWindowTitle("Login Succesfull")
            msg.setText(f'Welcome {self.lineEdit_username.text()}')
            msg.exec_()
            return True
            # app.quit()
        else:
            msg.setText('Incorrect Login Credentials')
            msg.exec_()
            return False


    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = LoginForm()
    form.show()
    # sys.exit(app.exec_())
    app.exec_()
