import re
import Classes.Wall as w
import Classes.Brick as b
import Classes.Powerup as p
import Classes.Button as btn
import Classes.Player_object_board as Player_ob

class Game_state:
    level = []
    last_pos = ''

    def __init__(self):
        print("Inicjalizacja stanu gry")
        self.game = [[0 for col in range(15)] for row in range(15)]
        for i in range(len(self.game)):
            for j in range(len(self.game[i])):
                self.game[i][j] = 0

    # board = "WWWWWWWWWWWWWWWW    BB       WW W W WBW W W WW       B     WWBW W W W W W WW    BBB    BBWW W W W W W WBWW      BB BB  WW W W W W W W WW             WW W W W W W W WW             WW W W W W W W WW             WWWWWWWWWWWWWWWW"
    def set_board(self, board):
        self.level = map(''.join, zip(*[iter(board)]*15))
        self.walls_bricks()

    def walls_bricks(self):
        x = 450
        y = 0
        for row in self.level:
            for col in row:
                if col == "W":
                    wal = w.Wall((x, y))
                    # x is a multiply of 50 f.ex 450, y also
                    # so it's easier to have element table[1][1] than table[50][50] etc
                    # table_x, table_y - [0-15][0-15]
                    # x,y - [450-1150][0-700]
                    table_x, table_y = self.table_dimension(y, x)
                    self.game[table_x][table_y] = wal.get_wall()
                elif col == "B":
                    brick = b.Brick((x, y))
                    table_x, table_y = self.table_dimension(y, x)
                    self.game[table_x][table_y] = brick.get_brick()
                    powerUP = p.Powerup((x, y))
                    # rand = random.randint(0, 100)
                    # if (rand > 0):

                    # table_x, table_y = self.table_dimension(y, x)
                    # self.powerups_array[table_x][table_y] = powerUP.get_powerup()
                x += 50
            y += 50
            x = 450

        if(self.last_pos == ''):
            self.game[1][1] = Player_ob.Player_object_board((1,1), 1)
            self.last_pos = (1,1)

        self.show_board()

    def table_dimension(self, x, y):
        return int(x/50), int((y-450)/50)


    def show_board(self):
        print("w show_board")
        for i in range(len(self.game)):
            for j in range(len(self.game[i])):
                if(self.game[i][j] != 0):
                    print(self.game[i][j].desc, end="\t")
                    #print("x ", i, " y ", j, " ", self.game[i][j].desc, end='\n')
                else:
                    print("empty", end="\t")
                    #print("x ", i, " y ", j, " empty", end='\n')
            print(end='\n')

    def set_player_position(self, player_number, position):

        x = int(re.search('P x(.*)y', position).group(1))
        y = int(re.search('y(.*)', position).group(1))

        # removing player from last position
        self.game[self.last_pos[0]][self.last_pos[1]] = 0

        # set current position of player
        self.game[y][x] = Player_ob.Player_object_board((x, y), player_number)
        self.last_pos = y,x
        self.show_board()




