import csv
import server as server
import utils

with open('../files/milho_br.csv', 'r') as arquivo_csv:
    reader = csv.reader(arquivo_csv, delimiter = ',')
    for idx, colunm in enumerate(reader):
        collection = 'historical_data'
        keys = ['date', 'corn_br']
        values = [colunm[0], utils.string_to_float(colunm[1])]

        values[0] = utils.string_to_date(values[0].replace('/', '.'))

        if server.db_select(collection, [keys[0]], [values[0]]) == None:
            server.db_insert(collection, keys, values)
        else:
            server.db_update(collection, {keys[0]: values[0]}, {keys[1]: values[1]})
