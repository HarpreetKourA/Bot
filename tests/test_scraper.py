import pytest
from src.scraper import NewsScraper
from unittest.mock import patch, MagicMock

def test_fetch_news_success():
    scraper = NewsScraper()
    with patch('feedparser.parse') as mock_parse:
        # Mock feed entry
        mock_entry = MagicMock()
        mock_entry.title = "Test Headline"
        mock_entry.link = "http://test.com"
        mock_entry.published = "Mon, 14 Feb 2026"
        
        mock_feed = MagicMock()
        mock_feed.entries = [mock_entry]
        mock_parse.return_value = mock_feed
        
        news = scraper.fetch_news("TEST")
        assert len(news) == 1
        assert news[0]['title'] == "Test Headline"

def test_fetch_news_empty():
    scraper = NewsScraper()
    with patch('feedparser.parse') as mock_parse:
        mock_feed = MagicMock()
        mock_feed.entries = []
        mock_parse.return_value = mock_feed
        
        news = scraper.fetch_news("TEST")
        assert len(news) == 0

def test_fetch_news_exception():
    scraper = NewsScraper()
    with patch('feedparser.parse') as mock_parse:
        mock_parse.side_effect = Exception("Network error")
        
        news = scraper.fetch_news("TEST")
        assert len(news) == 0
