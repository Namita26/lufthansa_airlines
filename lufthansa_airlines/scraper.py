"""
author: Namita Maharanwar
Date: 11 May, 2015
"""
import sys
import requests
import hashlib
from bs4 import BeautifulSoup
from datetime import datetime
from airlines.models import LinksInformation


def get_soup(link):
    """
    Return the BeautifulSoup object for input link
    """
    request_object = requests.get(link, auth=('user', 'pass'))
    soup = BeautifulSoup(request_object.content)
    print request_object.status_code
    return soup


def get_status_code(link):
    """
        Return the error code for any url
        param: link
    """
    try:
        error_code = requests.get(link).status_code
    except requests.exceptions.ConnectionError:
        error_code = 000
    return error_code


def hash_function(link):
    """
        Creates hash for any url
        param: link
    """
    hash = hashlib.sha1(link.encode()).hexdigest()
    return hash


def find_internal_urls(lufthansa_url, depth=0, max_depth=2):
    status_dict = {}
    soup = get_soup(lufthansa_url)
    a_tags = soup.findAll("a", href=True)

    if depth > max_depth:
        return {}

    for a_tag in a_tags:
        if "http" not in a_tag["href"] and "/" in a_tag["href"]:
            url = "http://www.lufthansa.com" + a_tag['href']
        elif "http" in a_tag["href"]:
            url = a_tag["href"]
        else:
            continue
        status_dict["url"] = url
        status_dict["status_code"] = get_status_code(url)
        status_dict["timestamp"] = datetime.now()
        status_dict["depth"] = depth + 1
        status_dict["hash"] = hash_function(url)
        insert_in_db(status_dict)


def insert_in_db(status_dict):
    """
        Insert data to database
    """
    table_oject = LinksInformation(
        link=status_dict["url"],
        status=status_dict["status_code"],
        time_of_verification=status_dict["timestamp"],
        level=status_dict["depth"],
        url_hash=status_dict["hash"]
    ).save()


def insert_level_two():
    """
        Insert all level 2 urls and their info into the database
    """
    lobj = LinksInformation.objects.all()
    for i in lobj:
        find_internal_urls(i.link)

if __name__ == "__main__":
    find_internal_urls(sys.argv[1])
    insert_level_two()
