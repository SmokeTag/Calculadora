import numexpr as ne

class CalculatorLogic:
    def __init__(self):
        self.expression = ""
        self.result = ""

    def clear_expression(self):
        self.expression = ""
        
    def process_expression(self):
        # self.expression = self.expression.replace("√", "sqrt(")
        # self.expression = self.expression.replace("²", "**2")
        self.expression = self.expression.replace("%", "/100*")
        if self.expression.endswith("*"):
            self.expression = self.expression[:-1]
        if self.expression.count("(") > self.expression.count(")"):
            self.expression += ")"

    def calculate_result(self, expression):
        self.expression = expression
        self.process_expression()
        self.result = ""
        try:
            self.result = str(ne.evaluate(self.expression))
        except Exception as e:
            self.result = "Error"
            print(f"Error evaluating expression: {e}")
        return self.result