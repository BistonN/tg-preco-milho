import csv
import server as server

with open('../arquivos/milho_br.csv', 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter = ',')
    for idx, coluna in enumerate(leitor):
        collection = 'milho_br'
        keys = ['date', 'value']
        values = [coluna[0], coluna[1]]
        if server.db_select(collection, keys, values) == None:
            values[0] = values[0].replace('/', '.')
            server.db_insert(collection, keys, values)
