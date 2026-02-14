import feedparser
import time

class NewsScraper:
    def __init__(self):
        # Google News RSS URL for searching
        self.base_url = "https://news.google.com/rss/search?q={}&hl=en-US&gl=US&ceid=US:en"

    def fetch_news(self, ticker):
        """
        Fetches news headlines for a given ticker from Google News RSS.
        
        Args:
            ticker (str): The stock ticker (e.g., 'AAPL', 'GOOGL').
            
        Returns:
            list: A list of dictionaries containing 'title', 'link', and 'published'.
        """
        print(f"Fetching news for {ticker}...")
        try:
            # Construct the query URL
            url = self.base_url.format(ticker)
            feed = feedparser.parse(url)
            
            headlines = []
            # Limit to top 15 entries to avoid overwhelming the model
            for entry in feed.entries[:15]:
                headlines.append({
                    'title': entry.title,
                    'link': entry.link,
                    'published': entry.published
                })
            
            print(f"Found {len(headlines)} headlines.")
            return headlines
        except Exception as e:
            print(f"Error fetching news for {ticker}: {e}")
            return []

if __name__ == "__main__":
    # Test execution
    scraper = NewsScraper()
    news = scraper.fetch_news("AAPL")
    for item in news:
        print(f"- {item['title']} ({item['published']})")
