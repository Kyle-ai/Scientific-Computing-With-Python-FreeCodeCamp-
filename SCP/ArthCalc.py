#The function will return the correct conversion if the supplied problems are
#properly formatted, otherwise, it will return a string that describes an error
#that is meaningful to the user.

#    Situations that will return an error:
#   DONE     If there are too many problems supplied to the function. The limit is
#five, anything more will return: Error: Too many problems.

#   DONE     The appropriate operators the function will accept are addition and
#subtraction. Multiplication and division will return an error. Other operators
 #not mentioned in this bullet point will not need to be tested. The error
 #returned will be: Error: Operator must be '+' or '-'.

#   DONE     Each number (operand) should only contain digits. Otherwise, the
#function will return: Error: Numbers must only contain digits.

#   DONE     Each operand (aka number on each side of the operator) has a max of
#four digits in width. Otherwise, the error string returned will be: Error:
 #Numbers cannot be more than four digits.

#    If the user supplied the correct format of problems, the conversion you
#return will follow these rules:
#     DONE   There should be a single space between the operator and the longest of
 #        the two operands, the operator will be on the same line as the second operand.

 #   DONE Both operands will be in the same order as provided (the first will be the top
 #        one and the second will be the bottom.

 #   DONE     Numbers should be right-aligned.

#    DONE     There should be four spaces between each problem.

#    DONE There should be dashes at the bottom of each problem. The dashes should
#         run along the entire length of each problem individually. (The example above
#         shows what this should look like.)


def arithmetic_arranger(equation, parm2=None):
    if len(equation) > 5:
        return 'Error: Too many problems.'

    new_equation = equation
    line1 = line2 = line3 = line4 = ""

    break_space = "    "
    start = True
    for item in new_equation:
        new_item = item.split()
        num1 = new_item[0]
        num2 = new_item[2]
        if len(num1) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        operator = (new_item[1])
        if num1.isnumeric() == False:
            return 'Error: Numbers must only contain digits.'
        if num2.isnumeric() == False:
            return 'Error: Numbers must only contain digits.'

        answer = 0
        if operator == '-':
            answer = int(num1) - int(num2)
        elif operator == '+':
            answer = int(num1) + int(num2)
        else:
            return "Error: Operator must be '+' or '-'."
        #print(answer)
        answer = str(answer)
        space = max(len(num1), len(num2))
        if start == True:
            line1 += num1.rjust(space + 2)
            line2 += operator + ' ' + num2.rjust(space)
            line3 += '-' * (space + 2)
            if parm2 == True:
                line4 += answer.rjust(space + 2)
            start = False

        else:
            line1 += num1.rjust(space + 6)
            line2 += operator.rjust(5) + ' ' + num2.rjust(space)
            line3 += break_space + '-' * (space + 2)
            if parm2 == True:
                line4 += break_space + answer.rjust(space + 2)


    if parm2 == True:
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    return line1 + '\n' + line2 + '\n' + line3




arithmetic_arranger(["345 + 648", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])
arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])
