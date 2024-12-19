import pandas as pd
import cbsodata

# Show an overview of all cbs data available for download
print(pd.DataFrame(cbsodata.get_table_list()))

# Downloading of a specific table
ID = '84783NED'
data = pd.DataFrame(cbsodata.get_data(ID))
print(data)