import pandas as pd
import datetime
from math import ceil


def week_of_month(dt):
    """ Returns the week of the month for the specified date.
    """
    first_day = dt.replace(day=1)
    dom = dt.day
    adjusted_dom = dom + first_day.weekday()
    return int(ceil(adjusted_dom/7.0) - 1)


monthly_forecast_data = {
    'RID': [],
    'Personnel Number': [],
    'Resource Name': []
}


def transform_data():
    df = pd.read_excel('../data/Forecast.xlsx').fillna(0)
    for idx, row in df.iterrows():
        flag = 0
        for index, value in row.items():
            if index == 'RID' or index == 'Personnel Number' or index == 'Resource Name':
                monthly_forecast_data[index].append(value)

            if isinstance(index, datetime.date):
                wom = week_of_month(index)
                if f'{index.year}/{index.month}' in monthly_forecast_data:
                    if wom == 1:
                        flag = 0
                    value = flag + value
                    flag = value
                    if idx:
                        monthly_forecast_data[f'{index.year}/{index.month}'].append(
                            value)
                        monthly_forecast_data[f'{index.year}/{index.month}'][idx] = value
                        monthly_forecast_data[f'{index.year}/{index.month}'] = monthly_forecast_data[f'{index.year}/{index.month}'][:idx+1]
                    else:
                        monthly_forecast_data[f'{index.year}/{index.month}'][idx] = value
                else:
                    monthly_forecast_data[f'{index.year}/{index.month}'] = []
                    flag = 0
                    value = flag + value
                    flag = value
                    monthly_forecast_data[f'{index.year}/{index.month}'].append(
                        value)


transform_data()
print(monthly_forecast_data)
monthly_forecast_df = pd.DataFrame(monthly_forecast_data)

monthly_forecast_df
