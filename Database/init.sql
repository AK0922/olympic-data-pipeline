CREATE TABLE noc (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    Team VARCHAR(255),
    CONSTRAINT Country UNIQUE(name)
);

CREATE TABLE event (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    sport VARCHAR(255) NOT NULL
);

CREATE TABLE olympic_game (
    id SERIAL PRIMARY KEY,
    year INTEGER,
    season VARCHAR(10),
    city VARCHAR(255) NOT NULL,
    games VARCHAR(255) NOT NULL
);

CREATE TABLE athlete (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    sex CHAR(1),
    age VARCHAR(10),
    noc_id INTEGER REFERENCES noc(id),
    CONSTRAINT Athlete_year UNIQUE(name,sex,age,noc_id)
);

CREATE TABLE athlete_event (
    id SERIAL PRIMARY KEY,
    athlete_id INTEGER REFERENCES athlete(id),
    age VARCHAR(10),
    event_id INTEGER REFERENCES event(id),
    medal VARCHAR(10),
    game_id INTEGER REFERENCES olympic_game(id)
);

CREATE TABLE metadata (
  id SERIAL PRIMARY KEY,
  destination_table TEXT NOT NULL,
  record TEXT NOT NULL,
  success BOOLEAN NOT NULL,
  error_message TEXT
);

-- Add indexes to the 'athlete' table
CREATE INDEX idx_athlete_name ON athlete (name);
CREATE INDEX idx_athlete_sex ON athlete (sex);
CREATE INDEX idx_athlete_age ON athlete (age);


-- Add indexes to the 'noc' table
CREATE INDEX idx_noc_name ON noc (name);
CREATE INDEX idx_noc_region ON noc (Team);

-- Add indexes to the 'olympic_game' table
CREATE INDEX idx_olympic_game_year ON olympic_game (year);
CREATE INDEX idx_olympic_game_season ON olympic_game (season);
CREATE INDEX idx_olympic_game_city ON olympic_game (city);

-- Add indexes to the 'event' table
CREATE INDEX idx_event_name ON event (name);
CREATE INDEX idx_event_sport ON event (sport);

-- Add indexes to the 'athlete_event' table
CREATE INDEX idx_athlete_event_athlete_id ON athlete_event (athlete_id);
CREATE INDEX idx_athlete_event_event_id ON athlete_event (event_id);
CREATE INDEX idx_athlete_event_medal ON athlete_event (medal);
