import datetime
from fetch_data import fetch_data
from store_data import store_data


def nessus_data_clone():
    end_date = datetime.datetime.today()
    start_date = end_date - datetime.timedelta(days=1)
    while start_date != datetime.datetime(1950, 1, 1):  # old enough date for bulk fetch and store
        data = fetch_data(start_date, end_date)
        store_data(data)
        del data
        end_date = start_date
        start_date = end_date - datetime.timedelta(days=1)


nessus_data_clone()
