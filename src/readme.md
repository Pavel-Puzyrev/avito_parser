# Install
```
pip install -r requirements.txt
```
# Use
0. To create an HTML file, open the Avito advertisements page, filter, sort and press ctrl+s. Next, select “Web page, HTML only” and save file as shown in Project structure example.
1. Create an AvitoParser object and use the html file path as a parameter.
2. Call .get_price_list_from_file to get the price of each ads on the page. Result can be added to solve pagination issue.
3. Call .get_stats to get print statistics: ad count, mean price, max, min, std deviation and percintile.
```
 ---=== СТАТИСТИКА ===--- 

count         19.0
mean     19,657.89
std       5,517.78
min       12,000.0
10%       14,600.0
25%       16,000.0
50%       19,000.0
75%       21,500.0
90%       25,400.0
max       35,000.0
```



# Project structure example

+---src

|   avito_parser.py

|   rent_1fl_in_NN.html

# Code example
```
parse_file = src.avito_parser.AvitoParser("rent_1fl_in_NN.html")
parse_file.get_stats(parse_file.get_price_list_from_file())
```