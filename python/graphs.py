# import dash
# import dash_core_elements as dcc
# import pandas as pd
import plotly.express as px


class Graphs:
    def barplot(self, df, x, y, **kwargs):
        bar_fig = px.bar(
            data_frame = df,
            x = x,
            y = y,
            orientation = 'h',
            **kwargs)
        return bar_fig 
    
