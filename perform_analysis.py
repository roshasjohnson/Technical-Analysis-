import pandas as pd
from difflib import get_close_matches




def load_data(reddit_path="data/reddit_data.xlsx", news_path="data/news_data.xlsx"):
    reddit_df = pd.read_excel(reddit_path)
    news_df = pd.read_excel(news_path)
    return reddit_df, news_df


def clean_data(reddit_df, news_df):
    reddit_df.columns = reddit_df.columns.str.lower()
    news_df.columns = news_df.columns.str.lower()
    news_df = news_df.rename(columns={"title": "news_title"})
    return reddit_df, news_df



def match_titles(reddit_df, news_df):
    def match_news_title(reddit_title, news_titles):
        matches = get_close_matches(reddit_title, news_titles, n=1, cutoff=0.3)
        return matches[0] if matches else None

    reddit_df['matched_news_title'] = reddit_df['title'].apply(
        lambda rt: match_news_title(rt, news_df['news_title'].dropna().tolist())
    )
    return reddit_df


def transform_data(reddit_df, news_df):
    final_df = pd.merge(
        reddit_df,
        news_df,
        left_on='matched_news_title',
        right_on='news_title',
        how='left'
    )

    output_df = final_df[[
        'title',            # Reddit post title
        'url',              # Reddit post URL
        'upvotes',
        'comments_count',
        'news_title',       # News article title
        'source_name',
        'published_date',
        'article_url'
    ]]
    output_df = output_df.dropna()
    output_df = output_df.drop_duplicates(subset=['title', 'news_title'])

    return output_df


def save_data(output_df, output_path="data/final_analysis.xlsx"):
    output_df.to_excel(output_path, index=False)
    print(f"✅ Final analysis saved to '{output_path}'")



def main():
    reddit_df, news_df = load_data()
    reddit_df, news_df = clean_data(reddit_df, news_df)
    reddit_df = match_titles(reddit_df, news_df)
    output_df = transform_data(reddit_df, news_df)
    save_data(output_df)

if __name__ == "__main__":
    main()
