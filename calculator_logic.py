import math

class CalculatorLogic:
    def __init__(self):
        self.expression: str = ""
        self.result: str = ""
        self.history: list[tuple[str, str]] = []

    def add_to_history(self):
        if self.expression and self.result:
            self.history.append((self.expression, self.result))
        else:
            print("No expression or result to add to history.")
    
    def clear_history(self):
        self.history.clear()

    def process_expression(self):
        # self.expression = self.expression.replace("√", "sqrt(")
        self.expression = self.expression.replace("²", "**2")
        if self.expression.endswith("%"):
            self.expression = self.expression[:-1] + "/100"
        self.expression = self.expression.replace("%", "/100*")
        unclosed_parentheses = self.expression.count("(") - self.expression.count(")")
        if unclosed_parentheses > 0:
            self.expression += ")" * unclosed_parentheses

    def calculate_result(self, expression):
        """Evaluate the expression safely."""
        self.expression = expression
        self.process_expression()
        try:
            allowed_globals = {
                "math": math,
                "sin": lambda x: math.sin(math.radians(x)),
                "cos": lambda x: math.cos(math.radians(x)),
                "tan": lambda x: math.tan(math.radians(x)),
                "sqrt": math.sqrt
            }
            # Evaluate the expression using eval with restricted globals
            # Note: eval is used here, but we restrict the namespace to math functions
            result = eval(self.expression, {"__builtins__": {}}, allowed_globals)
            self.result = str(round(result, 8))
        except Exception as e:
            self.result = "Error"
            print(f"Error evaluating expression: {e}")
        self.add_to_history()
        return self.result

    def toggle_sign(self, text):
        print(f'text: {text}, len(text): {len(text)}')
        number_flag = False
        text = " " + text
        for index in range(len(text)-1, -1, -1):
            print(f'index: {index}')
            print(f'index: {index}, text[index]: {text[index]}')
            print(f'number_flag: {number_flag}')
            print(f'text[index].isdigit(): {text[index].isdigit()}')
            if text[index] == ")":
                continue
            if not text[index].isdigit():
                break
            number_flag = True

        if number_flag:
            if text[index] == "-":
                text = text[:index] + "+" + text[index + 1:]
            elif text[index] == "+":
                text = text[:index] + "-" + text[index + 1:]
            elif text[index] == " ":
                text = text[:index+1] + "-" + text[index+1:]
            else:
                text = text[:index+1] + "(-" + text[index+1:] + ")"
        return text[1:]
