import csv
import json
csvfile = csv.DictReader('news.csv', 'r')
output =[]
with open('news.csv', newline='' ,encoding='UTF-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for each in reader:
        row ={}
        row['source'] = each['source']
        row['question']  = each['question']
        row['answer']  = each ['answer']
        output.append(row)
json.dump(output,open('news.json','w'),indent=4,sort_keys=False)