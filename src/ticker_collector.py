import requests
from bs4 import BeautifulSoup

class TickerCollector:
    def __init__(self):
        self.sources = {
            'Yahoo Finance': 'https://finance.yahoo.com/quote/^BIST100',
            'Investing.com': 'https://www.investing.com/indices/turkey-100',
            'Borsa Istanbul': 'https://borsaistanbul.com/en/indices'
        }
        self.tickers = []

    def collect_tickers(self):
        for source, url in self.sources.items():
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')

                if source == 'Yahoo Finance':
                    self.tickers.extend(self._parse_yahoo(soup))
                elif source == 'Investing.com':
                    self.tickers.extend(self._parse_investing(soup))
                elif source == 'Borsa Istanbul':
                    self.tickers.extend(self._parse_borsa(soup))
            except Exception as e:
                print(f'Error fetching data from {source}: {e}')

    def _parse_yahoo(self, soup):
        tickers = []
        # Example parsing logic; refine according to actual HTML structure
        ticker_elements = soup.find_all('a', {'data-symbol': True})
        for ticker in ticker_elements:
            tickers.append(ticker.text)
        return tickers

    def _parse_investing(self, soup):
        tickers = []
        # Example parsing logic; refine according to actual HTML structure
        ticker_elements = soup.find_all('a', {'class': 'instrument-name'})
        for ticker in ticker_elements:
            tickers.append(ticker.text)
        return tickers

    def _parse_borsa(self, soup):
        tickers = []
        # Example parsing logic; refine according to actual HTML structure
        ticker_elements = soup.find_all('div', {'class': 'market-symbol'})
        for ticker in ticker_elements:
            tickers.append(ticker.text.strip())
        return tickers

    def get_tickers(self):
        return self.tickers

if __name__ == '__main__':
    collector = TickerCollector()
    collector.collect_tickers()
    print(collector.get_tickers())