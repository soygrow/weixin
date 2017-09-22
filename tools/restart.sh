#/bin/bash

ps aux | grep "python ../test/main.py" | awk '{print $2}' | xargs kill -9

nohup python ../test/main.py 80 > ../logs/main.log 2>&1 &
