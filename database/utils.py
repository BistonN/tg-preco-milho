import datetime as dt

def string_to_date(_str):
    return dt.datetime.strptime(_str, '%d.%m.%Y')

def format_number(_number:str, _characters:int):
    results = _number
    i = 0
    while i < _characters:
        if len(str(results)) >= _characters:
            return str(results)
        results = '0' + str(results)
        i = i + 1

def string_to_float(_str):
    if _str == '-':
        return float(0)
    _str = _str.replace(',', '.')
    return float(_str)

mounth_numeric = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}

scripts_names = ["corn_br.py", "corn_usd.py", "crops_data.py", "dolar.py"]
