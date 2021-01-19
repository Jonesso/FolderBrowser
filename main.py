import sys  # for passing argv into QApplication
import os
from PyQt5 import QtWidgets

import design

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # To access all vars, methoda, etc in design.py
        super().__init__()
        self.setupUi(self)  # Initialize design itself
        self.btnBrowse.clicked.connect(self.browse_folder)  # Run browse_folder on button click

    def browse_folder(self):
        self.listWidget.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Select folder")
        
        if directory:  # don't execute if user didn't select a folder
            for file_name in os.listdir(directory):  # for each file in directory
                self.listWidget.addItem(file_name)   # add file into listWidget

def main():
    app = QtWidgets.QApplication(sys.argv)  # new QApplication
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
