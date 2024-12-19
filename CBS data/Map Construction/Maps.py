import pandas as pd
import geopandas as gpd
import cbsodata
import requests
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from io import BytesIO
import re

'''
Options
'''
year = 2019 # Year of CBS datatable, this also implies the year of your geographical data
pd.set_option('display.max_columns', None) # Display all columns of potential dataframes printed

'''
Load in CBS datatable
'''
# Downloading of a specific table
ID = '84783NED' # Containing details on
data = pd.DataFrame(cbsodata.get_data(ID))

# Filter for specific columns
data = data[data['BedrijfstakkenWoningen'] == 'Alle economische activiteit en woningen']
data = data[data['Perioden'] == '2019']

# Drop provinces and SubRES regions:
data = data[~data['RegioS'].str.contains(r'\(PV\)|\(ET\)', regex=True, na=False)]

# For some municipalities there are clarifications in parentheses: we remove them here
data['RegioS'] = data['RegioS'].apply(
    lambda x: re.sub(r'\(.*\)', '', x).strip() if 'Bergen' not in x else x
)

'''
Load in geographical data
'''
# Retrieve the polygons describing the municipalities in the Netherlands
geodata_url = f'https://service.pdok.nl/cbs/gebiedsindelingen/2019/wfs/v1_0?request=GetFeature&service=WFS&version=1.1.0&outputFormat=application%2Fjson&typeName=gebiedsindelingen:gemeente_niet_gegeneraliseerd'
response = requests.get(geodata_url)
if response.status_code == 200:
    # Read the content as a GeoDataFrame using GeoPandas
    municipality_borders = gpd.read_file(BytesIO(response.content))
else:
    raise Exception(f"Failed to retrieve municapality border data: {response.status_code}")

'''
Merge geographical data with CBS data
'''
combined_df = pd.merge(municipality_borders, data,
                           left_on = "statnaam", right_on = "RegioS", how = 'left')
rows_with_na = combined_df[combined_df.isna().any(axis=1)]
if not rows_with_na.empty: # If data not complete
    print(rows_with_na)
    raise Exception("There are rows which do not have data associated with them, see above. "
                    "Please consider if this makes sense and remove this exception accordingly")

'''
Plot a map
'''
p = combined_df.plot(column='AantalInstallaties_1', figsize = (10,8), legend=True,
                     legend_kwds={'label': "Number of solar installations per municipality",
                                  'orientation': "horizontal"})
p.axis('off')
p.set_title('Number of solar installations per municipality, 2019')
plt.savefig('Solar_installations_2019.png')
plt.show()