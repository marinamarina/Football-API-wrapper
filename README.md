# A Python wrapper for the Football API 
## Example usage of the module

`#! usr/bin/python
from football_api_wrapper import FootballAPIWrapper
from pprint import pprint

<!--example usage-->
wrap = FootballAPIWrapper()

<!--# set the api key
-->
faw = FootballAPIWrapper()
faw.api_key = 'your_key'
faw.data_dir = '/data/'

pprint(faw.played_matches)


