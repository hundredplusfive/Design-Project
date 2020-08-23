# Design-Project
"Integration of path planning and area mapping for autonomous cleaning robot"

Demonstration video: https://youtu.be/LP9Fz7td_1Y

grid-map_simulator code = processing.java

[Setup]
- Ubuntu 16.04
- processing IDE (https://processing.org/download/)
- spyder Python 3.7 IDE (any IDEs would do)

Instruction:
1. Ensure all the Python files are within the same directory
  - compEdgePath
  - dfs
  - hamiltonian
2. In the "compEdgePath" at line 32, change the output text file from the "grid-map_simulator" location accordingly
3. Create an empty "edge.txt" file within the same directory

[grid-map_simulator.pde]
Objectives: 
- creates a floor plan with obstacles
- demacates the entire floor plan into segments with coressponding start points

How to use:
(1) Create floor plan or obstacles = using the mouse, click + hold + drag the cursor on the preferred grids

(2) Erase grid status (from occupied to unoccupied) = using the mouse, click onnce on the selected grid

(3) Create square or rectangular segements = 
    1. keyboard press of 'd' or 'd' to start the segment marking sequence
    2. After the keyboard press, use the mouse and click the corners of preferred segment area as followed...

    x x x
    x x x = 3 by 3 segment (x represents the grid)
    x x x

    4 x 1
    x x x = click the corner grids as indicated by the numbers
    3 x 2

(4) Mark the start points within each segments =
    1. Hover the mouse cursor on the selected grid
    2. Keyboad press of 's' or 'S'
    
(5) Export information of all segments into a text file = 
    1. keyboard press of 'l' or 'L'
    2. Each segment information texts are labelled from 0

FAQ:
1. How to increase window size? Under the void setup() change the size parameters.

2. How to increase number of grids (columns and rows)? On the first line of the code, change the 'w' and 'h' variables

3. How to increase individual grid size? On the first line of the code, change the 'bs' variable (the value is in pixels)

[compEdgePath.py]
Objective: Returns the path sequence for depth first search or hamiltonian circuits for the provdied segment

How to use:
1. Ensure the line 32 indicates the segment to be computed
2. execute the the compEdgePath code
