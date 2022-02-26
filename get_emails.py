from readline import set_completion_display_matches_hook
from openpyxl import Workbook
from bs4 import BeautifulSoup
import requests
from get_restaurants import restaurant_urls
import re

#responses = []
# for restaurant_url in restaurant_urls:
#    response = requests.get(restaurant_url).text
#    responses.append(response)
response = requests.get(restaurant_urls[0]).text

# for response in responses:
doc = BeautifulSoup(response, "html.parser")
sections = doc.find_all("section")
for section in sections:
    print(section.find_all("a"))
    print("")
    print("")

# todo: z urlYelp ziskat urlRestaurant
# todo: z urlRestaurant ziskat email
# todo: email ulozit do excelu
# DONE
