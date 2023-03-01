import pandas as pd
import numpy as np
from util import file_exists

pd.options.mode.chained_assignment = None


def read_file(filepath):
    dfs = list()
    if len(filepath) == 0:
        raise FileNotFoundError("No input file is passed")
    for file in filepath:
        file_exists(file)
        df = pd.read_csv(file)
        dfs.append(df)

    olympic_df = pd.concat(dfs, ignore_index=True)

    athlete_df = olympic_df[['Name', 'Sex', 'Age', 'NOC']]
    athlete_df.drop_duplicates(inplace=True)
    athlete_df.to_csv('athlete.csv', index=False)

    games_df = olympic_df[['Season', 'Year', 'City', 'Games']]
    games_df.drop_duplicates(inplace=True)
    games_df.to_csv('games.csv', index=False)

    noc_df = olympic_df[['NOC', 'Team']]
    noc_df.drop_duplicates(subset="NOC",inplace=True)
    noc_df.to_csv('noc.csv', index=False)

    event_df = olympic_df[['Event', 'Sport']]
    event_df.drop_duplicates(inplace=True)
    event_df.to_csv('events.csv', index=False)

    athlete_event_df = olympic_df[['Name', 'Age', 'Event', 'Games', 'Medal']]
    athlete_event_df.drop_duplicates(inplace=True)
    athlete_event_df.to_csv('athlete_event.csv', index=False)
