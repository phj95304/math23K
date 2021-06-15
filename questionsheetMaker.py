import pandas as pd
import json
import sys
import csv

def Equation(path):
    answerLst=[]
    idx =1

    f = open(path, 'r', encoding='utf-8') 
    rdr = csv.reader(f) 
    for line in rdr: 
        answerLst.append( {idx:{"question":line}})
        idx+=1 
    f.close()


    with open("./questionsheet_Math23.json", "w", encoding="utf-8") as answer_file:
        json.dump(answerLst, answer_file, ensure_ascii=False,indent=2)

    sys.exit()

Equation("./Q_output.tsv")