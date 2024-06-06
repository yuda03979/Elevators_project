from functions_and_settings import *
from floor import *
from elevator import *


class Building:

    def __init__(self, building_number:int, x:int, y:int) -> None:

        self.building_number = building_number
        self.building_bottom_left = (x, y)#to change later!!!!
        
        self.floors_array = self.initialize_floors_array()
        self.elevators_array = self.initialize_elevators_array()


    def initialize_floors_array(self):
        """
        initialize floor array with floor x, y
        """
        arr = []
        x, updated_y = self.building_bottom_left[0], self.building_bottom_left[1]
        for i in range(FLOOR_NUMBER_ARRAY[self.building_number]):
            arr.append(Floor(i, x, updated_y))
            updated_y -= FLOOR_SIZE[1]
        return arr
    

    def initialize_elevators_array(self):
        """
        initialize elevator array with elevator x, y
        """
        arr = []
        updated_x, y = self.building_bottom_left[0]  + FLOOR_SIZE[0], self.building_bottom_left[1]
        for i in range(ELEVATOR_NUMBER_ARRAY[self.building_number]):
            arr.append(Elevator(updated_x, y, self.floors_array[0]))
            updated_x += ELEVATOR_SIZE[0]
        return arr


    def drow_building(self, screen, font):
        for floor in self.floors_array:
            floor.drow_floor(screen, font)
        for elevator in self.elevators_array:
            elevator.drow_elevator(screen)


    def update_building(self, time_past):
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
    
    def check_user_input(self, event, scrool_x, scroll_y):
        event = (event.pos[0] + scrool_x, event.pos[1] + scroll_y)
        for floor in self.floors_array:
            if floor.check_user_input(event):
                self.choose_elevator(floor)



            
