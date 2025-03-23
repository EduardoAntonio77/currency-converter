# Currency Converter

This Python script allows you to convert a specified amount from one currency to another using real-time exchange rates from the AwesomeAPI.

## Prerequisites
- Python 3.x installed
- `requests` library installed (if not installed, run `pip install requests`)

## How to Use
1. Clone this repository or copy the script to your local machine.
2. Run the script in your terminal or command prompt:
   ```bash
   python currency_converter.py
   ```
3. Enter the currency codes (e.g., USD, EUR, BRL) when prompted:
   ```
   De qual moeda deseja converter?: USD
   Para qual moeda deseja converter?: BRL
   Quantos USD deseja converter para BRL?: 10
   ```
4. The script will fetch the latest exchange rate and display the converted amount:
   ```
   A conversão de 10BRL para USD, $50.00
   ```

## Notes
- Ensure that the currency codes are in uppercase (e.g., USD, EUR, BRL) as required by the API.
- The script fetches exchange rates from [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas) in real time.
- If an error occurs (e.g., incorrect currency code or API issue), an error message will be displayed.

## License
This project is open-source and available under the MIT License.

