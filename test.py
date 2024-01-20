import json
database = []

with open('file_for_breakfast.json', 'r', encoding='utf-8-sig') as file:
    content = json.load(file)
    
for i in range(0,55,2):
    database.append(content[i])
    
    
with open('file_breakfast.json', 'w', encoding='utf-8-sig') as file:
    json.dump(database, file, indent=4, ensure_ascii=False)
    
