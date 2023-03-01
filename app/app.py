import os
import sys
import pandas as pd
from read import read_file
from write import DataLoader
from config import DBConnector


def main():
    input_file = sys.argv[1:]
    print(input_file)
    read_file(input_file)
    connector = DBConnector(host=os.environ.get('DB_HOST'), port=5432, database='olympic', user='dev', password='Qwerty@2')
    conn = connector.get_connection()
    loader = DataLoader(conn)
    loader.load_teams('noc.csv')
    loader.load_events('events.csv')
    loader.load_games('games.csv')
    loader.load_athletes('athlete.csv')
    loader.load_athlete_event('athlete_event.csv')


if __name__ == '__main__':
    main()
