import csv
import server as server
import utils

with open('../files/dolar_brl_historio.csv', 'r') as arquivo_csv:
    reader = csv.reader(arquivo_csv, delimiter = ',')
    for idx, colunm in enumerate(reader):
        if idx > 1:
            collection = 'dolar'
            keys = ['date', 'value']
            values = [utils.string_to_date(colunm[0]), utils.string_to_float(colunm[1])]
            if server.db_select(collection, keys, values) == None:
                server.db_insert(collection, keys, values)
