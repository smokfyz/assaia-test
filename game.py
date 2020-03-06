import settings
import random
import sys


class GameConnect4:
    def __init__(self,
                field_height=settings.FIELD_HEIGHT,
                field_width=settings.FIELD_WIDTH,
                length_to_win=settings.LENGTH_TO_WIN,
                num_of_players=settings.NUMBER_OF_PLAYERS):
        self.field = [['X' for i in range(field_width)] for j in range(field_height)]
        self.num_of_players = num_of_players
        self.length_to_win = length_to_win
        self.current_player = random.randint(0, self.num_of_players - 1)

    def win_check(self):
        cells_count = 0
        for row in self.field:
            for cell in row:
                if cell == self.current_player:
                    cells_count += 1
                    if cells_count == self.length_to_win:
                        return True
                else:
                    cells_count = 0
        return False

    def turn(self, col):
        if self.field[0][col] != 'X':
            raise ValueError
        
        for i, row in enumerate(self.field):
            if row[col] == 'X':
                continue
            else:
                self.field[i-1][col] = self.current_player
                break
        else:
            row[col] = self.current_player

    def print_field(self):
        print()
        print(" ".join(str(n) for n in range(0, len(self.field[0]))))
        for row in self.field:
            print("\n" + " ".join(str(n) for n in row))
        print()

    def next_player(self):
        self.current_player = (self.current_player + 1) % self.num_of_players

    def start(self):
        while not self.win_check():
            self.next_player()
            self.print_field()
            print(f"Turn of the Player {self.current_player}!")
            while True:
                try:
                    col = int(input(f"Select a column: "))
                    self.turn(col)
                    break
                except ValueError:
                    print("Wrong column! Please, try again.")
            
        self.print_field()
        print(f"\n*** Player {self.current_player} win! ***\n")


if __name__ == "__main__":
    game = GameConnect4()
    game.start()
