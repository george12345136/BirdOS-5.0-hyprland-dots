#!/bin/bash


WALLPAPER_DIR="/home/$USER/Pictures"

SWWW_TRANSITION_TYPE="wipe"
SWWW_TRANSITION_STEP="60"



WALLPAPER_SELECTION=$(find "$WALLPAPER_DIR" -type f \( -iname "*.jpg" -o -iname "*.png" -o -iname "*.jpeg" \) | \
    rofi -dmenu -i -p "Select Wallpaper:")

if [ -n "$WALLPAPER_SELECTION" ]; then

    swww img "$WALLPAPER_SELECTION" \
        --transition-type "$SWWW_TRANSITION_TYPE" \
        --transition-step "$SWWW_TRANSITION_STEP"


    matugen image "$WALLPAPER_SELECTION"

    notify-send "The Wallpaper has changed"
    
    pkill -SIGUSR2 waybar
    
fi
