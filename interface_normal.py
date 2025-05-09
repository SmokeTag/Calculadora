import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QGridLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

hyundai_blue =       (0,    44,  95) #002c5f
progressive_blue =   (0,   170, 210) #00aad2
hyundai_sand =       (228, 220, 211) #e4dcd3
hyundai_light_sand = (246, 243, 242) #f6f3f2
white =              (255, 255, 255) #ffffff

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Normal Mode")
        self.setGeometry(0, 0, 1200, 800)
        self.setWindowIcon(QIcon("Calculator_icon.png"))
        self.init_ui()
        
    def init_ui(self):
        # Set up the main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QGridLayout(self.central_widget)
        
        # Create buttons for number pad
        self.number_0 = QPushButton("0")
        self.number_1 = QPushButton("1")
        self.number_2 = QPushButton("2")
        self.number_3 = QPushButton("3")
        self.number_4 = QPushButton("4")
        self.number_5 = QPushButton("5")
        self.number_6 = QPushButton("6")
        self.number_7 = QPushButton("7")
        self.number_8 = QPushButton("8")
        self.number_9 = QPushButton("9")
        self.decimal_button   = QPushButton(".")
        self.add_button       = QPushButton("+")
        self.subtract_button  = QPushButton("-")
        self.multiply_button  = QPushButton("*")
        self.divide_button    = QPushButton("/")
        self.backspace_button = QPushButton("<-")
        self.clear_button     = QPushButton("Clear")
        self.equals_button    = QPushButton("=")
        
        self.layout.addWidget(self.number_0, 4, 0)
        self.layout.addWidget(self.number_1, 3, 0)
        self.layout.addWidget(self.number_2, 3, 1)
        self.layout.addWidget(self.number_3, 3, 2)
        self.layout.addWidget(self.number_4, 2, 0)
        self.layout.addWidget(self.number_5, 2, 1)
        self.layout.addWidget(self.number_6, 2, 2)
        self.layout.addWidget(self.number_7, 1, 0)
        self.layout.addWidget(self.number_8, 1, 1)
        self.layout.addWidget(self.number_9, 1, 2)
        self.layout.addWidget(self.decimal_button, 4, 1)
        self.layout.addWidget(self.add_button, 3, 3, 2, 1)
        self.layout.addWidget(self.subtract_button, 2, 3)
        self.layout.addWidget(self.multiply_button, 1, 3)
        self.layout.addWidget(self.divide_button, 0, 2)
        self.layout.addWidget(self.backspace_button, 0, 3)
        self.layout.addWidget(self.clear_button, 0, 0, 1, 2)        
        
        self.layout.addWidget(self.equals_button, 4, 2)
        
        
        self.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                font-family: 'Calibri';
                
                background-color: #f6f3f2;
                border: 1px solid #e4dcd3;
                padding: 10px 12px;
                border-radius: 7px;
            }
            QPushButton:hover {
                background-color: #e4dcd3;
            }
            QPushButton:pressed {
                background-color: #00aad2;
            }
        """)
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())