from PyQt5.QtWidgets import QPushButton, QWidget, QVBoxLayout, QLineEdit, QSizePolicy
from PyQt5.QtCore import Qt
from calculator_logic import CalculatorLogic

class HistoryCalculatorWidget(QWidget):
    def __init__(self, logic: CalculatorLogic):
        super().__init__()
        self.logic = logic
        self.button_map = {}
        self.history_in_display = []
        self.history_in_display_index = 0
        self.init_ui()
        
    def init_ui(self):
        self.layout = QVBoxLayout(self)
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        
        buttons = ["Update History", "Clear History", "↑", "↓"]
        for text in buttons:
            btn = QPushButton(text)
            self.button_map[text] = btn

        self.layout.addWidget(self.button_map["Update History"])
        self.layout.addWidget(self.button_map["Clear History"])
        self.layout.addWidget(self.button_map["↑"])
        self.layout.addWidget(self.display)
        self.layout.addWidget(self.button_map["↓"])
        
        self.button_map["Update History"].clicked.connect(self.update_history)
        self.button_map["Clear History"].clicked.connect(self.clear_history)
        self.button_map["↑"].clicked.connect(self.scroll_to_previous_expressions)
        self.button_map["↓"].clicked.connect(self.scroll_to_next_expressions)

    def update_history(self):
        self.history_in_display = self.logic.history[-6:]
        self.history_in_display_index = 0

        if self.history_in_display:
            self.display.setText("\n\n".join(f"{expr} \n= {result}" for expr, result in self.history_in_display))
        else:
            self.display.setText("No history available.")

    def clear_history(self):
        self.logic.clear_history()
        self.history_in_display.clear()
        self.display.clear()

    def scroll_to_previous_expressions(self):
        if self.history_in_display_index > -len(self.logic.history) + 1:
            self.history_in_display_index -= 1
            start_index = self.history_in_display_index - 6
            self.history_in_display = self.logic.history[start_index:self.history_in_display_index]
            self.display.setText("\n\n".join(f"{expr} \n= {result}" for expr, result in self.history_in_display))
        print(self.history_in_display_index)
        print(self.history_in_display)

    def scroll_to_next_expressions(self):
        if self.history_in_display_index < 0:
            self.history_in_display_index += 1
            self.history_in_display = self.logic.history[self.history_in_display_index-6:self.history_in_display_index]
            self.display.setText("\n\n".join(f"{expr} \n= {result}" for expr, result in self.history_in_display))
        print(self.history_in_display_index)
        print(self.history_in_display)

