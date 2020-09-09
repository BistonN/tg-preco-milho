import csv
import server as server

with open('../files/milho_br.csv', 'r') as arquivo_csv:
    reader = csv.reader(arquivo_csv, delimiter = ',')
    for idx, colunm in enumerate(reader):
        collection = 'milho_br'
        keys = ['date', 'value']
        values = [colunm[0], colunm[1]]
        if server.db_select(collection, keys, values) == None:
            values[0] = values[0].replace('/', '.')
            server.db_insert(collection, keys, values)
