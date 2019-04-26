import random
import copy
from game2d import *
from consts import *

class Twenty():
    """
    An instance of this class represents the state of the classic game 2048
    
    Instance Variables:
        playGrid: [list] a 2D list which keeps track of the blocks at each position
            0 represents no block, any other value represents a block with that value
    
    Class Variables:
        SPAWNABLE: [tuple] a list of the possible values for spawning blocks into the game
            default is (2,4) but could be changed to alter difficulty
    """
    SPAWNABLE = (2,4)

    def getGrid(self):
        return self.playGrid

    def getBlocks(self):
        return self.blocks

    def getBlock(self, row, col):
        for block in self.blocks:
            if row == block.get_row() and col == block.get_col():
                return block
        raise ValueError('No such block')

    def removeBlock(self, block):
        self.blocks.remove(block)

    def __init__(self):
        """
        The initializer for this game. Creates a new game grid
        and populates it with blocks
        """
        self.blocks = []
        self.playGrid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.pressed = []
        self.spawn_block()
        self.spawn_block()

    def spawn_block(self):
        value = random.choice(self.SPAWNABLE)
        acc = []
        for row in range(4):
            for col in range(4):
                if self.playGrid[row][col] == 0:
                    acc.append((row,col))
        new_location = random.choice(acc)
        self.playGrid[new_location[0]][new_location[1]] = value
        block = Block(new_location[0],new_location[1],value)
        self.blocks.append(block)
        block.set_rect(GLabel(y = GAME_HEIGHT - (BORDER + BORDER * block.get_row() + REC_SIDE * block.get_row() + REC_SIDE/2),
                           x = BORDER + BORDER * block.get_col() + REC_SIDE * block.get_col() + REC_SIDE/2,
                           width = STARTING_WIDTH, height = STARTING_WIDTH, fillcolor = COLORS[block.get_val()], 
                           font_name = 'ClearSans', font_size = 30, text = str(block.get_val())))


    def move(self,direction):
        """
        Moves all block in the direction specified if possible

        Parameter directon: the direction to move
        Precondition: [str] either up, down, left or right
        """
        old_grid = copy.deepcopy(self.playGrid)
        if direction == 'up':
            for row in range(1,4):
                for col in range(4):
                    if self.playGrid[row][col] != 0:
                        r = row; c = col
                        while r > 0 and self.playGrid[r-1][c] == 0:
                            self.playGrid[r-1][c] = self.playGrid[r][c]
                            self.playGrid[r][c] = 0

                            self.getBlock(r,c).move(r-1, c)
                            r -= 1
                        if r > 0 and self.playGrid[r-1][c] == self.playGrid[r][c]:
                            self.playGrid[r-1][c] *= 2
                            self.playGrid[r][c] = 0

                            self.getBlock(r-1,c).double()
                            self.getBlock(r-1,c).pulse()
                            self.removeBlock(self.getBlock(r,c))

        if direction == 'down':
            for row in range(2,-1,-1):
                for col in range(4):
                    if self.playGrid[row][col] != 0:
                        r = row; c = col
                        while r < 3 and self.playGrid[r+1][c] == 0:
                            self.playGrid[r+1][c] = self.playGrid[r][c]
                            self.playGrid[r][c] = 0

                            self.getBlock(r,c).move(r+1, c)
                            r += 1
                        if r < 3 and self.playGrid[r+1][c] == self.playGrid[r][c]:
                            self.playGrid[r+1][c] *= 2
                            self.playGrid[r][c] = 0

                            self.getBlock(r+1,c).double()
                            self.getBlock(r+1,c).pulse()
                            self.removeBlock(self.getBlock(r,c))

        if direction == 'right':
            for row in range(4):
                for col in range(2,-1,-1):
                    if self.playGrid[row][col] != 0:
                        r = row; c = col
                        while c < 3 and self.playGrid[r][c+1] == 0:
                            self.playGrid[r][c+1] = self.playGrid[r][c]
                            self.playGrid[r][c] = 0

                            self.getBlock(r,c).move(r, c+1)
                            c += 1
                        if c < 3 and self.playGrid[r][c+1] == self.playGrid[r][c]:
                            self.playGrid[r][c+1] *= 2
                            self.playGrid[r][c] = 0

                            self.getBlock(r,c+1).double()
                            self.getBlock(r,c+1).pulse()
                            self.removeBlock(self.getBlock(r,c))

        if direction == 'left':
            for row in range(4):
                for col in range(1,4):
                    if self.playGrid[row][col] != 0:
                        r = row; c = col
                        while c > 0 and self.playGrid[r][c-1] == 0:
                            self.playGrid[r][c-1] = self.playGrid[r][c]
                            self.playGrid[r][c] = 0

                            self.getBlock(r,c).move(r, c-1)
                            c -= 1
                        if c > 0 and self.playGrid[r][c-1] == self.playGrid[r][c]:
                            self.playGrid[r][c-1] *= 2
                            self.playGrid[r][c] = 0

                            self.getBlock(r,c-1).double()
                            self.getBlock(r,c-1).pulse()
                            self.removeBlock(self.getBlock(r,c))
        if old_grid != self.playGrid:
            self.spawn_block()

    def print_grid(self):
        """
        Prints current state of the game in an easy to read 
        format to the terminal
        """
        for row in self.playGrid:
            print(' ------- ------- ------- -------')
            print('|       |       |       |       |')
            rowStr = ''
            for element in row:
                if element == 0:
                    element = ' ' 
                element_length = len(str(element))
                rowStr += '|   ' + str(element) + ' ' * (4-element_length)
            print(rowStr + '|')
            print('|       |       |       |       |')
        print(' ------- ------- ------- -------')
    
    def check_for_moves(self, theInput):
        moves = ('up', 'down', 'left', 'right')
        for direction in moves:
            if theInput.is_key_down(direction) and direction not in self.pressed:
                self.move(direction)
                self.print_grid()
                self.pressed.append(direction)
            elif not theInput.is_key_down(direction) and direction in self.pressed:
                self.pressed.remove(direction)


    def update(self, theInput, dt):
        #self.print_grid()
        self.check_for_moves(theInput)


class Block():
    def update(self):
        if self.rect is not None:
            if self.pulsing:
                if self.rect.width < PULSE_SIZE and not self.maxpulse:
                    self.rect.width += PULSE_RATE
                elif self.rect.width > REC_SIDE:
                    self.maxpulse = True
                    self.rect.width -= PULSE_RATE
                else:
                    self.pulsing = False
                if self.rect.height < PULSE_SIZE and not self.maxpulse:
                    self.rect.height += PULSE_RATE
                elif self.rect.height > REC_SIDE:
                    self.maxpulse = True
                    self.rect.height -= PULSE_RATE
                else:
                    self.pulsing = False
            if self.rect.width < REC_SIDE:
                self.rect.width += GROWTH_RATE
            if self.rect.height < REC_SIDE:
                self.rect.height += GROWTH_RATE
            self.rect.x += self.dx * MOVE_TIME
            self.rect.y += self.dy * MOVE_TIME

    def pulse(self):
        self.pulsing = True
        self.maxpulse = False

    def get_rect(self):
        return self.rect

    def set_rect(self,rect):
        if self.rect is None:
            self.rect = rect
        else:
            self.dx = rect.x - self.rect.x
            self.dy = rect.y - self.rect.y
            self.rect.text = rect.text
            self.rect.fillcolor = rect.fillcolor
            self.rect.font_name = rect.font_name
            #self.rect.font_size = rect.font_size

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def get_val(self):
        return self.val

    def move(self, newrow, newcol):
        self.row = newrow
        self.col = newcol

    def double(self):
        self.val *= 2

    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.val = value
        self.rect = None
        self.dx = 0
        self.dy = 0
        self.dt = 0
        self.pulsing = False
        self.maxpulse = False