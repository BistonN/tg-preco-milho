import server as server
import datetime as dt
import csv

writer = csv.writer(open("../files/dataset.csv", 'w'))

query = {
    "$and": [
        { "date": {"$gt": dt.datetime(2013, 1, 1)}},
        { "date": {"$lt": dt.datetime(2019, 1, 1)}},
        { "corn_br": {"$ne": 0}}
    ]
}

writer.writerow(["date", "corn_br", "corn_usd", "br_production", "br_plateau_area", "br_productivity", "dolar"])
for item in server.db_select('historical_data', _query= query):
    date = item.get('date')
    corn_br = item.get('corn_br')
    corn_usd = item.get('corn_usd')
    br_production = item.get('br_production')
    br_plateau_area = item.get('br_plateau_area')
    br_productivity = item.get('br_productivity')
    dolar = item.get('dolar')

    if corn_br and corn_usd and br_production and br_plateau_area and br_productivity and dolar:
        writer.writerow([date, corn_br, corn_usd, br_production, br_plateau_area, br_productivity, dolar])

        print('date: ', date)
        print('corn_br: ', corn_br)
        print('corn_usd: ',corn_usd)
        print('br_production: ', br_production)
        print('br_productivity', br_productivity)
        print('br_plateau_area: ', br_plateau_area, '\n')

