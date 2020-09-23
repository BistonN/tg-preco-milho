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

            collection = 'historical_data'
            keys = ['date', 'corn_usd', 'open_corn_usd', 'max_corn_usd', 'min_corn_usd', 'vol_corn_usd', 'var_corn_usd']
            values = [utils.string_to_date(date), utils.string_to_float(colunm[1]), utils.string_to_float(colunm[2]), utils.string_to_float(colunm[3]), utils.string_to_float(colunm[4]), utils.string_to_float(colunm[5]), utils.string_to_float(colunm[6])]
            if server.db_select(collection, [keys[0]], [values[0]]) == None:
                server.db_insert(collection, keys, values)
            else:
                for i, *_ in enumerate(colunm):
                    if i > 1:
                        server.db_update(collection, {keys[0]: values[0]}, {keys[i]: values[i]})
