from leagueoflegends import LeagueOfLegends, RiotError

lol = LeagueOfLegends('RGAPIfcf985395c46447e815d77ae80c424be')

# Call the API with explicit summoner ID
id = lol.get_summoner_by_name('thispassing')
lol.get_games(id)