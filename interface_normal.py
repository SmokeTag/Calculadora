from PyQt5.QtWidgets import QPushButton, QWidget, QGridLayout, QLineEdit, QSizePolicy
from PyQt5.QtCore import Qt
from calculator_logic import CalculatorLogic

class NormalCalculatorWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.logic = CalculatorLogic()
        self.init_ui()
        self.connect_buttons()
        
    def init_ui(self):
        # Set up the layout
        self.layout = QGridLayout(self)
        
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.layout.addWidget(self.display, 0, 0, 2, 4, Qt.AlignBottom)
        
        buttons = [
        ("Clear", 2, 0, 1, 2),                ("/", 2, 2, 1, 1), ("<--", 2, 3, 1, 1),
        ("7", 3, 0, 1, 1), ("8", 3, 1, 1, 1), ("9", 3, 2, 1, 1),   ("*", 3, 3, 1, 1), 
        ("4", 4, 0, 1, 1), ("5", 4, 1, 1, 1), ("6", 4, 2, 1, 1),   ("-", 4, 3, 1, 1),
        ("1", 5, 0, 1, 1), ("2", 5, 1, 1, 1), ("3", 5, 2, 1, 1),   ("+", 5, 3, 2, 1),
        ("0", 6, 0, 1, 1), (".", 6, 1, 1, 1), ("=", 6, 2, 1, 1)
    ]
        self.button_map = {}
        for text, row, col, rowspan, colspan in buttons:
            btn = QPushButton(text)
            self.layout.addWidget(btn, row, col, rowspan, colspan)
            self.button_map[text] = btn
        self.button_map["+"].setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def connect_buttons(self):
        for text, button in self.button_map.items():
            if text == "=":
                button.clicked.connect(self.calculate_result)
            elif text == "Clear":
                button.clicked.connect(self.clear_display)
            elif text == "<--":
                button.clicked.connect(self.delete_last_character)
            else:
                button.clicked.connect(lambda _, b=text: self.append_to_display(b))

    def calculate_result(self):
        expression = self.display.text()
        if expression:
            try:
                result = self.logic.calculate_result(expression)
                self.display.setText(result)
            except Exception as e:
                self.display.setText("Error")
                print(f"Error evaluating expression: {e}")

    def clear_display(self):
        self.display.clear()

    def delete_last_character(self):
        current_text = self.display.text()
        if current_text:
            self.display.setText(current_text[:-1])

    def append_to_display(self, text):
        current_text = self.display.text()
        new_text = current_text + text
        self.display.setText(new_text)



    