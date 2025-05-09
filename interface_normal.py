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
        
        buttons = [
        ("0", 4, 0, 1, 1), ("1", 3, 0, 1, 1), ("2", 3, 1, 1, 1), ("3", 3, 2, 1, 1),
        ("4", 2, 0, 1, 1), ("5", 2, 1, 1, 1), ("6", 2, 2, 1, 1),
        ("7", 1, 0, 1, 1), ("8", 1, 1, 1, 1), ("9", 1, 2, 1, 1),
        (".", 4, 1, 1, 1), ("+", 3, 3, 2, 1), ("-", 2, 3, 1, 1),
        ("*", 1, 3, 1, 1), ("/", 0, 2, 1, 1), ("<-", 0, 3, 1, 1),
        ("Clear", 0, 0, 1, 2), ("=", 4, 2, 1, 1)
    ]
        self.button_map = {}  # Store buttons for later connections
        for text, row, col, rowspan, colspan in buttons:
            btn = QPushButton(text)
            self.layout.addWidget(btn, row, col, rowspan, colspan)
            self.button_map[text] = btn
        
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