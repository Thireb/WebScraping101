from datetime import datetime
import json
from gnews import GNews
import pandas as pd
import json
news = GNews()
news.start_date = (2019,1,1)
news.end_date = (2020,1,1)

output = news.get_news('Electric Vehicle')
#print(type(output))
json_string = json.dumps(output)
json_red = pd.read_json(json_string)
json_red.to_csv('csv_out.csv')
dframe = pd.read_csv('csv_out.csv')
date_col = dframe['published date']
for item in date_col:

    date_string = str(item).rstrip()
    datetime_object = datetime.strptime(
        date_string, "%a %b %d %Y %H:%M:%S %Z%z").strftime("%Y-%m-%d %H:%M:%S")
    print(datetime_object)
    #print(date_col[:10])