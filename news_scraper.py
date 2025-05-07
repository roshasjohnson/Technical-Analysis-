import requests
import pandas as pd
import yake
import os
from dotenv import load_dotenv
    
load_dotenv()

API_KEY  = os.getenv("API_KEY")



def extract_keywords(text):
    kw_extractor = yake.KeywordExtractor(lan="en", n=1, top=5)
    keywords = kw_extractor.extract_keywords(text)
    return ' '.join([kw[0] for kw in keywords])



def load_reddit_data():
    
    """
    Load the Reddit data from an Excel file.
    """     
    try:
        
        df = pd.read_excel('data/reddit_data.xlsx')
        # Extract the titles from the DataFrame
        titles = df['title'].tolist()
        return titles
    
    except FileNotFoundError:
        
        print("File not found. Please ensure the file exists.")
        return None
    
    
       
def extract_keywords_from_titles(titles):
    """
    Extract keywords from the titles using YAKE.
    """
    keywords = []
    
    for title in titles:
        keyword = extract_keywords(title)
        keywords.append(keyword)
    
    return keywords




def call_news_apis(keywords):
    
    """
    Call the News API with the specified keywords.
    """
    
    news_set = []
    
    
    for keyword in keywords:
        
        try :
            
            url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={API_KEY}&pageSize=5"
            
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                
                if data['status'] == 'ok':
                    articles = data['articles']
                    
                    for article in articles:
                        news_set.append({
                            'title': article['title'],
                            'source_name': article['source']['name'],
                            'published_date': article['publishedAt'],
                            'article_url': article['url']
                        })
                        print(f"Keyword: {keyword}")
                        print(f"Title: {article['title']}, Source: {article['source']['name']}, Published Date: {article['publishedAt']}, URL: {article['url']}")

                    print(f"Total articles for keyword '{keyword}': {len(articles)}")
                    print("-------------------------------")
                    
                else:
                
                    print(f"Error: {data['message']}")
            else:   
                               
                print(f"Error: Status:{response.status_code}, Response:{response.text}")
    
    
           
        except Exception as e:
            print(f"Error in API call: {e}")
            continue
        
        # print(news_set)
    return news_set



def load_news_data(news_set):
    
    """
    Load the news data into an Excel file.
    """
    
    df = pd.DataFrame(news_set)
    

    df.to_excel('data/news_data.xlsx', index=False)
    print("News data saved to data/news_data.xlsx")

titles = load_reddit_data()

if titles:
    
    keywords = extract_keywords_from_titles(titles)
    news_set = call_news_apis(keywords)
    load_news_data(news_set)
    

