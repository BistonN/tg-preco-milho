def format_number(_number:str, _characters:int):
    results = _number
    i = 0
    while i < _characters:
        if len(str(results)) >= _characters:
            return str(results)
        results = '0' + str(results)
        i = i + 1

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
