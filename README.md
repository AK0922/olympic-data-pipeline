## Olympic Data pipeline

 Normalized the 124 year Olympic data from these sources and ingested into postgres database 
 https://www.kaggle.com/datasets/nitishsharma01/olympics-124-years-datasettill-2020?se lect=Athletes_summer_games.csv\
 https://www.kaggle.com/datasets/nitishsharma01/olympics-124-years-datasettill-2020?se lect=Athletes_winter_games.csv

1.Created Postgres database and normalized tables\
2.Python library to read the source files and ingest to the created database tables in Postgres
3.Dockerized the above 2 steps. 

`Database/init.sql` file contains the DDL scripts to create the database tables and adding constraints, indexes.\
`app/` folder contains the python scrip to read source files and write to the database tables.\
For the sake of simplicity I have hardcoded the credentails for the database in the `docker-compose.yml` file

In the interest in time, I have this working solution. 
This can be further modularized, data cleaned, can make config abstractions and many more.


## How to Run Application

Building Docker using command `docker-compose build`\
Running Application using Docker `docker-compose up`

It will spin up 2 docker containers
1. db - to host database and runs DDL commands
2. app - to run the ignestion into database

if you are interested in changing the input files specify the path to files at `docker-compose.yml`

I have faced scenario where database tables were not getting created after container is up and running.
I was able to resolve it by accessing the running db container and executing the `init.sql`
Here are the steps:
connect to container with command `docker exec -it db /bin/bash`\
Run the command `psql -U dev -d olympic < init.sql`

## How to connect database

Validate if the db container is up and running using the command `docker ps`\
connect to container with command `docker exec -it db /bin/bash`\
once your inside the container to comment to the database `psql -u dev -d olympic`

# Tables Created
1. Athlete:
		athlete_id(primary key)
    name
    sex
    age
    noc_id(foreign key referencing noc table)
		
2. Noc table
		noc_id(primary key)
		name
		team
		
3. Event table
		event_id(primary key)
		event_name
		sport_name
		
4. Olympic_game table
		game_id(primary key)
		year
		season
		city
		games
		
5. Athlete_event
		athlete_event_id (primary key)
		athlete_id (foreign key referencing athlete table)
		athlete_age
		event_id (foreign key referencing event table)
		medal
		game_id (foreign key referencing olympic_game table)

6. Metadata
    id (primary key)
		destination_table
		record
		success
		error
		
		
Here is a brief explanation of the tables and their columns:

Athlete table: contains information about individual athletes, such as their name, sex, age, country(noc_id).\
The noc_id column is a foreign key that references the noc_id column in the noc table.

Noc table: contains information about the teams that participated in the Olympics, NOC (National Olympic Committee) name and Team.

Event table: contains information about the events, including the sport name and event name.

Olympic_game table: contains information about the year,season,city where the game was hosted.

Athlete_event table: contains information about the performance of athletes in events, including the athlete ID, event ID, medal type (gold, silver, or bronze), and age of athlete during that event.

Metadata table: tracks the each record ingestion into all the above tables.

