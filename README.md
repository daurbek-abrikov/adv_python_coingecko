# adv_python_coingecko
Title:

Assignment 1 


### Installation
PyPI
```bash
pip install pycoingecko
```
or from source
```bash
git clone https://github.com/man-c/pycoingecko.git
cd pycoingecko
python3 setup.py install
```

### Usage

```python
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
```

### Examples
The required parameters for each endpoint are defined as required (mandatory) parameters for the corresponding functions.\
**Any optional parameters** can be passed using same names, as defined in CoinGecko API doc (https://www.coingecko.com/api/docs/v3)





### Examples
The required parameters for each endpoint are defined as required (mandatory) parameters for the corresponding functions.\
**Any optional parameters** can be passed using same names, as defined in CoinGecko API doc (https://www.coingecko.com/api/docs/v3)

For any parameter:
- ***Lists** are supported as input for multiple-valued comma-separated parameters\
  (e.g. see /simple/price usage examples).*
- ***Booleans** are supported as input for boolean type parameters; they can be `str` ('true', 'false'') or `bool` (`True`, `False`)\
  (e.g. see /simple/price usage examples).*

Usage examples:
```python
# /simple/price endpoint with the required parameters
>>> cg.get_price(ids='bitcoin', vs_currencies='usd')
{'bitcoin': {'usd': 3462.04}}






- *coins*
  - **/coins/list** (List all supported coins id, name and symbol (no pagination required))
    ```python 
    cg.get_coins_list()
    ```
  - **/coins/markets** (List all supported coins price, market cap, volume, and market related data)
    ```python 
    cg.get_coins_markets()
    ```
  - **/coins/{id}** (Get current data (name, price, market, ... including exchange tickers) for a coin)
    ```python 
    cg.get_coin_by_id()
    ```
  - **/coins/{id}/tickers** (Get coin tickers (paginated to 100 items))
    ```python 
    cg.get_coin_ticker_by_id()
    ```

### Test

Run unit tests with:

```
# after installing pytest using pip3
pytest tests
```


