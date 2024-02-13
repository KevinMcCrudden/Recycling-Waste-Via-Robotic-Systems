#!/bin/bash
# Read PID from file and kill the process
if [ -f bokeh-server.pid ]; then
    kill $(cat bokeh-server.pid)
    rm bokeh-server.pid
else
    echo "PID file not found. Is the Bokeh server running?"
fi
