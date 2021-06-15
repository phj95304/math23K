import json

def tester(json_file_path):
    counter = 0
    json_file = open(json_file_path)
    data = json.load(json_file)
    id =1
    for entity in data:
        fac = entity[str(counter+1)]
        
        answer = fac["answer"]
        equation = fac["equation"]
        
        try:
            #print(equation)
            equation = eval(equation)
            equation = float(equation)
            equation = round(equation, 2)
            equation = str(equation)
        except SyntaxError:
            equation = None
            id+=1
        except TypeError:
            equation = None
            id+=1
        except ZeroDivisionError:
            equation = None
            id+=1

        if equation == str(answer):
            #print(id)
            id+=1
        counter+=1
        
    print(counter)
    print(id)

tester("./test_answersheet_Math23.json")
