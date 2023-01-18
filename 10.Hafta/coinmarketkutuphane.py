from cryptocmd import CmcScraper

scraper = CmcScraper("XRP", "15-10-2017", "25-10-2017")
headers, data = scraper.get_data()
json_data = scraper.get_data("json")
scraper.export("csv")
df = scraper.get_dataframe()