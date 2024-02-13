#!/bin/bash
# Start Bokeh server and save its PID
bokeh serve my_bokeh_app.py --port 5006 &
echo $! > bokeh-server.pid
