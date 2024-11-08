class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for i in range(abs(b)):
            result = self.add(result, a)
        if b < 0:  # Handle negative multiplier
            result = -result
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Error cannot divide by zero")
        result = 0
        remainder = a
        while remainder >= b:
            remainder = self.subtract(remainder, b)
            result += 1
        return result
    
    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Error cannot modulo by zero")
        remainder = a
        while remainder >= b:
            remainder = self.subtract(remainder, b)
        return remainder

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))