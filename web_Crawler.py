""" 
Below is a simple web crawler 
Name: Isha Angadi 
Total time to code: 1.5 hours
"""
import requests 
import re
from bs4 import BeautifulSoup 

#Ask the user for an input, we assume the input will be valid
URL = input ("Please enter a valid URL: ") 

#We create a regex pattern to match to the http and https websites to explore while web crawling 
regex_pattern = '^(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})'

#Send a HTTP request to the URL of the webpage entered by the user
r = requests.get(URL) 

#We use BeautifulSoup to create & navigate the parse tree of the URL entered
soup = BeautifulSoup(r.content, 'html5lib') 

print("The URLs found are: \n")
#As specified, we find the URLs inside a href attribute of URL 
for l in soup.find_all('a'):
    if l.has_attr('href'):
        link = l.attrs['href']
        #We find all the matching URLs 
        pattern = re.findall(regex_pattern, link) 
        #We loop through the list of matched patterns and print to standard output 
        for word in pattern: 
            print(word)

