#!/usr/bin/env python
# coding: utf-8

# In[311]:


# Week 3

import urllib
import csv
from datetime import datetime
import re
import logging
import urllib.request
import argparse

log = []
hours = {}

    # PART I (PULLING DOWN WEB LOG FILE)

def main():
    parser.add_argument("--url", 
                        default = "http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv", 
                        type = str)
    args = parser.parse_args()
    downloadData(str(args.url) if args.url != None else sys.exit())

if __name__ == "__main__":
    
    # PART II (DATA DOWNLOADING AND PROCESSING (PROCESS FILE USING CSV))
    
    def downloadData(url):
        dwnld = url
        urllib.request.urlretrieve(dwnld, 'weblog.csv')
        
    def processData(data):
        #logging.basicConfig(filename = 'logs.log', 
                            #format = '%(asctime)s %(message)s', 
                            #filemode = 'w')
        
        reader = csv.reader(data)
        for row in reader:
            path = row[0]
            datetimeAccesed = row[1]
            browser = row[2]
            statusofRequest = row[3]
            size = row[4]
            log.append((path, datetimeAccesed, browser, statusofRequest, size))
            
    # PART III (SEARCHING FOR IMAGE HITS)
            
    def imageSearch():
        n = 0
        for data in range(len(log)):
            if re.findall(".jpg|.gif|.png|.JPG|.GIF|.PNG", log[data][0]): # ALL IMAGE FILES
                n += 1
        print ("Image requests account for "+str((n/len(log)*100))+"% of all requests")
        
    # PART IV (FINDING THE MOST POPULAR BROWSER)
                
    def popularBrowser():
        firefox = 0
        chrome = 0
        explorer = 0
        safari = 0
        for data in range(len(log)):
            if re.findall("firefox|Firefox", log[data][2]):
                firefox += 1
            if re.findall("chrome|Chrome", log[data][2]):
                chrome += 1
            if re.findall("internet explorer|Internet Explorer", log[data][2]):
                explorer += 1
            if re.findall("safari|Safari", log[data][2]):
                safari += 1
        if (max(firefox, chrome, explorer, safari) == firefox):
                print ("The most popular browser is Firefox")
        if (max(firefox, chrome, explorer, safari) == chrome):
                print ("The most popular browser is Chrome")
        if (max(firefox, chrome, explorer, safari) == explorer):
                print ("The most popular browser is Internet Explorer")
        if (max(firefox, chrome, explorer, safari) == safari):
                print ("The most popular browser is Safari")
        else:
            sys.exit()
            
    # PART V (EXTRA CREDIT)
            
    def listofHours():
        for data in range(len(log)):
            # datetime_str = "1/27/2014 00:00"
            # ValueError: time data '2014-01-27 00:00:01' does not match format '%m-%d-%Y %H:%M:%S'
            # datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
            time = datetime.strptime(log[data][1], "%Y-%m-%d %H:%M:%S")
            if int(time.hour) in hours:
                hours[int(time.hour)] = hours[int(time.hour)] + int(log[data][3])
            else:
                hours[int(time.hour)] = int(log[data][3])    
        for keys in hours:
            print ("Hour "+str(keys)+" has "+str(hours[keys])+" hits")
    
# TESTS
    
url = "http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv"
downloadData(url)
file = open('weblog.csv')
processData(file)
imageSearch()
popularBrowser()
listofHours()
