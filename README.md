# Database scripts and programs
## Connecting to Oracle
[Connect to oracle](https://github.com/KRBlackwell/database/blob/main/oracle_connect.py)\
That's it. Connect with a config file. Query a schema table.

## Connecting to Postgres and alter user
[Connect to postgres](https://github.com/KRBlackwell/database/blob/main/postgres_connect.py)\
Connect with a config file. Alter user to change password. Disconnect and connect with new password. Query a schema table to check the new password.

# From "Portfolio Project Starters" repository:
I did a lot of teaching learners in 2022 and 2023. I started to share some of that in my github so they can access it, and to share with others.

## Sqlite3 create database and trigger, example of using a pandas dataframe and to_sql
[Example of dataframe to database with sqlite3](https://github.com/KRBlackwell/portfolio-project-starters/blob/main/sqlite3_project_starter.ipynb)\
[Link to Google Colab notebook](https://colab.research.google.com/drive/1C5iKVcuyhbqz8Co3GQ8hRiNXmwWhvif3?usp=sharing)\
With sqlite3, you need to specify SQL statements.

## SQLAlchemy example using a pandas dataframe
[Example of dataframe to database with SQLAlchemy - not using to_sql](https://github.com/KRBlackwell/portfolio-project-starters/blob/main/data_input_sqlalchemy.ipynb)\
[Link to Google Colab notebook](https://colab.research.google.com/drive/1vGUNLYN30u_tOlP3mGRJ62zx1zlTLrhe?usp=sharing)\
 \
[Example of dataframe to database with SQLAlchemy](https://github.com/KRBlackwell/portfolio-project-starters/blob/main/data_input_to_sql_sqlalchemy.ipynb)\
[Link to Google Colab notebook](https://colab.research.google.com/drive/1HAwvptwN1vBCx-5iI1psqMm1p2O1Cfic?usp=sharing)\
This is a good starter if you need a database and have an input file. Pandas can read different types of data files into a dataframe, and SQLAlchemy has an ORM that you can use to get the data into the database. What would you do to rename a bunch of dataframe columns to match what you want in the target databse?
