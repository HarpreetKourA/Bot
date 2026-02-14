import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

class Reporter:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def save_to_csv(self, headlines, ticker):
        """Saves the analyzed headlines to a CSV file."""
        if not headlines:
            print("No data to save.")
            return None
            
        df = pd.DataFrame(headlines)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(self.data_dir, f"{ticker}_sentiment_{timestamp}.csv")
        
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
        return filename, df

    def generate_report(self, df, ticker):
        """Generates a summary report and visualization."""
        if df.empty:
            return

        avg_sentiment = df['sentiment'].mean()
        print(f"\n--- Sentiment Report for {ticker} ---")
        print(f"Average Sentiment: {avg_sentiment:.2f}")
        print(f"Positive: {len(df[df['sentiment'] > 0])}")
        print(f"Negative: {len(df[df['sentiment'] < 0])}")
        print(f"Neutral: {len(df[df['sentiment'] == 0])}")
        
        # Visualization
        plt.figure(figsize=(10, 6))
        
        # Histogram
        plt.hist(df['sentiment'], bins=20, color='skyblue', edgecolor='black')
        plt.title(f"Sentiment Distribution for {ticker}")
        plt.xlabel("Sentiment Score (-1 to +1)")
        plt.ylabel("Frequency")
        plt.axvline(avg_sentiment, color='red', linestyle='dashed', linewidth=1, label=f'Mean: {avg_sentiment:.2f}')
        plt.legend()
        
        plot_filename = os.path.join(self.data_dir, f"{ticker}_sentiment_plot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        plt.savefig(plot_filename)
        print(f"Plot saved to {plot_filename}")
        plt.close()

if __name__ == "__main__":
    # Test execution
    data = [
        {'title': 'Good news', 'sentiment': 0.8},
        {'title': 'Bad news', 'sentiment': -0.6},
        {'title': 'Okay news', 'sentiment': 0.1}
    ]
    reporter = Reporter()
    f, df = reporter.save_to_csv(data, "TEST")
    reporter.generate_report(df, "TEST")
