import json
import os
import wikipedia
from requests import get
from bs4 import BeautifulSoup

wikipedia.set_lang("en")

def search_engine(word):
    tempword=word
    #Define the URL
    url = 'https://www.amazonaws.cn/en/products/'
    response = get(url)
    #print(response.text[:500])
    
    #Once we have the response from the website we are going to use BeautifulSoup to format the result.
    #Beautiful Soup is a Python library for pulling data out of HTML and XML files.
    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)
    #No we are going to extract the div that contains the product descriptions
    Service_containers = html_soup.find_all('div', class_ = 'columnbuilder parbase section')
    #Print for test
    print type(Service_containers)    

    #Our list contains None attribute, so we need to delete them first
    service_definition=[]
    
    for i in range(len(Service_containers)):
        if Service_containers[i].p.string is not None:
            service_definition.append(Service_containers[i].p.string)

    for y in range(len(service_definition)):
        str1=service_definition[y]
        if word.lower() in str1.lower():
                word=service_definition[y]
                break    
        
    if tempword == word:    
      word=wikipedia.summary(word ,sentences=1)

    return word


def lambda_handler(event, context):
	data_input=event['currentIntent']['slots']['Request']
	search_key=search_engine(data_input)
	response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
              "contentType": "SSML",
              "content": " {kelma}".format(kelma=search_key)
            }
        }
    }
	return response
