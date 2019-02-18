import pandas as pd
from bokeh.io import curdoc, show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

#read in nhl skaters
df = pd.read_csv('/bokeh_examples/2019_skaters.csv')
df = df.groupby(['Tm'])['G'].agg('sum').reset_index()

print(df)

#get goals by team
source = ColumnDataSource(df)

p = figure(plot_width=900, title='Goals By Team', x_range=df['Tm'], y_range=(0, 230))
p.vbar(x='Tm', top='G', width=0.5, source=source, bottom=0, color="firebrick")
curdoc().add_root(p)
show(p)