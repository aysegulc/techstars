
Techstars Scraping Project
-------------------------

This scrapy project is built to extract Techstars portfolio companies.

Details such as company name, funding, status, location, description and logo url are extracted for each company.

Scraped items can be saved as json or csv files.


```bash
# Save items to csv file
scrapy crawl techstars -o techstars_data.csv
# save items to json file
scrapy crawl techstars -o techstars_data.json
```
