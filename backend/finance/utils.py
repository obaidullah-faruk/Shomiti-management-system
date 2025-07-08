from datetime import date


def next_month_date():
    today = date.today()
    year = today.year + (today.month // 12)
    month = today.month % 12 + 1
    return date(year, month, 1)


def today_date():
    return date.today()
