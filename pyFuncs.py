import datetime

def get_date():
    date = datetime.datetime.now()
    return (f"{date.year}-{date.month}-{date.day} {date.hour}:{date.minute}")
