# PyQt5 Calculator Project

## Overview
This project is a graphical calculator application developed in Python using the **PyQt5** library. It supports two modes: **Normal** and **Scientific**, allowing users to perform basic and advanced mathematical operations. The project is designed with **Object-Oriented Programming (OOP)** principles, separating the user interface from the logic for better maintainability and scalability.

## Features
- **Mode Selection**: Switch between Normal and Scientific modes via a menu without opening a new window.
- **Normal Mode**:
  - Numeric buttons (0-9), decimal point, and basic operations (+, -, *, /).
  - "=" button to evaluate expressions and "Clear" button to reset.
  - Display area for expressions and results.
- **Scientific Mode**:
  - All Normal mode features.
  - Additional operations: square root (√), square (x²), percentage (%), reciprocal (1/x), sign toggle (±), trigonometric functions (sin, cos, tan), and π constant.
- **Extra Features**:
  - Support for compound operations.
  - Calculation history.
  - Safe expression evaluation (avoiding `eval` for security).

## Project Structure
The project is organized into the following files:
- `main.py`: Entry point of the application, initializes the app and main window.
- `Calculadora.py`: Contains the core logic for calculations and expression evaluation.
- `interface_normal.py`: Defines the UI for the Normal calculator mode.
- `interface_cientifica.py`: Defines the UI for the Scientific calculator mode.
- `menu_selector.py`: Manages the mode selection menu and interface switching.

## Requirements
- Python 3.x
- PyQt5 (`pip install pyqt5`)

## Setup and Installation
1. Clone or download the project repository.
2. Install the required dependencies:
   ```bash
   pip install pyqt5
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Usage
1. Launch the application using `python main.py`.
2. Select the desired mode (Normal or Scientific) from the menu.
3. Use the buttons to input expressions and perform calculations.
4. View the calculation history (if implemented) or clear the display as needed.

## Development Notes
- The application uses `clicked.connect` for button-event connections.
- The UI and logic are separated to adhere to OOP principles.
- Safe evaluation of expressions is implemented to avoid using `eval`.
- This is a beginner-friendly project for learning PyQt5 and OOP concepts.

## Future Improvements
- Add keyboard input support.
- Enhance the calculation history with save/load functionality.
- Implement error handling for invalid expressions.
- Add unit tests for the calculation logic.

## Contributing
Feel free to fork the repository, create issues, or submit pull requests for improvements or bug fixes.

## License
This project is licensed under the MIT License.