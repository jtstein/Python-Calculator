"""
Jordan Stein
Calculates user-entered mathematical expressions
Requires Python 3.4.2 interpreter
"""
    
def evaluateString(s = ""):

    stackOne = [] # numbers stack
    stackTwo = [] # operators stack

    sval = ""
    isOp = False
    for x in range(0,len(s)):
    
        if (s[x] != '+' and s[x] != '-' and s[x] != '*' and s[x] != '/' and s[x] != '(' and s[x] != ')'):
            sval += s[x]
        else:
            stackTwo.append(s[x])
            isOp = True
        
        if isOp == True and sval != '':
            stackOne.append(sval)
            sval = ""
    
        if x == len(s)-1 and sval != "":
            stackOne.append(sval)
    
        isOp = False 
    
    
    parens(stackOne, stackTwo)
    multDiv(stackOne, stackTwo)
    addSub(stackOne, stackTwo)
    
    total = stackOne.pop()
    print(s + " evaluates to: " + str(total))
    
    
def parens(stackOne = [], stackTwo = []):
    parenCount = 0
    i = 0
    while i < len(stackTwo):
        if stackTwo[i] == '(':
            openIndex = i
            parenCount +=1
        if stackTwo[i] == ')':
            parenCount -=1
            
            if parenCount == 0:
                subOne = stackOne[openIndex:i]
                subTwo = stackTwo[openIndex+1:i]
            
            if parenCount > 0:
                subOne = stackOne[openIndex-parenCount: i-parenCount]
                subTwo = stackTwo[openIndex+1:i]
            multDiv(subOne, subTwo)
            addSub(subOne, subTwo)
            
            stackOne[openIndex-parenCount] = subOne.pop()
            
            k=0
            for j in range(openIndex+1-parenCount, i-parenCount):
                stackOne.pop(j-k)
                stackTwo.pop(j-k)
                k+=1
                
            stackTwo.pop(openIndex)
            stackTwo.pop(openIndex)
            i-=2
            
            break
        
        i+=1
     
    
    if parenCount > 0:
        parens(stackOne, stackTwo) # recursively call parens() until parenCount = 0
    
def multDiv(mdOne = [], mdTwo = []):
    total = 0.0
    i = 1

    while i < len(mdOne):
        if mdTwo[i-1] == '*':
            total += float(mdOne[i-1]) * float(mdOne[i])
            mdOne.pop(i-1)
            mdOne[i-1] = total
            mdTwo.pop(i-1)
            i = i-1
    
        elif mdTwo[i-1] == "/":
            total += float(mdOne[i-1]) / float(mdOne[i])
            mdOne.pop(i-1)
            mdOne[i-1] = total
            mdTwo.pop(i-1)
            i = i-1
        i+=1
        total = 0.0


def addSub(asOne = [], asTwo = []):
    total = float(asOne[0])
    i = 1
    while i < len(asOne):
        if asTwo[i-1] == '+':
            total = float(asOne[i-1]) + float(asOne[i])
            asOne.pop(i-1)
            asOne[i-1] = total
            asTwo.pop(i-1)
            i = i - 1
        elif asTwo[i-1] == '-':
            total = float(asOne[i-1]) - float(asOne[i])
            asOne.pop(i-1)
            asOne[i-1] = total
            asTwo.pop(i-1)
            i = i - 1
        i+=1
        total = 0


def main():
    while True:
        while True:
            isAlpha = False
            hasNums = False
            operatorBeforeParen = False
            operatorAfterParen = False
            multOperatorsInRow = False
            operatorBtwnParens = True
            validChars = True
            
            s = input("Please input a mathematical expression. ('n' to exit): ")
            if s.lower() == 'n':
                return #exits the program
            
            countParens = 0
            for x in range(0, len(s)):
                if s[x] == '(':
                    countParens+=1
                elif s[x] == ')':
                    countParens -=1
                if s[x].isalpha():
                    print("Alphabetical characters detected: Please input a mathematical expression")
                    isAlpha = True
                    break
                if s[x].isdigit():
                    hasNums = True
                elif s[x] != '+' and s[x] != '-' and s[x] != '*' and s[x] != '/' and s[x] != '(' and s[x] != ')' and s[x] != '.' and s[x] != ' ':
                    validChars = False
             
            for x in range(0,len(s)-1):
                if x < len(s):
                    if s[x].isdigit() and s[x+1] == '(':
                        operatorBeforeParen = True
                        break
                    if s[x+1].isdigit() and s[x] == ')':
                        operatorAfterParen = True
                        break
                    if ( s[x] == '+' or s[x] == '-' or s[x] == '*' or s[x] == '/') and (s[x+1] == '+' or s[x+1] == '-' or s[x+1] == '*' or s[x+1] == '/'):
                        multOperatorsInRow = True
                        break
                    if s[x] == ')' and s[x+1] == '(':
                        operatorBtwnParens = False
                        break

            if operatorBtwnParens == False:
                print("There must be an operator between enclosing parenthesis, please re-input a mathematical expression.")
                break
            
            if validChars == False:
                print("Invalid characters detected, please re-input a mathematical expression.")
                break
            if operatorBeforeParen == True:
                print("No operator before parenthesis, please re-input a mathematical expression.")
                break
            if operatorAfterParen == True:
                print("No operator after parenthesis, please re-input a mathematical expression.")
                break
            if multOperatorsInRow == True:
                print("Multiple operators cannot appear consecutively. please re-input a mathematical expression.")
                break
            if countParens != 0:
                print("Parenthesis mismatch, please re-input a mathematical expression.")
                break
            
            if hasNums == False:
                print("No numbers detected in the expression. Please input a mathematical expression.")
            elif isAlpha == False:
                evaluateString(s)
                break
        print()
                    
main() # starts program