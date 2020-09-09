import csv
import server as server
import utils

with open('../files/milho_usd.csv', 'r') as arquivo_csv:
    reader = csv.reader(arquivo_csv, delimiter = ',')
    for idx, colunm in enumerate(reader):
        if idx > 1:

            date = colunm[0].replace(',','')
            date = date.split(' ')
            date = utils.format_number(date[1], 2) + '.' + utils.format_number(str(utils.mounth_numeric.get(date[0])), 2) + '.' + date[2]

            collection = 'corn_usd'
            keys = ['date', 'value']
            values = [utils.string_to_date(date), utils.string_to_float(colunm[1])]
            if server.db_select(collection, keys, values) == None:
                server.db_insert(collection, keys, values)
