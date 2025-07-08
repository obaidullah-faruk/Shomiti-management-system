from datetime import date


def next_month_date():
    """
    Finds out the first date of the next month
    Returns:
        date: first date of the next month
    """
    today = date.today()
    year = today.year + (today.month // 12)
    month = today.month % 12 + 1
    return date(year, month, 1)


def today_date():
    """
    Today's date
    Returns:
        date: today
    """
    return date.today()
