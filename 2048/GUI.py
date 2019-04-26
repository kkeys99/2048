from game2d import *
from Twenty import *
from consts import *

class TwentyGUI(GameApp):
    
    def start(self):
        self.game = Twenty()
        self.backdrop = GRectangle(x = GAME_WIDTH/2, y = GAME_HEIGHT/2, width = GAME_HEIGHT, height = GAME_HEIGHT, fillcolor = BACK_COLOR)
        self.block_list = []
        rect_list = []
        for row in range(4):
            rect_list.append([])
            for col in range(4):
                rect_list[row].append(GRectangle(x = BORDER + BORDER * col + REC_SIDE * col + REC_SIDE/2,
                                                 y = BORDER + BORDER * row + REC_SIDE * row + REC_SIDE/2, 
                                                 width = REC_SIDE, height = REC_SIDE, fillcolor = DEFAULT_REC_COLOR))
        self.recs = rect_list

    def update(self,dt):
        self.game.update(self.input, dt)
        active_blocks = self.game.getBlocks()
        self.block_list = []
        for block in active_blocks:
            block.set_rect(GLabel(y = GAME_HEIGHT - (BORDER + BORDER * block.get_row() + REC_SIDE * block.get_row() + REC_SIDE/2),
                           x = BORDER + BORDER * block.get_col() + REC_SIDE * block.get_col() + REC_SIDE/2,
                           width = REC_SIDE, height = REC_SIDE, fillcolor = COLORS[block.get_val()], font_name = 'ClearSans', font_size = 30, text = str(block.get_val())))
            self.block_list.append(block)
            block.update()

    def draw(self):
        self.backdrop.draw(self.view)
        for row in self.recs:
            for rect in row:
                rect.draw(self.view)
        for block in self.block_list:
            block.get_rect().draw(self.view)


if __name__ == '__main__':
    TwentyGUI(width=GAME_WIDTH,height=GAME_HEIGHT).run()