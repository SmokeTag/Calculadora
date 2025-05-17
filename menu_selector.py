from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton

class ModeSelector(QWidget):
    def __init__(self, stack_widget, normal_widget, scientific_widget, history_widget):
        super().__init__()
        self.stack_widget = stack_widget
        self.normal_widget = normal_widget
        self.scientific_widget = scientific_widget
        self.history_widget = history_widget
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout(self)
        self.normal_btn = QPushButton("Normal")
        self.scientific_btn = QPushButton("Scientific")
        self.history_btn = QPushButton("History")
        layout.addWidget(self.normal_btn)
        layout.addWidget(self.scientific_btn)
        layout.addWidget(self.history_btn)
        self.normal_btn.clicked.connect(self.show_normal)
        self.scientific_btn.clicked.connect(self.show_scientific)
        self.history_btn.clicked.connect(self.show_history)
        self.show_normal()

    def show_normal(self):
        self.stack_widget.setCurrentWidget(self.normal_widget)
        self.normal_btn.setEnabled(False)
        self.scientific_btn.setEnabled(True)
        self.history_btn.setEnabled(True)

    def show_scientific(self):
        self.stack_widget.setCurrentWidget(self.scientific_widget)
        self.normal_btn.setEnabled(True)
        self.scientific_btn.setEnabled(False)
        self.history_btn.setEnabled(True)
    
    def show_history(self):
        self.stack_widget.setCurrentWidget(self.history_widget)
        self.normal_btn.setEnabled(True)
        self.scientific_btn.setEnabled(True)
        self.history_btn.setEnabled(False)