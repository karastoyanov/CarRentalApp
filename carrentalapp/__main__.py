import sys
from mainWindow import MainMenu
from addCustomer import CreateCustomerForm
from mainWindow import MainMenu
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QVBoxLayout, QDateEdit)
from PyQt5.QtGui import (QIcon, QFont, QFontDatabase)
from PyQt5.QtCore import (QDateTime, QDate, QTime, Qt, QTimer, QSize)
import aws_sql_credentials as awsdb

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainMenu()
    win.show()
    sys.exit(app.exec_())