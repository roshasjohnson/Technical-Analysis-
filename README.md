# Technical-Analysis-



## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/roshasjohnson/Technical-Analysis-.git
     
    ```
2. Navigate to the project directory:
    ```bash
    cd Technical-Analysis
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up API keys:
        - Obtain the necessary API keys from the News API
        - Edit the `.env` file in the project directory and add the keys in the following format:

            ```
            API_KEY=your_news_api_key
            ```
        - Replace `your_api_key` and `your_news_api_key` with your actual API keys.



## Usage



1. Run the following scripts in order:

    ```bash
    python3 reddit_scraper.py
    python3 news_scraper.py
    python3 perform_analysis.py

    ```




