# A Python wrapper around the Football API (http://football-api.com/)
# Example usage of the module

`#! usr/bin/python
from football_api_wrapper import FootballAPIWrapper
from pprint import pprint

<!--example usage-->
wrap = FootballAPIWrapper()

<!--# set the api key
-->
wrap.api_key = 'api_key'

dict1 = dict()
ids_dict = {'Manchester': 1, 'Aston Villa': 3}

pprint(wrap.played_matches)


