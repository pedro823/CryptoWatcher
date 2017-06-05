import http.client as cl
import matplotlib.pyplot as plt
import json
from sys import argv
import re

# # #
# Removes unnecessary whitespace from archive
#
# # #
def remove_whitespace(file_name = "history.json"):
    a = None
    with open(file_name, 'r') as f:
        a = "".join(f.readlines())
    a = re.sub(r'\s+', ' ', a)
    with open(file_name, 'w') as f:
        f.write(a)

# # #
# Fetches current cryptocoin values in USD and BRL from coinmarketcap
# and dumps into @file_name
# @return void
# # #
def fetch_JSON(file_name = "history.json"):
    # Creates connection to server
    connection = cl.HTTPConnection("api.coinmarketcap.com", 80)
    connection.set_debuglevel(1)
    # Requests for API
    connection.request("GET", "/v1/ticker/?convert=BRL&limit=20")
    # Decodes response into utf-8
    response = connection.getresponse().read().decode("utf-8")
    with open(file_name, 'a') as f:
        # Writes to file
        f.write(response + "\n")


if __name__ == "__main__":
    try:
        fetch_JSON(argv[1])
    except IndexError:
        fetch_JSON()
