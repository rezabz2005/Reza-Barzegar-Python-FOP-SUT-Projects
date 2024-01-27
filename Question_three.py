class soldier:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.health = 100
class melee(soldier):
    def __init__(self, id, x, y):
        super().__init__(id, x, y)
        self.damage = 20
class archer(soldier):
    def __init__(self, id, x, y):
        super().__init__(id, x, y)
        self.damage = 10
class game:
    def __init__(self, number_value):
        self.map = [[None]*number_value for _ in range(number_value)]
        self.player = [[],[]]
        self.turn = 0
    def new(self,soldier_type, id, x, y):
        for soldier in self.player[self.turn]:
            if( soldier.id == id ):
                print("duplicate tag")
                return
        if( soldier_type == "melee" ):
            soldier = melee(id, x, y)
        elif( soldier_type == "archer" ):
            soldier = archer(id, x, y)
        self.player[self.turn].append(soldier)
        self.map[y][x] = soldier
        self.turn = 1 - self.turn
    def move(self, id, direction):
        for soldier in self.player[self.turn]:
            if( soldier.id == id ):
                if( direction == "up" ):
                    if( soldier.y - 1 < 0 ):
                        print("out of bounds")
                    else:
                        soldier.y -= 1
                elif( direction == "down" ):
                    if( soldier.y + 1 > number_value - 1 ):
                        print("out of bounds")
                    else:
                        soldier.y += 1
                elif( direction == "left" ):
                    if( soldier.x - 1 < 0 ):
                        print("out of bounds")
                    else:
                        soldier.x -= 1
                elif( direction == "right" ):
                    if( soldier.x + 1 > number_value - 1 ):
                        print("out of bounds")
                    else:
                        soldier.x += 1
                self.turn = 1 - self.turn
                return
        print("soldier does not exist")
    def attack(self, attacker_id, target_id):
        for attacker in self.player[self.turn]:
            if( attacker.id == attacker_id ):
                for target in self.player[1 - self.turn]:
                    if( target_id == target.id ):
                        if( int((abs(attacker.x - target.x))**2 + (abs(attacker.y - target.y))**2)**0.5 <= attacker.damage//10 ):
                            target.health -= attacker.damage

                            if( target.health <= 0 ):
                                self.player[1 - self.turn].remove(target)
                                print("target eliminated")
                            self.turn = 1 - self.turn
                            return
                        else:
                            print("the target is too far")
                            self.turn = 1 - self.turn
                            return
    def info(self, id):
        for soldier in self.player[self.turn]:
            if( soldier.id == id ):
                print(f"health:  {soldier.health}")
                print(f"location:  {soldier.x}   {soldier.y}")
                self.turn = 1 - self.turn
                return
        self.turn = 1 - self.turn
        print("soldier does not exist")
        return
    def who(self):
        health_0, health_1 = 0, 0
        for soldier in self.player[0]:
            health_0 += soldier.health
        for soldier in self.player[1]:
            health_1 += soldier.health
        if( health_1 < health_0 ):
            print("player  1")
        elif( health_0 < health_1 ):
            print("player  2")
        else:
            print("draw")
number_value = int(input())

g = game(number_value)

while True:
    act_string = input().split()

    if( act_string[0] == "end" ):
        break
    elif( act_string[0] == "new" ):
        g.new(act_string[1], int(act_string[2]), int(act_string[3]), int(act_string[4]))
    elif( act_string[0] == "move" ):
        g.move(int(act_string[1]), act_string[2])
    elif( act_string[0] == "attack" ):
        g.attack(int(act_string[1]), int(act_string[2]))
    elif( act_string[0] == "info" ):
        g.info(int(act_string[1]))
    elif( act_string[0] == "who" ):
        g.who()

