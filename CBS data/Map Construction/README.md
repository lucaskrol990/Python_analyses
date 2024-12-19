# Map Construction
This folder explains how to construct a geographical map, populated with CBS data. To do so, you need to follow this procedure:
* Load in CBS datatable based on ID. More details on this can be found in Query Data
* Load in geographical data:
  * .json files containing specifics on municipalities can be found in the [Nationaal Georegister](https://www.nationaalgeoregister.nl/geonetwork/srv/dut/catalog.search#/search?isTemplate=n&creationDateForResource=%7B%22range%22:%7B%22creationDateForResource%22:%7B%22gte%22:null,%22lte%22:null,%22relation%22:%22intersects%22%7D%7D%7D&revisionDateForResource=%7B%22range%22:%7B%22revisionDateForResource%22:%7B%22gte%22:null,%22lte%22:null,%22relation%22:%22intersects%22%7D%7D%7D&publicationDateForResource=%7B%22range%22:%7B%22publicationDateForResource%22:%7B%22gte%22:null,%22lte%22:null,%22relation%22:%22intersects%22%7D%7D%7D&resourceTemporalDateRange=%7B%22range%22:%7B%22resourceTemporalDateRange%22:%7B%22gte%22:null,%22lte%22:null,%22relation%22:%22intersects%22%7D%7D%7D&sortBy=relevance&sortOrder=&any=gebiedsindelingen&from=1&to=50&query_string=%7B%22tag.default%22:%7B%22CBS%22:true%7D%7D)
  * Select the WFS application for your required year
  * Select the download for gemeente_gegeneralizeerd
  * Press download as JSON or application/json; subtype=geojson
  * Paste the URL of this page into your script to download the JSON
* Merge the CBS data and the geographical data and plot this

An example usage can be found in Maps.py
