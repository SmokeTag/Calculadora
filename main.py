import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QIcon
from interface_normal import NormalCalculatorWidget
from interface_scientific import ScientificCalculatorWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Calculator")
        screen = QApplication.primaryScreen().availableGeometry()
        x = (screen.width() - 320) // 2
        y = (screen.height() - 400) // 2
        self.setGeometry(x, y, 320, 400)
        self.setWindowIcon(QIcon("Calculator_icon.png"))
        
        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Mode-switching buttons
        button_layout = QHBoxLayout()
        self.normal_btn = QPushButton("Normal")
        self.scientific_btn = QPushButton("Scientific")
        self.normal_btn.clicked.connect(self.show_normal)
        self.scientific_btn.clicked.connect(self.show_scientific)
        button_layout.addWidget(self.normal_btn)
        button_layout.addWidget(self.scientific_btn)
        main_layout.addLayout(button_layout)
        
        # Stacked widget for calculators
        self.stack = QStackedWidget()
        self.normal_calc = NormalCalculatorWidget()
        self.scientific_calc = ScientificCalculatorWidget()
        self.stack.addWidget(self.normal_calc)
        self.stack.addWidget(self.scientific_calc)
        main_layout.addWidget(self.stack)
        
        # Apply stylesheet to all child widgets
        self.setStyleSheet("""
            QLineEdit {
                font-size: 24px;
                padding: 10px;
                border: 1px solid #e4dcd3;
            }
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
        
        # Start in normal mode
        self.show_normal()
        
    def show_normal(self):
        self.stack.setCurrentWidget(self.normal_calc)
        self.normal_btn.setEnabled(False)
        self.scientific_btn.setEnabled(True)
        
    def show_scientific(self):
        self.stack.setCurrentWidget(self.scientific_calc)
        self.normal_btn.setEnabled(True)
        self.scientific_btn.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
