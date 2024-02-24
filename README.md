# NBA Analytica

## Overview
NBA Analytica is a Python package designed to retrieve detailed statistics for NBA players from the `stats.nba.com` API. This package simplifies the process of accessing various types of player statistics by abstracting away the API request handling and providing users with a simple function call to get the data they need in different statistical modes.

## Features
- Fetch NBA player statistics by name.
- Support for statistical modes: Per Game, Per Possession, and Per 100 Possessions.
- Easy-to-use function with parameter validation for robust error handling.

## Installation

Install the package via pip:

```bash
pip install nba-analytica
```
Ensure you have Python 3.x and pip installed on your system before installing.

## Usage
Import the `get_player_stats` function from the package and use it to fetch player statistics by specifying the player's name and the desired statistical mode.

```python
from nba_stats_fetcher import get_player_stats

# Example: Fetch LeBron James's per game statistics
stats = get_player_stats('LeBron James', 'PerGame')
print(stats)
```
## Parameters
- `player_name` (str): Name of the player to fetch stats for.
- `per_mode` (str): Statistical mode. Options: 'PerGame', 'PerPossession', 'Per100Possessions'. Default is 'PerGame'.

## Returns
- If successful, returns a dictionary containing the player's statistics.
- Returns a string error message if the player is not found or if there's a request failure.

## Error Handling
Raises a `ValueError` if the `per_mode` parameter is invalid. Make sure to handle this exception appropriately in your code.

## Contributing
Contributions are welcomed! If you have suggestions for improvements or bug fixes, please feel free to fork the repository, make your changes, and submit a pull request.
