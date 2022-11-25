from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import sys 


class User_Interface():
    def GUI_Interface(self, Form):
        Form.setObjectName("Bracket Nesting Checker")
        Form.resize(519, 344)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 130, 113, 32))
        self.pushButton.setStyleSheet("background-color:red;\n"
                                 "color: white;\n"
                                 "border-style: outset;\n"
                                "border-width: 2px;\n"
                                "border-radius: 10px;\n"
                                "boder-color:black;\n"
                                "font:bold 14px;\n"
                                "min-width:10px;\n"
                                "\n"
                                "\n"
                                "")

        self.pushButton.setObjectName("pushButton")
        self.retranslate_user_interface(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)    

    def retranslate_user_interface(self, Form):
        _translate = QtCore.QCoreApplication.translate  
        Form.setWindowTitle(_translate("Form", "Form"))  
        self.pushButton.setText(_translate("Form", "Browse")) 

        self.pushButton.clicked.connect(self.pushButton_handler)

    def pushButton_handler(self):
        print("Button Clicked") 
        self.open_dialog_box()   

    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName() 
        path = filename[0]
        print(path)   

        with open(path, "r") as f:
            print(f.readline())      

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = User_Interface()
    ui.GUI_Interface(Form)
    Form.show()
    sys.exit(app.exec_())

    
