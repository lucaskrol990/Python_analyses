# Query data
To query data from CBS follow this procedure:
* Select data from CBS to query and get its ID. This can be done in two methods:
    * Go to the [CBS website](https://opendata.cbs.nl/#/CBS/nl/) and look for the dataset of your interest. In the url you will see something like https://opendata.cbs.nl/#/CBS/nl/dataset/83140NED/XXXXX, where the 83140NED is the ID of the dataset
    * List all tables that CBS provides using pd.DataFrame(cbsodata.get_table_list()) and select the dataset of your interest
* Query the data using the previously found ID: pd.DataFrame(cbsodata.get_data(ID))

An example can be found in Query data.py
    
