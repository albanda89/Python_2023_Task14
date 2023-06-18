from library.apifunctions import get_public_holidays, find_most_holidays_month, find_country_with_most_long_weekends
from library.models.publicholiday import PublicHoliday

list_of_public_holiday = get_public_holidays(2024, "DE")
month_with_most_holidays = find_most_holidays_month(list_of_public_holiday)
print('Month with most holidays: ' + str(month_with_most_holidays))

list_of_countries = ['FI', 'FR', 'GB', 'IT']
country_with_most_long_weekends = find_country_with_most_long_weekends(2024, list_of_countries)
print('Country with most long weekends: ' + str(country_with_most_long_weekends))





