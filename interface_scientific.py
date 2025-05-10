from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit, QPushButton, QSizePolicy
from PyQt5.QtCore import Qt
from interface_normal import NormalCalculatorWidget

class ScientificCalculatorWidget(NormalCalculatorWidget):
    def __init__(self):
        super().__init__()  # Initialize normal calculator UI
        self.adjust_display()
        self.remove_buttons()
        self.add_scientific_buttons()
    
    def adjust_display(self):
        self.layout.removeWidget(self.display)
        self.layout.addWidget(self.display, 0, 0, 2, 6, Qt.AlignBottom)
        
    def remove_buttons(self):
        for btn_text in ["+"]:
            btn = self.button_map[btn_text]
            self.layout.removeWidget(btn)
            btn.deleteLater()
            del self.button_map[btn_text]
    
    def add_scientific_buttons(self):
        # Extend the grid layout with scientific buttons
        scientific_buttons = [
            ("sin", 3, 4, 1, 1), ("cos", 3, 5, 1, 1), ("tan", 4, 4, 1, 1),
            ("√", 5, 5, 1, 1), ("x²", 5, 4, 1, 1), ("%", 6, 4, 1, 1),
            ("1/x", 6, 5, 1, 1), ("±", 6, 3, 1, 1), ("π", 4, 5, 1, 1),
            ("(", 2, 4, 1, 1), (")", 2, 5, 1, 1), ("+", 5, 3, 1, 1)
        ]
        for text, row, col, rowspan, colspan in scientific_buttons:
            btn = QPushButton(text)
            self.layout.addWidget(btn, row, col, rowspan, colspan)
            self.button_map[text] = btn