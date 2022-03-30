from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd

load_dotenv()

class SQL():
    def __init__(self):
        self.connect_db()

    def connect_db(self):
        self.conn = psycopg2.connect(
            host=os.getenv('HOST_HEROKU_SQL_PROJECT'),
            database=os.getenv('DATABASE_HEROKU_SQL_PROJECT'),
            user=os.getenv('USER_HEROKU_SQL_PROJECT'),
            password=os.getenv('PASSWORD_HEROKU_SQL_PROJECT'),
            port = os.getenv('PORT_HEROKU_SQL_PROJECT'))

        print('Connected!')
        return self.conn 

    def create_table(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        cursor.close()
        print('create_table() - Done!')

    def copy_from_file(self, file, table):
        """
        Here we are going save the dataframe on disk as 
        a csv file, load the csv file  
        and use copy_from() to copy it to the table
        """
        f = open(file, 'r')
        cursor = self.conn.cursor()
        try:
            cursor.copy_from(f, table, sep=",", null = 'NA')
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            self.conn.rollback()
            cursor.close()
            return 1
        cursor.close()
        print('copy_from_file() - Done!')

    def make_query(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        output = cursor.fetchall()
        colnames = [desc[0] for desc in cursor.description]
        self.conn.commit()
        cursor.close()
        return pd.DataFrame(output, columns = colnames)

    # if __name__ == '__main__':
    #     conn = connect_db()
    #     # select, boolean, count and group by
    #     result = make_query(
    #         conn, 
    #         """
    #         SELECT 
    #             t1.species as species, 
    #             count(*) as qtd_of_penguins,
    #             avg(t1.body_mass_g) as mean_body_mass_g, 
    #             t1.species = 'Adelie' as is_adelie  
    #         FROM penguins t1 
    #         GROUP BY t1.species
    #         """)
    #     conn.close()