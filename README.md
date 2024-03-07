# Crypto API Data Collection and Analysis

This project automates the retrieval of cryptocurrency data from CoinMarketCap's API and analyzes it using Python. The code retrieves the latest cryptocurrency listings, including details such as price, market cap, and percentage changes over different time intervals. It then organizes the data into a pandas DataFrame for easy manipulation and analysis.

## Features

- **Automated Data Retrieval:** The script retrieves cryptocurrency data from CoinMarketCap's API at regular intervals using a function.
- **Data Storage:** The retrieved data is stored in a CSV file for future reference and analysis.
- **Data Analysis:** The script calculates and visualizes the percentage changes in cryptocurrency prices over different time intervals (1 hour, 24 hours, 7 days, 30 days, 60 days, and 90 days) using pandas and seaborn libraries.

## Instructions

1. **Clone the repository:** `git clone https://github.com/yourusername/crypto-api.git`
2. **Install dependencies:** Ensure you have Python installed, along with the required libraries (`pandas`, `seaborn`, `matplotlib`, `requests`).
3. **Update API key:** Replace the placeholder API key in the script with your own CoinMarketCap API key.
4. **Run the script:** Execute the script to start retrieving and analyzing cryptocurrency data.
5. **View results:** Check the generated CSV file for stored data and the plotted visualizations for insights.

## Files Included

- `crypto_api.py`: Python script for automating data retrieval and analysis.
- `api.csv`: CSV file containing stored cryptocurrency data.
- `README.md`: Detailed instructions and overview of the project.

## Dependencies

- Python 3.x
- pandas
- seaborn
- matplotlib
- requests

## Future Enhancements

- Incorporate additional data analysis techniques.
- Improve visualization options for better insights.
- Implement alerts for significant price changes.

Feel free to contribute or provide feedback to enhance the functionality and usefulness of this project!
