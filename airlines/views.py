"""
@author: Namita Maharanwar
function which returns all the URLS according to the status code
"""

import json
from airlines.models import LinksInformation


def fetch_url_information(status_code):
    """
        Returns the urls from database having status code equal to inputed status
        param: status_code
    """
    links = []
    result = {}
    obj = LinksInformation.objects.filter(status=status_code)
    for i in obj:
        links.append(i.link)
    result["result"] = links
    json.dump(result, open("airlines/links.json", "w"), indent=4)
    return result

if __name__ == "__main__":
    print fetch_url_information(504)
