import csv
import server as server 
import calendar
import utils 

with open('../files/dados_safra_milho_conab.csv', 'r') as arquivo_csv:
    reader = csv.reader(arquivo_csv, delimiter = ',')
    year = 2013
    mounth = 1

    for colunm in reader:    
        if year < 2021: 
            for week in calendar.monthcalendar(year, mounth):
                for day in week:
                    if day != 0:   
                        date = utils.format_number(day, 2) + '.' + utils.format_number(mounth, 2) + '.' + str(year)
                        date = utils.string_to_date(date)
                        if server.db_select('br_production', ['date', 'value'], [date, utils.string_to_float(colunm[1])]) == None:
                            server.db_insert('br_production', ['date', 'value'], [date, utils.string_to_float(colunm[1])])
                        if server.db_select('br_plateau_area', ['date', 'value'], [date, utils.string_to_float(colunm[2])]) == None:
                            server.db_insert('br_plateau_area', ['date', 'value'], [date, utils.string_to_float(colunm[2])])
                        if server.db_select('br_productivity', ['date', 'value'], [date, utils.string_to_float(colunm[3])]) == None:
                            server.db_insert('br_productivity', ['date', 'value'], [date, utils.string_to_float(colunm[3])])
            if mounth + 1 == 13:
                mounth = 1
                year = year + 1
            else:
                mounth = mounth + 1
        else: 
            if mounth <= 8:
                print('cabo')
                break
            