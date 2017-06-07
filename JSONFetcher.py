import http.client as cl
import json
from sys import argv
import re
import time

# # #
# Removes unnecessary whitespace from archive.
# # #
def remove_whitespace(file_name = "visualizer/history.json"):
    a = None
    with open(file_name, 'r') as f:
        a = "".join(f.readlines())
    a = re.sub(r'\s+', ' ', a)
    with open(file_name, 'w') as f:
        f.write(a)

# # #
# TODO: Creates JSON the proper way
# The same way as described in format_JSON
# # #
def create_JSON(new_json, file_name):
    arr_out = []
    timestamp = int(time.time())
    new_json = json.loads(new_json)
    for i in new_json:
        arr_out.append({
            "type" : "line",
            "name" : i["symbol"],
            "dataPoints" : [{
                "x" : timestamp,
                "y" : float(i["price_brl"])
            }]
        })
    return json.dumps(arr_out, indent = 4)

# # #
# Formats JSON the proper way:
# {
#   "type": "line",
#   "name": "BTC"
#   "dataPoints": [
#       {
#            "x": "2017-10-5",
#           "y": valor_em_reais,
#       },
#   ],
# }
# # #
def format_JSON(new_json, file_name):
    try:
        with open(file_name, 'r') as f:
            old_json = json.load(f)
        new_json = json.loads(new_json)
        timestamp = int(time.time())
        for i in new_json:
            price_brl = float(i["price_brl"])
            actual = { "x" : timestamp, "y" : price_brl }
            for j in old_json:
                if i["symbol"] == j["name"]:
                    j["dataPoints"].append(actual)
                    break
        formatted_json = json.dumps(old_json, indent = 4)
        return formatted_json
    except FileNotFoundError:
        return create_JSON(new_json, file_name)



# # #
# Fetches current cryptocoin values in USD and BRL from coinmarketcap
# and dumps into @file_name
# @return void
# # #
def fetch_JSON(file_name = "visualizer/history.json"):
    # Creates connection to server
    connection = cl.HTTPConnection("api.coinmarketcap.com", 80)
    connection.set_debuglevel(1)
    # Requests for API
    connection.request("GET", "/v1/ticker/?convert=BRL&limit=20")
    # Decodes response into utf-8
    response = connection.getresponse().read().decode("utf-8")
    actual_json = format_JSON(response, file_name)
    with open(file_name, 'w') as f:
        # Writes to file
        f.write(actual_json + '\n')


if __name__ == "__main__":
    try:
        fetch_JSON(argv[1])
    except IndexError:
        fetch_JSON()
