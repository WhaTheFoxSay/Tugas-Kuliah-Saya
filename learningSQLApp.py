from learningSQL import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
import MySQLdb as mdb

def signals(self):
    #buat show tabel
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
    self.tableWidget.setSizePolicy(sizePolicy)
    self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
    self.tableWidget.setRowCount(10)
    self.tableWidget.setColumnCount(4)

    #panggil fungsi
    self.pushButton.clicked.connect(self.InsertData)
    self.pushButton_2.clicked.connect(self.UpdateData)
    self.pushButton_3.clicked.connect(self.DeleteData)
    self.pushButton_4.clicked.connect(self.login)
    self.pushButton_5.clicked.connect(self.select_data)
    
    
        
def DBConnection(self):
    try:
        db = mdb.connect('localhost', 'root', '', 'myfirstdb')
        QMessageBox.about(self, 'Connection', 'Database Connected Successfully')

    except mdb.Error as e:
        QMessageBox.about(self, 'Connection', 'Failed To Connect Database')
        sys.exit(1)     
    
def InsertData(self): 
    username = self.lineEdit.text()
    name = self.lineEdit_2.text()
    password = self.lineEdit_3.text()
    mobilePhone = self.lineEdit_4.text()
    
    con = mdb.connect('localhost','root','','myfirstdb')
    
    query = ("INSERT INTO user(username, name, password, mobile_phone) VALUES(%s, %s, %s, %s)")
    cur = con.cursor()
    cur.execute(query, (username, name, password, mobilePhone))
    con.commit()    
    QMessageBox.about(self, 'Inserted', 'Data Inserted Successfully')
    self.close()

def UpdateData(self): 
    username = self.lineEdit.text()
    name = self.lineEdit_2.text()
    password = self.lineEdit_3.text()
    mobilePhone = self.lineEdit_4.text()
    
    con = mdb.connect('localhost','root','','myfirstdb')
    
    query = ("UPDATE user SET name = %s, password = %s, mobile_phone = %s WHERE username = %s")
    cur = con.cursor()
    cur.execute(query, (name, password, mobilePhone, username))
    con.commit()    
    QMessageBox.about(self, 'Updated', 'Data Updated Successfully')
    self.close()

def DeleteData(self): 
    username = self.lineEdit.text()
            
    con = mdb.connect('localhost','root','','myfirstdb')
    
    cur = con.cursor()
    cur.execute("DELETE FROM user WHERE username = %s", [username])
    con.commit()    
    QMessageBox.about(self, 'Deleted', 'Data Deleted Successfully')
    self.close()
    
def login(self):
    try:
        username = self.lineEdit_5.text()
        password = self.lineEdit_6.text()

        #ini sama aja sama connect diatas
        con = mdb.connect(
            host="localhost",
            user="root",
            password="",
            database="myfirstdb"
        )

        cur = con.cursor()
        cur.execute("SELECT username,password from user where username like '"+username + "'and password like '"+password+"'")
        result = cur.fetchone()

        if result == None:
            QMessageBox.about(self, 'Failed to Login', 'Incorrect Email & Password')

        else:
            QMessageBox.about(self, 'Login Success', 'You Are Login')
            

    except mdb.Error as e:
        QMessageBox.about(self, 'Error', 'Some Error')
        

def select_data(self):
    try:
        dbname = self.lineEdit_7.text()
        tablename = self.lineEdit_8.text()
        con = mdb.connect(

            host="localhost",
            user="root",
            password="",
            database=dbname
        )

        cur = con.cursor()

        cur.execute("SELECT * FROM {} ".format(tablename))

        result = cur.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            print(row_number)
            print(row_data)
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                print(column_number)
                print(str(data))
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    except mdb.Error as e:
        QMessageBox.about(self, 'Error', 'Some Error')
        
        
Ui_MainWindow.signals = signals
Ui_MainWindow.DBConnection = DBConnection
Ui_MainWindow.InsertData = InsertData
Ui_MainWindow.UpdateData = UpdateData
Ui_MainWindow.DeleteData = DeleteData
Ui_MainWindow.login = login
Ui_MainWindow.select_data = select_data

if __name__ == "__main__":              
    import sys 
    app = QtWidgets.QApplication(sys.argv) 
    MainWindow = QtWidgets.QMainWindow() 
    ui = Ui_MainWindow() 
    ui.setupUi(MainWindow) 
    ui.signals()
    MainWindow.show() 
    sys.exit(app.exec_()) 
