import openpyxl
import json

path = "roguelike_table.json"
items = ['id','name','usage','description','rarity','unlockCondDesc']

if __name__ == "__main__":
    with open(path, encoding='utf-8') as relicsfile:
        relics = json.load(relicsfile)['itemTable']['items']

    wb = openpyxl.Workbook()

    sheets=wb.active

    sheets.append(items)
    
    for relic in relics:
        sheet = []
        for item in items:
            sheet.append(relics[relic][item])

        sheets.append(sheet)

    wb.save('relics.xlsx')
        
            
