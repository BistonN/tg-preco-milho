# date, corn_br, corn_br_one_day_before, corn_br_two_days_before, corn_br_three_days_before, open_corn_br, max_corn_br, min_corn_br, vol_corn_br, var_corn_br, corn_usd, max_corn_usd, min_corn_usd, vol_corn_usd, var_corn_usd, dolar, max_dolar, min_dolar, var_dolar

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

writer.writerow(["date", "corn_br", "corn_br_one_day_before", "open_corn_br", "max_corn_br", "min_corn_br", "vol_corn_br", "var_corn_br", "corn_usd", "max_corn_usd", "min_corn_usd", "vol_corn_usd", "var_corn_usd", "dolar", "max_dolar", "min_dolar", "var_dolar"])

corn_br_one_day_before = 0
# corn_br_two_days_before = 0
# corn_br_three_days_before = 0

for item in server.db_select('historical_data_daily', _query= query):

    date = item.get('date')
    corn_br = item.get('corn_br')
    open_corn_br = item.get('open_corn_br')
    max_corn_br = item.get('max_corn_br')
    min_corn_br = item.get('min_corn_br')
    vol_corn_br = item.get('vol_corn_br')
    var_corn_br = item.get('var_corn_br')
    corn_usd = item.get('corn_usd')
    max_corn_usd = item.get('max_corn_usd')
    min_corn_usd = item.get('min_corn_usd')
    vol_corn_usd = item.get('vol_corn_usd')
    var_corn_usd = item.get('var_corn_usd')
    dolar = item.get('dolar')
    max_dolar = item.get('max_dolar')
    min_dolar = item.get('min_dolar')
    var_dolar = item.get('var_dolar')

    if corn_br and corn_usd and dolar:
        
        date_corn_one_day_before = date - timedelta(days=1)
        date_corn_two_days_before = date - timedelta(days=2)
        date_corn_three_days_before = date - timedelta(days=3)

        for one_day_before in server.db_select('historical_data_daily', _query={"date": date_corn_one_day_before}):
            if one_day_before.get('corn_br'): 
                if corn_br_one_day_before == 0:
                    corn_br_one_day_before = corn_br

                corn_br_one_day_before = one_day_before.get('corn_br')  

        # for two_days_before in server.db_select('historical_data_daily', _query={"date": date_corn_two_days_before}):
        #     if two_days_before.get('corn_br'): 
        #         if corn_br_two_days_before == 0:
        #             corn_br_two_days_before = corn_br

        #         corn_br_two_days_before = two_days_before.get('corn_br') 

        # for three_days_before in server.db_select('historical_data_daily', _query={"date": date_corn_three_days_before}):
        #     if three_days_before.get('corn_br'): 
        #         if corn_br_three_days_before == 0:
        #             corn_br_three_days_before = corn_br

        #         corn_br_three_days_before = two_days_before.get('corn_br') 
        
        writer.writerow([date, corn_br, corn_br_one_day_before, open_corn_br, max_corn_br, min_corn_br, vol_corn_br, var_corn_br, corn_usd, max_corn_usd, min_corn_usd, vol_corn_usd, var_corn_usd, dolar, max_dolar, min_dolar, var_dolar])

        print('date: ', date)
        print('corn_usd: ',corn_usd)
        print('corn_one_day_before: ', corn_br_one_day_before)
        print('corn_br: ', corn_br, '\n')
    
    else:
        print(date, ' sem dados')
