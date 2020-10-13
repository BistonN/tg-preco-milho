import csv
import server as server
import utils
from datetime import timedelta

# print('\n\nImportando dados Semanais do Preço do Milho\n\n')
# with open('../files/milho_br_semanal.csv', 'r') as arquivo_csv:
#     reader = csv.reader(arquivo_csv, delimiter = ',')
#     for idx, colunm in enumerate(reader):
#         if idx > 1:
#             date = colunm[0].replace(',','')
#             date = date.split(' ')
#             date = utils.format_number(date[1], 2) + '.' + utils.format_number(str(utils.mounth_numeric.get(date[0])), 2) + '.' + date[2]

#             collection = 'historical_data_weekly'
#             keys = ['date', 'corn_br', 'open_corn_br', 'max_corn_br', 'min_corn_br', 'vol_corn_br', 'var_corn_br']
#             values = [utils.string_to_date(date), utils.string_to_float(colunm[1]), utils.string_to_float(colunm[2]), utils.string_to_float(colunm[3]), utils.string_to_float(colunm[4]), utils.string_to_float(colunm[5]), utils.string_to_float(colunm[6])]


#             if server.db_select(collection, [keys[0]], [utils.string_to_date(date)]) == None:
#                 server.db_insert(collection, keys, values)
#             else:
#                 for i, *_ in enumerate(colunm):
#                     if i > 1:
#                         server.db_update(collection, {keys[0]: values[0]}, {keys[i]: values[i]})

print('\n\nImportando dados Diarios do Preço do Milho\n\n')
with open('../files/milho2020.csv', 'r') as arquivo_csv:
    reader = csv.reader(arquivo_csv, delimiter = ',')
    for idx, colunm in enumerate(reader):
        if idx >= 1:
            collection = 'historical_data_daily'
            keys = ['date', 'corn_br', 'open_corn_br', 'max_corn_br', 'min_corn_br', 'vol_corn_br', 'var_corn_br']
            values = [colunm[0], utils.string_to_float(colunm[1]), utils.string_to_float(colunm[2]), utils.string_to_float(colunm[3]), utils.string_to_float(colunm[4]), utils.string_to_float(colunm[5]), utils.string_to_float(colunm[6])]

            values[0] = utils.string_to_date(values[0].replace('/', '.')) 

            if server.db_select(collection, [keys[0]], [values[0]]) == None:
                server.db_insert(collection, keys, values)
            else:
                for i, *_ in enumerate(colunm):
                    if i > 1:
                        server.db_update(collection, {keys[0]: values[0]}, {keys[i]: values[i]})
