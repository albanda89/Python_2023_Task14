import requests
from datetime import datetime
from library.models.publicholiday import PublicHoliday
from typing import List


def get_public_holidays(year, country_code): 

    url = "https://date.nager.at/api/v3/PublicHolidays/" + str(year) + "/" + country_code
    payload = {}
    headers = {
    'accept': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    list_of_holidays_dict = response.json()  

    list_of_public_holiday = []
    for holiday in list_of_holidays_dict:
      tmp_pub_holiday = PublicHoliday(holiday)
      list_of_public_holiday.append(tmp_pub_holiday)

    return list_of_public_holiday
    

def find_most_holidays_month(list_of_public_holiday: list):

    public_holidays_by_month_dict = {}

    for public_holiday in list_of_public_holiday:
        date_obj = datetime.strptime(public_holiday.date, '%Y-%m-%d').date()
        month = date_obj.month
        
        number_of_public_holidays = 0
        if month in public_holidays_by_month_dict :
            number_of_public_holidays = public_holidays_by_month_dict.get(month)
        
        public_holidays_by_month_dict.update({month: number_of_public_holidays+1})

    print(public_holidays_by_month_dict)
    return max(public_holidays_by_month_dict, key=lambda k: public_holidays_by_month_dict[k])


def find_country_with_most_long_weekends(year: int, list_of_countries: list):

    long_weekends_by_country_dict = {}

    for country in list_of_countries:
        url = "https://date.nager.at/api/v3/LongWeekend/" + str(year) + "/" + country
        payload = {}
        headers = {
        'accept': 'application/json'
        }
        response = requests.request("GET", url, headers=headers, data=payload)

        list_of_long_weekends_dict = response.json()  
        long_weekends_by_country_dict.update({country:len(list_of_long_weekends_dict)})

    print(long_weekends_by_country_dict)
    return max(long_weekends_by_country_dict, key=lambda k: long_weekends_by_country_dict[k])
