import re

def parse_and_calculate(expression):
    # Regular expression to match basic operations
    pattern = r'^\s*(-?\d+(\.\d+)?)\s*([\+\-\*/])\s*(-?\d+(\.\d+)?)\s*$'
    match = re.match(pattern, expression)
    
    if not match:
        return "Error: Invalid expression format"
    
    num1, _, operator, num2, _ = match.groups()
    num1, num2 = float(num1), float(num2)
    
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Unsupported operator"

def main():
    print("Simple Calculator")
    print("Enter operations in the format: number1 operator number2 (e.g., 3 + 4)")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("Enter operation: ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        result = parse_and_calculate(user_input)
        print("Result:", result)

if __name__ == "__main__":
    main()