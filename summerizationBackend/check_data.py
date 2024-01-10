import json

with open('../要素识别第二阶段训练数据/divorce/train_selected.json', 'r', encoding='utf-8') as f:
    first_doc = f.readlines()[0]
    first_doc_json = json.loads(first_doc)
    for item in first_doc_json:
        print(item['labels'], item['sentence'])



