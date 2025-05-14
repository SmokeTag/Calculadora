import numexpr as ne

class CalculatorLogic:
    def __init__(self):
        self.expression = ""
        self.result = ""

    def clear_expression(self):
        self.expression = ""

    def calculate_result(self, expression):
        self.expression = expression
        self.result = ""
        try:
            self.result = str(ne.evaluate(self.expression))
        except Exception as e:
            self.result = "Error"
            print(f"Error evaluating expression: {e}")
        return self.result