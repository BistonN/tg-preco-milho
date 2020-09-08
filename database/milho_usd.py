import csv
import server as server

with open('../arquivos/milho_usd.csv', 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter = ',')
    for idx, coluna in enumerate(leitor):
        if idx > 1:
            collection = 'milho_usd'
            keys = ['date', 'value']
            values = [coluna[0], coluna[1]]
            if server.db_select(collection, keys, values) == None:
                server.db_insert(collection, keys, values)
