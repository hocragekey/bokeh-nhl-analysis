# bokeh-nhl-analysis

`docker build --file Dockerfile --tag jimlebonitte/bokeh-nhl-analysis .`

#interactive run time

`docker run -p 5006:5006 -it jimlebonitte/bokeh-nhl-analysis bokeh serve /bokeh_examples/hello_world.py`