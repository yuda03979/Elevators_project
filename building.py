from functions_and_settings import *
from floor import *
from elevator import *


class Building:
    """
    responsebility:
    - create the building's floors
    - update and drow the building
    
    API:
    - drow_building()
    - update_building()
    - check_user_input()
    - choose_elevator()
    - get_right_side_index()
    """

    def __init__(self, building_number:int, x:int, y:int) -> None:

        self.building_number = building_number
        self.building_bottom_left = (x, y) # to change later!!!!
        
        self.floors_array = self.initialize_floors_array()
        self.elevators_array = self.initialize_elevators_array()


    def drow_building(self, world: pg.surface, font: pg.font):
        """
        drow the all building, (floors and elevators)
        """
        for floor in self.floors_array:
            floor.drow_floor(world, font)
        for elevator in self.elevators_array:
            elevator.drow_elevator(world)


    def update_building(self, time_past):
        """
        update all the time the all building. without user input
        """
        for floor in self.floors_array:
            floor.update_floor(time_past)
        for elevator in self.elevators_array:
            elevator.update_indexes(time_past)
            elevator.update_last_used()
        
              
    def get_right_side_index(self):
        """
        return the index of right side of the building (for the next building)
        """
        return self.building_bottom_left[0] + (ELEVATOR_SIZE[0] * ELEVATOR_NUMBER_ARRAY[self.building_number])
    

    def choose_elevator(self, floor:object):
        """
        checks the better elevator, 
        floor attributes are updates including timer,
        add the call to the elevator
        return None
        """
        elevator, timer = self.nearest_elevator(floor)
        floor.occupied_floor(timer)
        elevator.queue.append(floor)


    def check_user_input(self, event: pg.event, scrool_x: int, scroll_y: int):
        # because the user input (x, y) is according the screen, and our button is according the world we need to fix it
        event = (event.pos[0] + scrool_x, event.pos[1] + scroll_y) 

        for floor in self.floors_array:
            if floor.check_user_input(event):
                self.choose_elevator(floor)


# private



    def initialize_floors_array(self):
        """
        initialize floor array with floor x, y
        """
        arr = []
        x, updated_y = self.building_bottom_left
        for i in range(FLOOR_NUMBER_ARRAY[self.building_number]):
            arr.append(Floor(self.building_number, i, x, updated_y))
            updated_y -= FLOOR_SIZE[1]
        return arr
    

    def initialize_elevators_array(self):
        """
        initialize elevator array with elevator x, y
        """
        arr = []
        updated_x, y = self.building_bottom_left[0] + FLOOR_SIZE[0], self.building_bottom_left[1]
        for _ in range(ELEVATOR_NUMBER_ARRAY[self.building_number]):
            arr.append(Elevator(updated_x, y, self.floors_array[0]))
            updated_x += ELEVATOR_SIZE[0]
        return arr


    def nearest_elevator(self, floor):
        """
        checks if the floor already calld elevator if so:
        using get next floor arival time, 
        determine which elevator will take the callElevator
        and apply it by add_call_elevator
        """
        min = [-1, float('inf')]
        for elevator in self.elevators_array:
            val = elevator.get_arivel_time(floor)
            min = [elevator, val] if min[1] > val else min
        return min[0], min[1]