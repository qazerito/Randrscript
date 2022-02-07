import os

os.system ("xrandr --output DisplayPort-0 --primary --mode 2560x1080 --rate 74.99 --output eDP --off")

r = input("Would you like to revert changes?")

if r == "y":
    os.system("xrandr --output eDP --primary --mode 1920x1080 --output DisplayPort-0 --off")

    else
        print("Configuration Completed! Restart your i3wm instance...")
