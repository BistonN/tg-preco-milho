import csv
import server as server 
import calendar
import utils 

with open('../files/dados_safra_milho_conab.csv', 'r') as arquivo_csv:
    reader = csv.reader(arquivo_csv, delimiter = ',')
    year = 2013
    month = 1

    collection = 'historical_data_daily'

    for colunm in reader:    
        if year < 2021: 
            for week in calendar.monthcalendar(year, month):
                for day in week:
                    if day != 0:   
                        date = utils.format_number(day, 2) + '.' + utils.format_number(month, 2) + '.' + str(year)
                        date = utils.string_to_date(date) 
                        if server.db_select(collection, ['date'], [date]) == None:
                            server.db_insert(collection, ['date', 'br_production'], [date, utils.string_to_float(colunm[1])])
                        else:
                            server.db_update(collection, {"date": date}, {'br_production': utils.string_to_float(colunm[1])})

                        if server.db_select(collection, ['date'], [date]) == None:
                            server.db_insert(collection, ['date', 'br_plateau_area'], [date, utils.string_to_float(colunm[2])])
                        else:
                            server.db_update(collection, {"date": date}, {'br_plateau_area': utils.string_to_float(colunm[2])})

                        if server.db_select(collection, ['date'], [date]) == None:
                            server.db_insert(collection, ['date', 'br_productivity'], [date, utils.string_to_float(colunm[3])])
                        else:
                            server.db_update(collection, {"date": date}, {'br_productivity': utils.string_to_float(colunm[3])})
                        
            if month + 1 == 13:
                month = 1
                year = year + 1
            else:
                month = month + 1
        else: 
            if month <= 8:
                break
            