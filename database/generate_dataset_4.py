#4	2015 - 2019	date	'corn_br_week	'corn_usd_week' 'dolar_week' 'corn_br-1_week' 'corn_br-2_week' 'corn_br-3_week' 'max_corn_br-1_week' 'min_corn_br-1_week' 'open_corn_br-1_week' 'var_corn_br-1_week' 'vol_corn_br-1_week'														

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


writer = csv.writer(open("../files/dataset_4.csv", 'w'))

writer.writerow(['date', 'corn_br_week', 'corn_usd_week', 'dolar_week', 'corn_br-1_week', 'corn_br-2_week', 'corn_br-3_week', 'max_corn_br-1_week', 'min_corn_br-1_week', 'open_corn_br-1_week', 'var_corn_br-1_week', 'vol_corn_br-1_week']) 

year = 2009
month = 1

corn_br_weeks_before = [{}, {}, {}]

while year <= 2019 and month <= 12:
    for week in calendar.monthcalendar(year, month):
        for day in week:
            if day != 0:
                results = server.db_select('historical_data_weekly', ['date'], [dt.datetime(year, month, day)])
                if results != None:
                    print('results: ', results)
                    copy_results = results.copy()
                    corn_br_weeks_before.append(copy_results)

                    corn_3_before = corn_br_weeks_before.pop(0)
                    corn_2_before = corn_br_weeks_before[-2]
                    corn_1_before = corn_br_weeks_before[-3]



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


