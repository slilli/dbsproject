# Anna, Lilli, Elisa
import pandas as pd
import plotly.express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import psycopg2

def connect(query):
    try:
        conn = psycopg2.connect("dbname=dbsproject user=postgres password =swaggier")
        print("Connected")

    except:
        print("Not able to connect")

    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data
#Load dataset as csv
#mr = pd.read_csv('all_csv_merged_dash.csv')
mr = connect("SELECT * FROM output")

country_names = []
years = []
gdps = []
mrs = []

for tup in mr:
    country_names.append(tup[0])
    years.append(tup[2])
    gdps.append(tup[3])
    mrs.append(tup[4])

dfdata = {'country_name': country_names,'year': years,'gdp': gdps, 'mortality_rate': mrs}

mydf = pd.DataFrame(dfdata)


#create dash app
app= dash.Dash()

#Set up the app layout
app.layout = html.Div(children = [
    html.H1(children = 'GDP Dashboard'),
    dcc.Dropdown(id='country_name-dropdown',
                options = [{'label': i, 'value': i}
                        for i in mydf['country_name'].unique()],
                        #for i in mydf["country_name"].unique()],
                        value = 'Germany'),
    dcc.Graph(id='mr-graph')
])

#Set up the callback functions
@app.callback(
    Output(component_id = 'mr-graph', component_property = 'figure'),
    Input(component_id = 'country_name-dropdown', component_property = 'value')
)

def update_graph(selected_country):
    filtered_mr = mydf[mydf['country_name'] == selected_country]
    line_fig = px.line(filtered_mr,
                x='year', y='gdp',
                title = f'GDP ~ year in {selected_country}')
    return line_fig

#Run local server
if __name__ == '__main__':
    app.run_server(debug=True)
