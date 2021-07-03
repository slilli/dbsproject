import psycopg2
import csv

"""
DBS Projekt
Gruppe Anna Lilli Elisa
--------------------
ACHTUNG: Alle Kommentare vor dem Ausführen lesen
"""

def create_tables():

    """SQL Befehle in Tupel gespeichert"""
    commands = """
    CREATE TABLE Output(
        country_name CHAR(64) NOT NULL,
        country_code CHAR(64) NOT NULL,
        year FLOAT(53) NOT NULL,
        gdp FLOAT(53),
        mortality_rate FLOAT(53),
        population_growth FLOAT(53),
        population_total FLOAT(53),
        annual_co2_emission FLOAT(53),
    PRIMARY KEY(country_code, year)
        )
    """
    """Führt alle SQL Commands im Tupel aus"""
    #for command in commands:
    cur.execute(commands)
    conn.commit()
    print("Tables created")

#tut die Input Daten in die Output Tabelle
def insert_data_input(input_file):
    with open(input_file,'r') as in_csv:
        reader=csv.reader(in_csv)
        print("Füge Daten ein")
        for r in reader:
            cur.execute("""Insert Into output(
            country_name,
            country_code,
            year,
            gdp,
            mortality_rate,
            population_growth,
            population_total,
            annual_co2_emission)
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
            ON CONFLICT DO NOTHING
            """,
            (r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8]))
        conn.commit()
        print("Daten eingefügt")


try:
    conn = psycopg2.connect("dbname=dbsproject user=postgres password =swaggier")
    print("Connected")

except:
    print("Not able to connect")

cur = conn.cursor()

#cur.execute("""DROP TABLE output""")
create_tables()
insert_data_input("all_csv_merged_new.csv")

#cur = conn.cursor()
