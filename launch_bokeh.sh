#!/bin/bash
# Start Bokeh server and save its PID
bokeh serve main.py --address 10.0.4.103 --port 5006 --allow-websocket-origin=10.0.4.103:5006 &
echo $! > bokeh-server.pid
