# nrdylights
LED-Light Controller

### actions/next.action
The script reads the next action from this file. Possible entries:
```
Line1: static | exit
Line2: Name of the .scn Scenefile (file only, without folder)
Line3: Name of the .bright File with the brightness-Definitions
```

### scenes-static/foo.scene
Two possibilities. Raw-value file, each line represents a percentage of a channel
```
0
100
50
...
0
```
Or a named-color file. First Line must be 'color', then 5 lines with a color-name for each channel-group. The color-name represents a file in the color/ folder, where this specific color is defined
```
color
blue
off
white
white
off
```

### brightness/foo.bright
A brightness-definition file. Five lines, with a brightness-percentage for each channel-group
```
100
100
50
10
0
```

### color/foo.color
A color-definition file. Three lines, defining the RGB-value of a specific color. Write in percent-values
```
100
0
0
```

### scenes-dynamic/foo.dyn
Needs some more informations
```
NUM # First line defines the amount of different steps in this scene
foo.scene #First scene
10 #Steps to first scene
0.1 #Delay after each step in seconds
4 #Pause after the first scene before starting the next one
bar.scene #Second scene
20 #Steps to second scene
0.2 #Delay
3 #Pause after the second scene... and so on
```
