import re

def arithmetic_arranger(problems, test_case=False):
    arranged_problems = []
    calculator = {
        '+':lambda a , b : int(a) + int(b),
        '-':lambda a , b : int(a) - int(b)
    }
    
    if len(problems) > 5:
        return "Error: Too many problems."
    
    for problem in problems:
        fisrtNumber,operator,secondNumber = re.split(r"\s",problem)
        
        if not (re.search(r"[+-]",problem)):
            return "Error: Operator must be '+' or '-'."
        
        if re.search("[a-zA-Z]",problem):
            return "Error: Numbers must only contain digits."
        
        if len(fisrtNumber) > 4 or len(secondNumber) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        result = calculator[operator](fisrtNumber,secondNumber)
        lenght = max(len(fisrtNumber)+2, len(secondNumber)+2)      
        
        data = {
        1 : fisrtNumber.rjust(lenght),
        2 : operator + " " + secondNumber.rjust(lenght-2),
        3 : "-"*lenght,
        4 : str(result).rjust(lenght)
        }
        arranged_problems.append(data)
    
    top="    ".join(i[1] for i in arranged_problems)
    boton="    ".join(i[2] for i in arranged_problems)
    line="    ".join(i[3] for i in arranged_problems)
    res="    ".join(i[4] for i in arranged_problems)
    
    arranged_problems=f"{top}\n{boton}\n{line}" if test_case == False else f"{top}\n{boton}\n{line}\n{res}"
    
    return arranged_problems