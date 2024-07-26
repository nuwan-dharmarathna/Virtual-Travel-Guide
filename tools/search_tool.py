from langchain.tools import tool

import os
from dotenv import load_dotenv

import requests
import json

load_dotenv()

class SearchTool():
    @tool("search the internet")
    def search_internet(query):
        """ Useful to search the internet
        about a a given topic and return relevant results
        """
        top_result_to_return = 4
        
        url = "https://google.serper.dev/search"
        payload = json.dumps({ "q": query })
        headers = {
            'X-API-KEY': os.getenv("SERPER_API_KEY"),
            'Content-Type': 'application/json'
            }
        response = requests.request("POST", url, headers=headers, data=payload)
        
        #check if there in an organic key
        if 'organic' not in response.json():
            return "Sorry, I couldn't find anything about that, there could be an error with you serper api key."
        else:
            results = response.json()['organic']
            string = []
            for result in results[:top_result_to_return]:
                try:
                    string.append('\n'.join([
                        f"Title: {result['title']}",
                        f"Link: {result['link']}",
                        f"Snippet: {result['snippet']}",
                        "\n-----------------------------"
                    ]))
                except KeyError:
                    next
            return '\n'.join(string)