
#!/bin/bash
# Kill any existing processes
pkill -f Xvfb
pkill -f tint2
pkill -f firefox

# Set display
export DISPLAY=:0

# Start X server and wait for it
Xvfb :0 -screen 0 1024x768x24 &
sleep 3

# Start window manager and wait
tint2 &
sleep 2

# Start Firefox with proper flags
firefox --kiosk --new-window http://0.0.0.0:5000 --no-remote &
