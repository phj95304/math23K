import json
import pandas as pd

#한국어로 번역된 파일을 이용해 json 생성
def extractor(json_file_path, text_file_path):
    test_file = open(text_file_path, "w")

    json_file = open(json_file_path)
    data = json.load(json_file)

    for entity in data:
        question = entity["original_text"]
        test_file.write(question)
        test_file.write("\n")

def dumper(question, destination):
    global idx
    global data
    #print(question)
    data.append({str(idx) : {"question":question}})

    with open(destination, "w", encoding="utf-8") as testfile:
        json.dump(data, testfile, ensure_ascii=False, indent=2)


def jsonMaker(KOR_text_tile_path, destination):
    global idx
    EquList = []
    data = open(KOR_text_tile_path)
    for i in data:
        EquList.append(i)
        
    df = pd.DataFrame(EquList, columns=['question'])
    df.to_csv("./Q_output.tsv",sep='\t',header=None, index=None)

 
if __name__ == "__main__":
    json_file_path = "./Math_23K.json"
    text_file_path = "./question_CH.txt"
    extractor(json_file_path, text_file_path)

    KOR_text_tile_path = "./question_KO.txt"
    result_json_file_path = "./questionsheet_mathQA.json"
    idx = 1
    data = []
    jsonMaker(KOR_text_tile_path, result_json_file_path)
    