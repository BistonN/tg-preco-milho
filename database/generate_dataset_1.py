# date corn_usd br_production, br_productivity, br_plateau_area corn_one_day_before, corn_br, dolar 

import server as server
import datetime as dt
from datetime import timedelta
import csv

writer = csv.writer(open("../files/dataset_1.csv", 'w'))

query = {
    "$and": [
        { "date": {"$gt": dt.datetime(2013, 1, 1)}},
        { "date": {"$lt": dt.datetime(2019, 1, 1)}},
        { "corn_br": {"$ne": 0}}
    ]
}

writer.writerow(["date", "corn_usd", "br_production", "br_plateau_area", "br_productivity", "dolar", "corn_br_-1", "corn_br"])
corn_one_day_before = 0

for item in server.db_select('historical_data_daily', _query= query):
    date = item.get('date')
    corn_br = item.get('corn_br')
    corn_usd = item.get('corn_usd')
    br_production = item.get('br_production')
    br_plateau_area = item.get('br_plateau_area')
    br_productivity = item.get('br_productivity')
    dolar = item.get('dolar')

    if corn_br and corn_usd and br_production and br_plateau_area and br_productivity and dolar:
        
        date_corn_one_day_before = date - timedelta(days=1)

        for i in server.db_select('historical_data_daily', _query={"date": date_corn_one_day_before}):
            if i.get('corn_br'): 
                if corn_one_day_before == 0:
                    corn_one_day_before = corn_br
                corn_one_day_before = i.get('corn_br')            
        
        writer.writerow([date, corn_usd, br_production, br_plateau_area, br_productivity, dolar, corn_one_day_before, corn_br])

        print('date: ', date)
        print('corn_usd: ',corn_usd)
        print('br_production: ', br_production)
        print('br_productivity', br_productivity)
        print('br_plateau_area: ', br_plateau_area)
        print('corn_one_day_before: ', corn_one_day_before)
        print('corn_br: ', corn_br, '\n')
