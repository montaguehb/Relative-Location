import numpy

class Room():
    all = []
    directions = {
        #rotate player's heading 360, 180, 270, or 90 degrees respectively 
    "forward": numpy.array([[1, 0],
                            [0, 1]]),
    "back": numpy.array([[-1, 0],
                         [0, -1]]),
    "left": numpy.array([[0, 1],
                         [-1, 0]]),
    "right": numpy.array([[0, -1],
                          [1, 0]]),
    }
    
    def __init__(self, num, x=None, y=None, negative_x=None, negative_y=None):
        self.num = num
        self.rooms = {(1, 0): x, 
                      (0, 1): y,
                      (-1, 0): negative_x,
                      (0, -1): negative_y
                      }
        
        Room.all.append(self)

    @classmethod
    def find_by_num(cls, num):
        return [room for room in cls.all if room.num == num][0]
    
class Player():
    def __init__(self, room):
        self.current_room = room
        self.heading = numpy.array([1, 0])

    def move(self, rot_matrix):
        self.heading = numpy.matmul(self.heading, rot_matrix)
        self.current_room = Room.find_by_num(self.current_room.rooms.get(tuple(self.heading)))

# Could be done more efficiently using iteration, only need to technically set half the values and can find the other half using inferences.
# e.g. the postitive y for the room at negative_y for 0 is 0               
Room(0, x=5, negative_y=1)
Room(1, x=4, y=0, negative_y=2)
Room(2, x=3, y=1)
Room(3, x=8, y=4, negative_x=2) 
Room(4, x=7, y=5, negative_x=1, negative_y=3) 
Room(5, x=6, negative_x=0, negative_y=4) 
Room(6, negative_x=5, negative_y=7) 
Room(7, y=6, negative_x=4, negative_y=8) 
Room(8, y=7, negative_x=3)  

new_player = Player(room=Room.find_by_num(0))

moving = True
direction_list = [key for key, value in Room.directions.items()]
while moving:
    print(f"The current room num is {new_player.current_room.num}")
    user_input = input("input a direction:")
    if user_input == ".exit":
        break
    elif user_input in new_player.current_room.direction_list:
        new_player.move(Room.directions.get(user_input))
        
        
        
        