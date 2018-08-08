import json
import wikipedia

wikipedia.set_lang("en")

def search_engine(word):
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
