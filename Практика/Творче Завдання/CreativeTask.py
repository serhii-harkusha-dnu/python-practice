# Робота на GITHUB - https://github.com/serhii-harkusha-dnu/python-practice/tree/main
# Творче завдання
# Студента групи КМ-22-1
# Гаркуші Сергія
import math
import string

def characterInList(character, allowedCharacters):
    for ch in allowedCharacters:
        if ch == character:
            return True
    return False

def skipSpaces(inputString: str, position: int):
    while position < len(inputString) and inputString[position] == ' ':
        position += 1
    return position

def readString(inputString: str, position: int, allowedCharacters: list, maxCharacters = 1000):
    symbol = "";
    while position < len(inputString) \
            and characterInList(inputString[position], allowedCharacters) \
            and len(symbol) < maxCharacters:
        symbol += inputString[position]
        position += 1
    position = skipSpaces(inputString, position)
    return symbol, position

def readSymbol(inputString: str, position: int):
    allowedCharacters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return readString(inputString, position, allowedCharacters)

def readNumberOrVariable(inputString: str, position: int):
    allowedCharacters = string.ascii_lowercase + string.ascii_uppercase + string.digits + "."
    minus, position = readString(inputString, position, ['-'])
    character, position = readString(inputString, position, allowedCharacters)
    return minus + character, position

def performOperation(firstArgument, secondArgument, operator):
    match operator:
        case '+':
            return firstArgument + secondArgument
        case '-':
            return firstArgument - secondArgument
        case '*':
            return firstArgument * secondArgument
        case '/':
            return firstArgument / secondArgument
        case '^':
            return math.pow(firstArgument, secondArgument)
        case _:
            raise Exception(f"Unknown operator {operator}")

def calculateVariable(inputString, availableVariables):
    position = 0
    variableName, position = readSymbol(inputString, position)
    if not characterInList(variableName[0], string.ascii_lowercase + string.ascii_uppercase):
        raise Exception(f"Incorrect variable: {variableName}. It should start with a letter.")
    _, position = readString(inputString, position, ['='])
    operatorStack = []
    firstArgumentStack = []
    bracketPositionStack = []
    prioritizedOperators = ['+', '-', '*', '/', '^']
    
    expectNumber = True
    while position < len(inputString):
        if expectNumber:
            openingBrackets, position = readString(inputString, position, ['('])
            for bracket in openingBrackets:
                bracketPositionStack.append(len(operatorStack))

            numberOrVariable, position = readNumberOrVariable(inputString, position)
            if characterInList(numberOrVariable[0], string.digits + "-"):
                currentNumber = float(numberOrVariable)
            else:
                currentNumber = availableVariables[numberOrVariable]
            expectNumber = False
        else:
            closingBrackets, position = readString(inputString, position, [')'])
            for bracket in closingBrackets:
                expectedOperatorStackSize = bracketPositionStack.pop()
                while len(operatorStack) > expectedOperatorStackSize:
                    previousOperator = operatorStack.pop()
                    previousFirstArgument = firstArgumentStack.pop()
                    currentNumber = performOperation(previousFirstArgument, currentNumber, previousOperator)
            
            if position >= len(inputString):
                break

            currentOperator, position = readString(inputString, position, prioritizedOperators, 1)
            while len(operatorStack) > 0 \
                    and (len(bracketPositionStack) == 0 or len(operatorStack) > bracketPositionStack[len(bracketPositionStack) - 1]) \
                    and prioritizedOperators.index(operatorStack[len(operatorStack)-1]) >= prioritizedOperators.index(currentOperator):
                previousOperator = operatorStack.pop()
                previousFirstArgument = firstArgumentStack.pop()
                currentNumber = performOperation(previousFirstArgument, currentNumber, previousOperator)
            operatorStack.append(currentOperator)
            firstArgumentStack.append(currentNumber)
            expectNumber = True

    if expectNumber:
        raise Exception(f"Incorrect input: string expected to end with constant or variable.")

    while len(operatorStack) > 0:
        previousOperator = operatorStack.pop()
        previousFirstArgument = firstArgumentStack.pop()
        currentNumber = performOperation(previousFirstArgument, currentNumber, previousOperator)

    return variableName, currentNumber

def printHelp():
    print("This program calculates math variables.")
    print("Example:")
    print("\tx = 1.5")
    print("\ty = 3")
    print("\tf = x + y / (x * y^0.5 - 1)")
    print("Enter variables to calculate. Leave empty to exit.")

printHelp()
availableVariables = {}
inputString = input()
while len(inputString) > 0:
    try:
        variableName, value = calculateVariable(inputString, availableVariables)
        print(f"Variable added: {variableName} = {value}")
        availableVariables[variableName] = value
    except Exception:
        print("Expression could not be calculated. Please try again.")
    inputString = input()