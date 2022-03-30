# import dash
# import dash_core_elements as dcc
# import pandas as pd
import plotly.express as px


class Dashboard:
    def __init__(self, df):
        self.df = df

    def barplot(self, x, y, title):
        bar_fig = px.bar(
            data_frame = self.df,
            x = x,
            y = y,
            title = title,
            orientation = 'h')
        return bar_fig 
    
