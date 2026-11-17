import json

purchases = {}

with open('purchase_log.txt', 'r', encoding='utf-8') as file:
    for line in file:
        record = json.loads(line.strip())
        user_id = record['user_id']
        category = record['category']
        purchases[user_id] = category

print(list(purchases.items())[:5])