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
import aws_sql_credentials as awsdb


class ViewCustomersForm(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("List of Customers")
        self.resize(1024, 768)
        
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
        self.view.resizeColumnsToContents()
        self.setCentralWidget(self.view)


app = QApplication(sys.argv)
win = ViewCustomersForm()
win.show()
sys.exit(app.exec_())
