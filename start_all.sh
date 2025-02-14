
#!/bin/bash
export DISPLAY=:0
Xvfb :0 -screen 0 1024x768x24 &
sleep 2
tint2 &
sleep 1
firefox --kiosk --new-window http://0.0.0.0:5000 &
