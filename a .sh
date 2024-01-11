`boot.sh#!/bin/bash

read -p "Do you want to play rock-paper-scissors? (yes/no): " response

if [ "$response" == "yes" ]; then
    python3 play_game.py
else
    echo "That's too bad, maybe next time."
fi
