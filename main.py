import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon
from calculator_logic import CalculatorLogic
from interface_normal import NormalCalculatorWidget
from interface_scientific import ScientificCalculatorWidget
from menu_selector import ModeSelector

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.logic = CalculatorLogic()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("Calculator_icon.png"))
        screen = QApplication.primaryScreen().availableGeometry()
        app_width = 320; app_height = 400
        x = (screen.width() - app_width) // 2
        y = (screen.height() - app_height) // 2
        self.setGeometry(x, y, app_width, app_height)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Stacked widget for calculators
        self.stack = QStackedWidget()
        self.normal_calc = NormalCalculatorWidget(self.logic)
        self.scientific_calc = ScientificCalculatorWidget(self.logic)
        self.normal_calc = NormalCalculatorWidget()
        self.scientific_calc = ScientificCalculatorWidget()
        self.stack.addWidget(self.normal_calc)
        self.stack.addWidget(self.scientific_calc)
        
        self.mode_selector = ModeSelector(self.stack, self.normal_calc, self.scientific_calc)
        main_layout.addWidget(self.mode_selector)
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
