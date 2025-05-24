# PyQt5 Calculator Project

## Overview
This project is a calculator application developed in Python using the **PyQt5** library. It supports two modes: **Normal** and **Scientific**, allowing users to perform both basic and advanced mathematical operations. The application is designed with **Object-Oriented Programming (OOP)** principles, separating the user interface from the calculation logic for maintainability and scalability.

## Features
- **Mode Selection**: Switch between Normal, Scientific, and History modes via a menu bar without opening new windows.
- **Normal Mode**:
  - Numeric buttons (0-9), decimal point, and basic operations (+, -, *, /).
  - "=" button to evaluate expressions, "Clear" button to reset, and "<--" button to delete the last character.
  - Display area for expressions and results.
- **Scientific Mode**:
  - All Normal mode features.
  - Additional operations: square root (√), square (x²), percentage (%), reciprocal (1/x), sign toggle (±), trigonometric functions (sin, cos, tan), and π constant.
  - Parentheses for grouping expressions.
- **History Mode**:
  - View and clear the calculation history.
- **Extra Features**:
  - Support for compound operations.
  - Calculation history is maintained and can be cleared.
  - Safe expression evaluation (restricted `eval` usage for security).

## Project Structure
The project is organized into the following files:
- `main.py`: Entry point of the application, initializes the app and main window.
- `calculator_logic.py`: Contains the core logic for calculations, expression evaluation, and history management.
- `interface_normal.py`: Defines the UI for the Normal calculator mode.
- `interface_scientific.py`: Defines the UI for the Scientific calculator mode.
- `interface_history.py`: Defines the UI for the History view.
- `menu_selector.py`: Manages the mode selection menu and interface switching.

## Requirements
- Python 3.11
- PyQt5 (`pip install pyqt5`)

## Setup and Installation
1. Clone or download the project repository.
2. Install the required dependencies:
   ```bash
   pip install pyqt5
   ```
3. Ensure the icon files (`Calculator_icon.png`, `History_icon.png`) are present in the project directory.
4. Run the application:
   ```bash
   python main.py
   ```

## Usage
1. Launch the application using `python main.py`.
2. Select the desired mode (Normal, Scientific, or History) from the menu.
3. Use the buttons to input expressions and perform calculations.
4. View or clear the calculation history as needed.

## Development Notes
- The application uses `clicked.connect` for button-event connections.
- The UI and logic are separated to adhere to OOP principles.
- Safe evaluation of expressions is implemented to avoid using unrestricted `eval`.
- Calculation history is managed and can be viewed or cleared.

## Future Improvements
- Add keyboard input support.
- Enhance the calculation history with save/load functionality.
- Implement more robust error handling for invalid expressions.
- Add unit tests for the calculation logic.

## Contributing
Feel free to fork the repository, create issues, or submit pull requests for improvements or bug fixes.

## License
This project is licensed under the MIT License.