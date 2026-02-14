# Market Sentiment Bot 📈

A Python-based tool that scrapes financial news headlines, analyzes their sentiment using Google's Gemini API, and generates detailed reports with visualizations.

## Features

-   **News Scraping**: Fetches the latest headlines for any stock ticker using Google News RSS.
-   **Sentiment Analysis**: Uses the Gemini 1.5 Flash model to score headlines from -1 (Negative) to +1 (Positive).
-   **Visualizations**: Generates sentiment distribution plots.
-   **Data Export**: Saves all analyzed data to CSV for further processing.
-   **CLI Interface**: Easy-to-use command line interface with rich text output.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/DarkWaterReflection/market-sentiment-bot.git
    cd market-sentiment-bot
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure API Key:**
    -   Get a Google Gemini API key from [Google AI Studio](https://aistudio.google.com/).
    -   Rename `.env.example` to `.env` (or create a new `.env` file).
    -   Add your key:
        ```text
        GEMINI_API_KEY=your_actual_api_key_here
        ```

## Usage

Run the bot by providing a stock ticker symbol:

```bash
python main.py AAPL
```

Or for other stocks:
```bash
python main.py TSLA
python main.py NVDA
```

## Output

The tool will create a `data/` directory containing:
-   `{TICKER}_sentiment_{TIMESTAMP}.csv`: Raw data with sentiment scores and reasoning.
-   `{TICKER}_sentiment_plot_{TIMESTAMP}.png`: A histogram showing the distribution of sentiment.

## Project Structure

-   `src/`: Source code for scraper, analyzer, and reporter.
-   `tests/`: Unit tests.
-   `main.py`: Entry point.
-   `requirements.txt`: Python dependencies.

## License

MIT
