import csv
import psycopg2
from util import track_load


class DataLoader:
    def __init__(self, conn):
        self.conn = conn

    def load_teams(self, file):
        with open(file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # skip header row
            for row in reader:
                name, team = row
                cur = self.conn.cursor()
                try:
                    cur.execute(
                        "INSERT INTO noc (name, Team) VALUES (%s, %s)",
                        (name, team)
                    )
                    self.conn.commit()
                    success = True
                except Exception as e:
                    self.conn.rollback()
                    success = False
                    error_message = str(e)
                track_load(self.conn, 'noc', team, success, error_message if not success else None)
                cur.close()

    def load_events(self, event_csv_file):
        with open(event_csv_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # skip header row
            for row in reader:
                event_name, sport_name = row
                cur = self.conn.cursor()
                try:
                    cur.execute(
                        "INSERT INTO event (name, sport) VALUES (%s, %s)",
                        (event_name, sport_name)
                    )
                    self.conn.commit()
                    success: bool = True
                except Exception as e:
                    self.conn.rollback()
                    success = False
                    error_message = str(e)
                track_load(self.conn, 'event', event_name, success, error_message if not success else None)
                cur.close()

    def load_games(self, game_csv_file):
        with open(game_csv_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # skip header row
            for row in reader:
                season, year, city, games = row
                cur = self.conn.cursor()
                try:
                    cur.execute(
                        "INSERT INTO olympic_game (year, season, city, games) VALUES (%s, %s, %s, %s)",
                        (year, season, city, games)
                    )
                    self.conn.commit()
                    success = True
                except Exception as e:
                    self.conn.rollback()
                    success = False
                    error_message = str(e)
                track_load(self.conn,'olympic_game', games, success, error_message if not success else None)
                cur.close()

    def load_athletes(self, athlete_csv_file):
        with open(athlete_csv_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # skip header row
            for row in reader:
                name, sex, age, noc = row
                cur = self.conn.cursor()
                try:
                    cur.execute(
                        "SELECT id FROM noc WHERE name = %s",
                        (noc,)
                    )
                    noc_id = cur.fetchone()[0]
                    cur.execute(
                        "INSERT INTO athlete (name, sex, age, noc_id) VALUES (%s, %s, %s, %s)",
                        (name, sex, age, noc_id)
                    )
                    self.conn.commit()
                    success = True
                except Exception as e:
                    self.conn.rollback()
                    success = False
                    error_message = str(e)
                track_load(self.conn, 'athlete', name, success, error_message if not success else None)
                cur.close()

    def load_athlete_event(self, athlete_event_csv_file):
        with open(athlete_event_csv_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # skip header row
            for row in reader:
                athlete_name, age, event_name, games, medal_type = row
                cur = self.conn.cursor()
                try:
                    cur.execute(
                        "SELECT id FROM athlete WHERE name = %s and age = %s",
                        (athlete_name, age)
                    )
                    athlete_id = cur.fetchone()[0]
                    cur.execute(
                        "SELECT id FROM event WHERE name = %s",
                        (event_name,)
                    )
                    event_id = cur.fetchone()[0]
                    cur.execute(
                        "SELECT id FROM olympic_game WHERE games = %s",
                        (games,)
                    )
                    game_id = cur.fetchone()[0]
                    cur.execute(
                        "INSERT INTO athlete_event (athlete_id, age, event_id, medal, game_id) VALUES (%s, %s, %s, "
                        "%s, %s)",
                        (athlete_id, age, event_id, medal_type, game_id)
                    )
                    self.conn.commit()
                    success = True
                except Exception as e:
                    self.conn.rollback()
                    success = False
                    error_message = str(e)
                track_load(self.conn, 'athlete_event', athlete_name, success, error_message if not success else None)
                cur.close()
