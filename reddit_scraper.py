import requests
import json


URL  = "https://www.reddit.com"
SUBREDDIT= "technology"

def call_reddit_api():
    """
    Call the Reddit API to get the top posts from a subreddit.
    """
    
    try:
        
        headers = {
            'User-Agent': 'RedditScraper/1.0'}
        response = requests.get(f"{URL}/r/{SUBREDDIT}/top.json?limit=100", headers=headers)
        
        if response.status_code == 200:
            print("Success!")
            return response.json()
        
        else:
            print(f"Error: Status:{response.status_code}, Response:{response.text}")
            return None
        
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    
    
    
    
def extract_reddit_data(data):
    """
    Extract the title and URL from the Reddit API response.
    """
    extracted_data = []
    
    
    for post in data['data']['children']:
        title = post['data']['title']
        url   = URL + post['data']['permalink']
        print(url)

        
        
    
    
        
    
    
    

def load_to_excel(data):    
    """
    Save the extracted data to an Excel file.
    """
    


    
result  = call_reddit_api()

if result:
    
    
    extracted_data = extract_reddit_data(result)
    
    load_to_excel(extracted_data)
    
    
    
    