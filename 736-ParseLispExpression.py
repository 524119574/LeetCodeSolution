# 736. Parse Lisp Expression
# Hard

# 174

# 147

# Favorite

# Share
# You are given a string expression representing a Lisp-like expression to return the integer value of.

# The syntax for these expressions is given as follows.

# An expression is either an integer, a let-expression, an add-expression, a mult-expression, or an assigned variable. Expressions always evaluate to a single integer.
# (An integer could be positive or negative.)
# A let-expression takes the form (let v1 e1 v2 e2 ... vn en expr), where let is always the string "let", then there are 1 or more pairs of alternating variables and expressions, meaning that the first variable v1 is assigned the value of the expression e1, the second variable v2 is assigned the value of the expression e2, and so on sequentially; and then the value of this let-expression is the value of the expression expr.
# An add-expression takes the form (add e1 e2) where add is always the string "add", there are always two expressions e1, e2, and this expression evaluates to the addition of the evaluation of e1 and the evaluation of e2.
# A mult-expression takes the form (mult e1 e2) where mult is always the string "mult", there are always two expressions e1, e2, and this expression evaluates to the multiplication of the evaluation of e1 and the evaluation of e2.
# For the purposes of this question, we will use a smaller subset of variable names. A variable starts with a lowercase letter, then zero or more lowercase letters or digits. Additionally for your convenience, the names "add", "let", or "mult" are protected and will never be used as variable names.
# Finally, there is the concept of scope. When an expression of a variable name is evaluated, within the context of that evaluation, the innermost scope (in terms of parentheses) is checked first for the value of that variable, and then outer scopes are checked sequentially. It is guaranteed that every expression is legal. Please see the examples for more details on scope.
# Evaluation Examples:
# Input: (add 1 2)
# Output: 3

# Input: (mult 3 (add 2 3))
# Output: 15

# Input: (let x 2 (mult x 5))
# Output: 10

# Input: (let x 2 (mult x (let x 3 y 4 (add x y))))
# Output: 14
# Explanation: In the expression (add x y), when checking for the value of the variable x,
# we check from the innermost scope to the outermost in the context of the variable we are trying to evaluate.
# Since x = 3 is found first, the value of x is 3.

# Input: (let x 3 x 2 x)
# Output: 2
# Explanation: Assignment in let statements is processed sequentially.

# Input: (let x 1 y 2 x (add x y) (add x y))
# Output: 5
# Explanation: The first (add x y) evaluates as 3, and is assigned to x.
# The second (add x y) evaluates as 3+2 = 5.

# Input: (let x 2 (add (let x 3 (let x 4 x)) x))
# Output: 6
# Explanation: Even though (let x 4 x) has a deeper scope, it is outside the context
# of the final x in the add-expression.  That final x will equal 2.

# Input: (let a1 3 b2 (add a1 1) b2) 
# Output 4
# Explanation: Variable names can contain digits after the first character.

"""
Idea is similar to compiler code gen, but it is hard without the compiler tool chain.

First need to handle scoping

second need to find the right token
"""

class Solution(object):
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        return self.evaluateExpression(expression, {})

    def evaluateExpression(self, expression, variables): # This is a let exp, add expr or mult expr.
        if (expression[0] == "("):
            keywordEnd = self.findSpace(expression, 1)
            token = expression[1:keywordEnd]
            operandStr = expression[keywordEnd + 1: -1] # we get the operand part
            if (token == "add" or token == "mult"):
                firstEnd = self.findEndOfExpression(operandStr, 0)
                operand1 = self.evaluateExpression(operandStr[:firstEnd], variables)
                operand2 = self.evaluateExpression(operandStr[firstEnd + 1:], variables)
                return operand1 + operand2 if token == "add" else operand1 * operand2
            else:
                newScope = {}
                newScope["Prv"] = variables
                i = 0
                while(operandStr[i] != '(' and self.findSpace(operandStr, i) != -1): # check if this is a expression to be evaluated
                    varEnd = self.findSpace(operandStr, i)
                    exprStart = varEnd + 1
                    exprEnd = self.findEndOfExpression(operandStr, exprStart)
                    newScope[operandStr[i:varEnd]] = self.evaluateExpression(operandStr[exprStart:exprEnd], newScope)
                    i = exprEnd + 1
                return self.evaluateExpression(operandStr[i:], newScope)                
        else: # this is a variable or a integer
            if ((expression[0] >= '0' and expression[0] <= '9') or expression[0] == '-'):
                return int(expression)
            else:
                return self.findVariable(variables, expression)

    def findEndOfExpression(self, expression, start):
        if (expression[start] == '('):
            return self.findCorrespondingClosingBracket(expression, start) + 1
        else:
            return self.findSpace(expression, start)
    
    def findVariable(self, variables, variableName): # We omit the error handling here, we assume variable can always be found.
        currentVariables = variables
        while(variableName not in currentVariables):
            currentVariables = currentVariables["Prv"] # we store the outer scope under the key "Prv" 
        return currentVariables[variableName]
    
    def findChar(self, string, startingPosition, char):
        i = startingPosition
        while (i < len(string)):
            if (string[i] == char):
                return i
            i += 1
        return -1
    
    def findSpace(self, string, startingPosition):
        return self.findChar(string, startingPosition, " ")
    
    def findCorrespondingClosingBracket(self, string, startingPosition):
        bracketCount = 0
        for i in range(startingPosition, len(string)):
            if (string[i] == "("):
                bracketCount += 1
            if (string[i] == ")"):
                bracketCount -= 1
            if (bracketCount == 0):
                return i
            i += 1
        return -1
