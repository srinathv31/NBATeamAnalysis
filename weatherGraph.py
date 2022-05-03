# Import Meteostat library and dependencies
from datetime import datetime
from meteostat import Point, Monthly
import pandas as pd
import plotly.express as px
from modifyData import grabTeamWinsPerMonth

# Set time period
start = datetime(2000, 10, 31)
end = datetime(2001, 6, 18)

# Create Point for philly, LA
philly = Point(39.952583, -75.165222, 39)
los_angeles = Point(34.052235, -118.243683, 305)

# Get monthly data for 2000 - 2001
data = Monthly(los_angeles, start, end)
data = data.fetch()
df = pd.DataFrame(data)
df.to_csv("tempData.csv", encoding="utf-8", index_label="index")

# Get monthly team data
team_data = grabTeamWinsPerMonth()

fig = px.line(x=team_data['month'][:], y=df['tavg'], markers=True)
fig.add_bar(x=team_data['month'][:], y=team_data['W'], name="Wins", text=team_data['W'])
fig.add_bar(x=team_data['month'][:], y=team_data['L'], name="Losses", text=team_data['L'])

fig.update_layout(
    barmode='stack',
    xaxis_type = 'category'
)
fig.show()
