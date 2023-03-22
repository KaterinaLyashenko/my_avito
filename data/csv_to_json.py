import csv
import json

def convert_file(csv_file, json_file, model):
    res = []
    with open(csv_file, encoding="utf-8") as csv_f:
        for row in csv.DictReader(csv_f):
            del row['id'] #удаление колонки с id

            if 'price' in row: #преобразует price в int
                row['price'] = int(row['price'])

            if 'is_published' in row: #преобразует is_published в boolean
                if row['is_published'] == "TRUE":
                    row['is_published'] = True
                if row['is_published'] == "FALSE":
                    row['is_published'] = False

            #if 'location_id' in row:
            #    row['location_id'] = [row['location_id']]

            res.append({"model": model, "fields": row})

    with open(json_file, 'w', encoding="utf-8") as json_f:
        json_f.write(json.dumps(res, ensure_ascii=False, indent=4))

#convert_file('user.csv', 'user_tes.json', 'users.user')
convert_file("categories.csv", "categories.json", "ads.category")
convert_file("ads.csv", "ads.json", "ads.ad")


