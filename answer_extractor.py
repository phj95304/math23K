import json
import pandas as pd


def dumper(question, destination):
    global idx
    global data
    #print(question)
    data.append({str(idx) : {"question":question}})
    with open(destination, "w", encoding="utf-8") as testfile:
        json.dump(data, testfile, ensure_ascii=False, indent=4)



#한국어로 번역된 파일을 이용해 json 생성
def extractor(json_file_path):
    EquList = []
    answerList = []
    id =1
    json_file = open(json_file_path)
    data = json.load(json_file)

    for entity in data:
        equation = entity["equation"]
        equation = equation[2:]
        answer = entity["ans"]

        try:
            #print(equation)
            equation_p = eval(equation)
            equation_p = float(equation_p)
            equation_p = round(equation_p, 2)
            equation_p = str(equation_p)
        except SyntaxError:
            equation = None
            answer = None
            id+=1
        except TypeError:
            equation = None
            answer = None
            id+=1
        except ZeroDivisionError:
            equation = None
            answer = None
            id+=1

        EquList.append(equation)
        answerList.append(str(answer))
        
    df = pd.DataFrame(EquList, columns=['equation'])
    dfAnswer = pd.DataFrame(answerList, columns=['answer'])
    
    all  = pd.concat([df,dfAnswer], axis=1)
    all.to_csv("./A_output.tsv",sep='\t',header=None, index=None)
        
    

 
if __name__ == "__main__":
    json_file_path = "./Math_23K.json"
    extractor(json_file_path)
    
    