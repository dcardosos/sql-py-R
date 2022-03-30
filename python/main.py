from sql_tools import SQL
import plotly.express as px

def dash(df, x, y, title):
    bar_fig = px.bar(
        data_frame = df,
        x = x,
        y = y,
        title = title,
        orientation = 'h'
    )
    
    bar_fig.show()

if __name__ == '__main__':
    query = """
        SELECT 
            t1.species as species, 
            count(*) as qtd_of_penguins,
            avg(t1.body_mass_g) as mean_body_mass_g, 
            t1.species = 'Adelie' as is_adelie  
        FROM penguins t1 
        GROUP BY t1.species
        """

    sql_obj = SQL()
    result = sql_obj.make_query(query)
    print(result)
    # # dashboard
    # dash(
    #     df = result, 
    #     x = 'qtd_of_penguins',
    #     y = 'species',
    #     title = 'Quantity of penguins')
