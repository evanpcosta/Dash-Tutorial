# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

csvfile = pd.read_csv('cd.csv')

def generate_table(dataframe, max_rows=10, max_cols=9):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns[:max_cols]])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns[:max_cols]
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

#Data declaration
df = pd.DataFrame({
    "City Size": ["Large", "Small", "Large", "Large", "Medium", "Medium", "Medium", "Medium", "Small", "Large"],
    "Amount": [45000, 11250, 175000, 175000, 125000, 125000, 125000, 125000, 87500, 87500],
    "Maritial Status": ["Married", "Single", "Single", "Single", "Married", "Married", "Married", "Single", "Single", "Married",]
})

exp_df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')


#graph instances
fig = px.bar(df, x="City Size", y="Amount", color="Maritial Status", barmode="group")

fig2 = px.scatter(exp_df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

#graph layout
fig.update_layout(plot_bgcolor='honeydew', font_color='black', paper_bgcolor='honeydew')
fig2.update_layout(plot_bgcolor='honeydew', font_color='black', paper_bgcolor='honeydew')

#App layout 
app.layout = html.Div(
    html.Div(style={'backgroundColor': 'honeydew'}, children=[

    html.H1(children='Evans Dash Application', style = {'color': 'black', 'textAlign': 'center'}),

    html.Div(children= 'Made with Dash', style={'color': 'black', 'textAlign':'center'}),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    html.H4(children='ID Theft Data'),
    generate_table(csvfile),

    html.Div(style={'backgroundColor':'honeydew'}, children = [html.Div(children='Helloooo', style={'color':'honeydew'}), html.Div(children='Helloowo2', style={'color':'honeydew'})]),

    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig2
    )

]))

if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=False)