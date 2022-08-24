import sys
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QPushButton,
                             QLabel,
                             QLineEdit,
                             QGridLayout,
                             QMessageBox,
                             QTableWidget,
                             QTableWidgetItem,
                             QMainWindow,
                             QTableWidget,
                             QTableWidgetItem)
# from PyQt5 import (QtCore, QtGui, QtWidgets)
from PyQt5.QtSql import (QSqlDatabase, QSqlQuery)
from PyQt5.QtGui import (QIcon)
import aws_sql_credentials as awsdb


class ViewCustomersForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("List of Customers")
        self.resize(1024, 768)
        
        layout = QGridLayout()
        
        # Set up the view
        self.view = QTableWidget()
        self.view.setColumnCount(7)
        self.view.setHorizontalHeaderLabels(["ID",
                                             "First Name", 
                                             "Last Name", 
                                             "Phone", 
                                             "Email", 
                                             "Status", 
                                             "Date Created"])
        self.view.showGrid()
        #Print the database table objects
        db = awsdb.db
        cursor = db.cursor()
        cursor.execute("SELECT * FROM customers")
        result = cursor.fetchall()
        for row in result:
            rows = self.view.rowCount()
            self.view.setRowCount(rows + 1)
            self.view.setItem(rows, 0, QTableWidgetItem(str(row[0])))
            self.view.setItem(rows, 1, QTableWidgetItem(row[1]))
            self.view.setItem(rows, 2, QTableWidgetItem(row[2]))
            self.view.setItem(rows, 3, QTableWidgetItem(row[3]))
            self.view.setItem(rows, 4, QTableWidgetItem(row[4]))
            self.view.setItem(rows, 5, QTableWidgetItem(row[5]))
            self.view.setItem(rows, 6, QTableWidgetItem(str(row[6])))
        # self.view.resizeColumnsToContents()
        # self.setCentralWidget(self.view)
        self.view.resize(1024, 800)
        layout.addWidget(self.view, 1, 0, 8, 10)
        self.view.horizontalHeader().setStretchLastSection(True)

        button_sumbit = QPushButton()
        button_sumbit.setText("Sumbit Changes")
        button_sumbit.setIcon(QIcon(r'carrentalapp\images\save.png'))
        button_sumbit.clicked.connect(self.submit_changes)
        layout.addWidget(button_sumbit, 10, 4, 1, 2)
        layout.setRowMinimumHeight(2, 75)
            
        button_back = QPushButton()
        button_back.setText("Back")
        button_back.setIcon(QIcon(r'carrentalapp\images\left-arrow.png'))
        # button_back.clicked.connect() #Add CODE
        layout.addWidget(button_back, 10, 6, 1, 2)
        layout.setRowMinimumHeight(2, 75)
        
        button_exit = QPushButton()
        button_exit.setText("Exit")
        button_exit.setIcon(QIcon(r'carrentalapp\images\exit.png'))
        button_exit.clicked.connect(sys.exit)
        layout.addWidget(button_exit, 10, 8, 1, 2)
        layout.setRowMinimumHeight(2, 75)
        
        
        layout.setRowStretch(8, 100)
        self.setLayout(layout)

    def submit_changes():
        #Add Code Here
        pass
    
app = QApplication(sys.argv)
win = ViewCustomersForm()
win.show()
sys.exit(app.exec_())
