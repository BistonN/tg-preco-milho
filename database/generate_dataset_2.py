# 'date', 'corn_br', 'corn_usd', 'dolar', 'corn_br-1', 'corn_br-2', 'corn_br-3', 'max_corn_br-1', 'min_corn_br-1', 'open_corn_br-1', 'var_corn_br-1', 'vol_corn_br-1' 

import server as server
import datetime as dt
from datetime import timedelta
import csv
import calendar
import datetime as dt

def get_last_not_null_value(key, corn_1_before, corn_2_before, corn_3_before):
    if corn_1_before.get(key) == 0 or corn_1_before.get(key) == '' or corn_1_before.get(key) == None:
        results = corn_2_before.get(key)
        if corn_2_before.get(key) == 0 or corn_2_before.get(key) == '' or corn_2_before.get(key) == None:
            results = corn_3_before.get(key)
            if corn_3_before.get(key) == 0 or corn_3_before.get(key) == '' or corn_3_before.get(key) == None:
                results = 0
        
        return results

    results = corn_1_before.get(key)
    return results


writer = csv.writer(open("../files/dataset_2.csv", 'w'))

writer.writerow(['date', 'corn_br', 'corn_usd', 'dolar', 'corn_br-1', 'corn_br-2', 'corn_br-3', 'max_corn_br-1', 'min_corn_br-1', 'open_corn_br-1', 'var_corn_br-1', 'vol_corn_br-1']) 

year = 2011
month = 1

corn_br_days_before = [{}, {}, {}]
print(corn_br_days_before )

while year <= 2019 and month <= 12:
    for *week, _, _ in calendar.monthcalendar(year, month):
        for day in week:
            if day != 0:
                results = server.db_select('historical_data_daily', ['date'], [dt.datetime(year, month, day)])
                
                if results.get('corn_br'):
                    copy_results = results.copy()
                    corn_br_days_before.append(copy_results)

                    corn_3_before = corn_br_days_before.pop(0)
                    corn_2_before = corn_br_days_before[-3]
                    corn_1_before = corn_br_days_before[-2]



                    max_corn_br_1_before = get_last_not_null_value('max_corn_br', corn_1_before, corn_2_before, corn_3_before)
                    min_corn_br_1_before = get_last_not_null_value('min_corn_br', corn_1_before, corn_2_before, corn_3_before)
                    open_corn_br_1_before = get_last_not_null_value('open_corn_br', corn_1_before, corn_2_before, corn_3_before)
                    var_corn_br_1_before = get_last_not_null_value('var_corn_br', corn_1_before, corn_2_before, corn_3_before)
                    vol_corn_br_1_before = get_last_not_null_value('vol_corn_br', corn_1_before, corn_2_before, corn_3_before)

                    writer.writerow([results.get('date'), results.get('corn_br'), results.get('corn_usd'), results.get('dolar'), corn_1_before.get('corn_br'), corn_2_before.get('corn_br'), corn_3_before.get('corn_br'), max_corn_br_1_before, min_corn_br_1_before, open_corn_br_1_before, var_corn_br_1_before, vol_corn_br_1_before]) 
                    print(results.get('date'))
    if month + 1 == 13:
        month = 1
        year = year + 1
    else:
        month = month + 1


