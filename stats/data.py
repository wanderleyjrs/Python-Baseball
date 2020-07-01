import os
import glob
import pandas as pd
#3 - Python File Management
#game_files = glob.glob(os.path.join(os.getcwd(), 'games','*.EVE'))  os.getcwd() -> return the current working directory of a process.
game_files = glob.glob('/home/wanderley/Python-Baseball/games/*.EVE')
#4 - Sorting File Names
game_files.sort()

#5 - Read CSV Files
game_frames = []
#6 - Append Game Frames
for game_file in game_files:
	game_frame = pd.read_csv(game_file, names = ['type', 'multi2', 'multi3', 'multi4', 'multi5', 'multi6', 'event'])
	game_frames.append(game_frame)
#7 - Concatenate DataFrames
games = pd.concat(game_frames)
#8 - Clean Values
games.loc[(games['multi5'] == '??'),'multi5'] = " "
#9 - Extract Identifiers
identifiers = games['multi2'].str.extract(r'(.LS(\d{4})\d{5})')
#10 - Forward Fill Identifiers
identifiers = identifiers.fillna(method='ffill')
#11 - Rename Columns
identifiers.columns = ['game_id', 'year']
#12 - Concatenate Identifier Columns
games = pd.concat([games, identifiers], axis=1, sort=False)
#13 - Fill NaN Values
games = games.fillna(' ')
#14 - Categorical Event Type
games.loc[:,'type'] = pd.Categorical(games.loc[:,'type'])
#15 - Print DF
print(games.head())


