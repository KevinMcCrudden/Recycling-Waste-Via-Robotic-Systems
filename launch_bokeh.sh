#!/bin/bash
# Start Bokeh server and save its PID
bokeh serve main_bokeh_server.py --address 130.215.244.47 --port 5006 --allow-websocket-origin=130.215.244.47:5006 &
echo $! > bokeh-server.pid
