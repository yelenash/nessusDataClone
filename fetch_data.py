import vulners
from config import nessus_data_config


def fetch_data(start_date, end_date):
    vulners_api = vulners.Vulners(api_key=nessus_data_config["api_key"])
    print(start_date)
    print(end_date)
    data = vulners_api.archive("nessus", start_date=start_date.strftime('%Y-%m-%d'),
                               end_date=end_date.strftime('%Y-%m-%d'))
    return data
