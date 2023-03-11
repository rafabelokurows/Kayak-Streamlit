import os
import pandas as pd

from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(filename='basedosdados-370918-34da29e1c968.json',
                                                                    scopes=['https://www.googleapis.com/auth/cloud-platform'])

#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'basedosdados-370918-1ce12b915c7f.json'



#client = bigquery.Client()
#query_job = client.query(sql_query)

sql_query = """
SELECT station_id,name,dockcount
FROM `bigquery-public-data.san_francisco.bikeshare_stations`
LIMIT 50
"""
df = pd.read_gbq(credentials=credentials,query=sql_query)

print(df.head())

