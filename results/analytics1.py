import csv
from decimal import *

def string_to_float(_str):
    _str = str(_str)
    _str = _str.replace(',', '.')
    return float(_str)

with open('../files/resultados-dataset.csv', 'r') as arquivo_csv:
    reader = csv.reader(arquivo_csv, delimiter = ',')
    total = 0
    list_reader = []
    contract_numbers = 100

    for colunm in reader:
        list_reader.append(colunm)


for idx, colunm in enumerate(list_reader):  
    # if colunm[0][3] == '8':
    if idx > 2:
        closing_current_price = string_to_float(colunm[1])
        price_preview = string_to_float(colunm[2])
        closing_price_before = string_to_float(list_reader[idx - 1][1])

        if closing_price_before:

            if Decimal(price_preview) > Decimal(closing_price_before):
                results = Decimal(((Decimal(closing_current_price) - Decimal(closing_price_before)) * 450))
                print(colunm[0], '',results)

            elif Decimal(price_preview) < Decimal(closing_price_before):
                results = Decimal(((Decimal(closing_price_before) - Decimal(closing_current_price)) * 450))
                print(colunm[0], '',results)

            elif Decimal(price_preview) == Decimal(closing_price_before):
                print('Out: ', colunm[0], colunm[1], colunm[2])

            total = Decimal(total) + Decimal(results)
print('total: ', Decimal(total) * Decimal(contract_numbers))
