#Following the method of arxiv doc: 4.1.2 Python API
#More specifically, the python 3 example.
#This is a general example of how to use the arxiv API for python 3.

import urllib.request as libreq
def general_example():
    url = "http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1"
    with libreq.urlopen(url) as url:
        r = url.read()
    print(r)
#general_example()

#######Api Research Agenda
#3.1 Search Parameters
#using search_query parameter
def search_query_eg():
    start = 0 
    max_results = 1
    search_query = "all:electron"
    url = "http://export.arxiv.org/api/query?search_query={}&start={}&max_results={}".format(search_query, start, max_results)
    with libreq.urlopen(url) as url:
        r = url.read()
    print(r)
#search_query_eg()

#using id_list parameter 
#valid structure of id_list parameter: YYDD.NNNNvV ie. YearDate:NumbervVersion
# From 0704 through 1412 it is 4-digits, starting at 0001. From 1501 onwards it is 5-digits, starting at 00001
# more details here : https://info.arxiv.org/help/arxiv_identifier.html#new
#NOTE: Its unclear why certain errors occur, empty responses or non-existent articles

def id_list_eg():
    #id_list format: YYDD.NNNN
    #NOTE: format changes based on date and number limitations respectively
    date = 706
    date = str(date).zfill(4)   #zfill is for number padding
    num = 1
    num = str(num).zfill(4)
    id = "{}.{}".format(date, num)
    url = "http://export.arxiv.org/api/query?id_list={}".format(id)
    with libreq.urlopen(url) as url:
        r = url.read()
    print(r)
#id_list_eg()

#using the start and max_results parameters
# NOTE:I think we can scratch the idea of using the OAI-PMH protocol as it doesnt retrieve article content. 
# I added a check to see how long it took the request to process.
def start_max_eg(s = 0, m = 1000):
    import time
    start = s
    max_results = m
    search_query = "all:electron"
    url = "http://export.arxiv.org/api/query?search_query={}&start={}&max_results={}".format(search_query, start, max_results)
    start_time = time.time()
    with libreq.urlopen(url) as url:
        r = url.read()
    end_time = time.time()
    print(r)
    duration = end_time - start_time
    print("TIME TO COMPLETE: {}".format(duration))
#start_max_eg()

#sortBy and sortOrder example
def sorting_eg(s = 0, m = 1000):
    import time
    sortBy = "lastUpdatedDate"  #relevance, submittedDate
    sortOrder = "ascending"     #descending
    start = s
    max_results = m
    search_query = "all:electron"
    url = "http://export.arxiv.org/api/query?search_query={}&start={}&max_results={}&sortBy={}&sortOrder={}".format(search_query, start, max_results, sortBy, sortOrder)
    start_time = time.time()
    with libreq.urlopen(url) as url:
        r = url.read()
    end_time = time.time()
    print(r)
    duration = end_time - start_time
    print("TIME TO COMPLETE: {}".format(duration))
#sorting_eg()