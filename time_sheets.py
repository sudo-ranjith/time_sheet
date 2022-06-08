# create a pyqt5 application to get the details from user and save it to a csv file
# input fields: name, email, project, hours, date
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel,  QAction, QComboBox, QMainWindow, QTreeWidget, QTreeWidgetItem, QTextEdit, QSplitter, QMdiArea
from PyQt5.QtGui import QIcon, QFont, QIntValidator
from PyQt5.QtCore import QDir, Qt, QSize, QThread, QThreadPool, QEvent
import json
import yaml
import traceback
from datetime import datetime
# import pandas
# import numpy as np
import time


class QTTimeSheets(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Time Sheets")
        self.setContentsMargins(0, 0, 0, 0)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setAttribute(Qt.WA_NoSystemBackground)

        # define title
        self.title_label = QLabel(self)
        self.title_label.setText("Time Sheets")

        self.name_label = QLabel(self)
        self.name_label.setText("Name")
        self.name_edit = QTextEdit()
        self.name_edit.setFixedHeight(25)
        # default value
        self.name_edit.setText("Ranjith")

        self.email_label = QLabel(self)
        self.email_label.setText("Email")
        self.email_edit = QTextEdit()
        self.email_edit.setText("ranjith@brillersys.com")
        self.email_edit.setFixedHeight(25)

        self.project_label = QLabel(self)
        self.project_label.setText("Project")
        # create dropdown PDF, IMI
        self.project_edit = QComboBox()
        self.project_edit.addItem("PDF")
        self.project_edit.addItem("IMI")
        self.project_edit.setFixedHeight(25)
        self.project_edit.setCurrentIndex(0)


        self.hours_label = QLabel(self)
        self.hours_label.setText("Hours")
        self.hours_edit = QTextEdit()
        self.hours_edit.setText("1")
        self.hours_edit.setFixedHeight(25)

        self.date_label = QLabel(self)
        self.date_label.setText("Date")
        self.date_edit = QTextEdit()
        today_date = datetime.now().strftime("%d/%m/%Y")
        self.date_edit.setText(today_date)
        self.date_edit.setFixedHeight(25)

        # task details
        self.task_label = QLabel(self)
        self.task_label.setText("Task Details")
        self.task_edit = QTextEdit()
        # self.task_edit.setFixedHeight(25)

        self.submit_button = QPushButton("Submit")
        self.submit_button.setFixedHeight(25)
        self.submit_button.clicked.connect(self.on_click_submit_button)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.title_label)
        self.main_layout.addWidget(self.name_label)
        self.main_layout.addWidget(self.name_edit)
        self.main_layout.addWidget(self.email_label)
        self.main_layout.addWidget(self.email_edit)
        self.main_layout.addWidget(self.project_label)
        self.main_layout.addWidget(self.project_edit)
        self.main_layout.addWidget(self.hours_label)
        self.main_layout.addWidget(self.hours_edit)
        self.main_layout.addWidget(self.date_label)
        self.main_layout.addWidget(self.date_edit)
        self.main_layout.addWidget(self.task_label)
        self.main_layout.addWidget(self.task_edit)
        self.main_layout.addWidget(self.submit_button)
        self.setLayout(self.main_layout)

        self.show()

    def on_click_submit_button(self):
        # write into a CSV file
        with open('time_sheets.csv', 'a') as f:
            name = self.name_edit.toPlainText()
            email = self.email_edit.toPlainText()
            project = self.project_edit.currentText()
            hours = self.hours_edit.toPlainText()
            date = self.date_edit.toPlainText()
            task_details = self.task_edit.toPlainText()
            f.write(name + ',' + email + ',' + project + ',' + hours + ',' + date + ',' + task_details + '\n')
        
        time.sleep(15)
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QTTimeSheets()
    sys.exit(app.exec_())
    
        
