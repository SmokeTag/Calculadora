from PyQt5.QtWidgets import QPushButton, QWidget, QGridLayout, QLineEdit, QSizePolicy
from PyQt5.QtCore import Qt

class NormalCalculatorWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        # Set up the layout
        self.layout = QGridLayout(self)
        
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.layout.addWidget(self.display, 0, 0, 2, 4, Qt.AlignBottom)
        
        buttons = [
        ("0", 6, 0, 1, 1), ("1", 5, 0, 1, 1), ("2", 5, 1, 1, 1), ("3", 5, 2, 1, 1),
        ("4", 4, 0, 1, 1), ("5", 4, 1, 1, 1), ("6", 4, 2, 1, 1),
        ("7", 3, 0, 1, 1), ("8", 3, 1, 1, 1), ("9", 3, 2, 1, 1),
        (".", 6, 1, 1, 1), ("+", 5, 3, 2, 1), ("-", 4, 3, 1, 1),
        ("*", 3, 3, 1, 1), ("/", 2, 2, 1, 1), ("<--", 2, 3, 1, 1),
        ("Clear", 2, 0, 1, 2), ("=", 6, 2, 1, 1)
    ]
        self.button_map = {}
        for text, row, col, rowspan, colspan in buttons:
            btn = QPushButton(text)
            self.layout.addWidget(btn, row, col, rowspan, colspan)
            self.button_map[text] = btn
        self.button_map["+"].setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        


    