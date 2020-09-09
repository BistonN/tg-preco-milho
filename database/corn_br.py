import csv
import server as server
import utils

with open('../files/milho_br.csv', 'r') as arquivo_csv:
    reader = csv.reader(arquivo_csv, delimiter = ',')
    for idx, colunm in enumerate(reader):
        collection = 'corn_br'
        keys = ['date', 'value']
        values = [colunm[0], utils.string_to_float(colunm[1])]
        if server.db_select(collection, keys, values) == None:
            values[0] = utils.string_to_date(values[0].replace('/', '.'))
            server.db_insert(collection, keys, values)
