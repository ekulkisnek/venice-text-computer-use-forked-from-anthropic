
#!/bin/bash
export DISPLAY=:0
Xvfb :0 -screen 0 1024x768x24 &
sleep 1
tint2 &
firefox --kiosk --new-window http://0.0.0.0:5000 &
