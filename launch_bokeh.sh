#!/bin/bash
# Start Bokeh server and save its PID
bokeh serve main.py --port 5006 &
echo $! > bokeh-server.pid
