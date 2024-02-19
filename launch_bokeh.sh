#!/bin/bash
# Start Bokeh server and save its PID
bokeh serve main_bokeh_server.py --address 130.215.212.4 --port 5006 --allow-websocket-origin=130.215.212.4:5006 &
echo $! > bokeh-server.pid
