# Elevators_project

## Description
The Elevators Project is a simulation of elevator systems, using pygame 

## Features
•⁠  ⁠Simulates multiple elevators serving multiple floors.
•⁠  ⁠Demonstrates various elevator scheduling algorithms.
•⁠  ⁠Provides visualization of elevator movement and system performance.
   
## Installation
1.⁠ ⁠Clone the repository:
   ```bash
   git clone https://github.com/yuda03979/elevators_project.git



# files:

1. classes:
  - GameMeneger
  - Building
  - Floor
  - ShoeButton
  - Timer
  - Button
  - Elevator
2. python files:
  - main
  - gui: drow and updates the data into the screen
  - settings: for user to change  :)
  - functions_and_settings: other settings => do not change!
  - source(folder): images, fonts, etc.

# Algorithem and data structure:
## overview:
   - when user press a floor, the elevator with the shortest arrival time will add the floor into its queue(
      and occupied the floor).
      when the elevator will arrive to the floor, the elevator will wait 2 sec, and if there are more floors
      in the queue, the elevator will releas the floor.
## data structure:
   - each elevatore have queue of floors that it should arrive to.
