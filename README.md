# StockXSneakers

Using the StockX API available at https://stockx.com/api/browse?page=1&productCategory=sneakers

As of now the point of this repo is to provide a dataset with all sneakers that are available StockX.
Explorations and insights into this data are soon to come.

Inspiration from my web scraping experiments found in https://github.com/ReubenMathew/DataOpsExperiments

Notes:
1. If compiler throws a HTTP error from urllib package, delete cookies and run Pagination
2. API getting really depends on internet speed

ToDo:
1. Utilize market JSON object for price data
2. Explore data
3. Use the data I guess...
4. IMPORTANT!!! Move getData_API.py to some hosting thing where it can automatically run and not depend on home internet speeds
