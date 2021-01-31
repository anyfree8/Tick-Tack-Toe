class TickTackToe:
    def __init__(self, name1, name2):
        self.X = name1
        self.O = name2
        self.playing_field = [" "] * 9
        self.win_sequences = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                              [0, 3, 6], [1, 4, 7], [2, 5, 8],
                              [0, 4, 8], [2, 4, 6]]

    def check_move(self):
        countX = self.playing_field.count("X")
        countO = self.playing_field.count("O")
        if countX == countO:
            return True
        else:
            return False

    def make_a_x_move(self, place):
        if self.check_move():
            self.playing_field[place - 1] = "X"
        else:
            print("It is not your turn!")

    def make_a_o_move(self, place):
        if not self.check_move():
            self.playing_field[place - 1] = "O"
        else:
            print("It is not your turn!")

    def withdraw_playing_field(self):
        print(" | ".join(self.playing_field[:3]))
        print("----------")
        print(" | ".join(self.playing_field[3:6]))
        print("----------")
        print(" | ".join(self.playing_field[6:]))

    def is_walking(self):
        if self.check_move():
            print(self.X)
        else:
            print(self.O)

    def is_game_over(self):
        game_over = False
        for seq in self.win_sequences:
            res = ''
            for j in seq:
                res += self.playing_field[j]
                if res == "XXX":
                    game_over = True
                elif res == "OOO":
                    game_over = True
            if game_over:
                print("Game is over!")
                break
        if not game_over:
            print("Game is continue.")

    def is_win(self):
        win = "Game is continue."
        for seq in self.win_sequences:
            res = ''
            for j in seq:
                res += self.playing_field[j]
                if res == "XXX":
                    win = self.X
                elif res == "OOO":
                    win = self.O
            if win != "Game is continue.":
                print(win, "is winner!")
                break
        if win == "Game is continue.":
            print(win)


if __name__ == '__main__':
    first_player, second_player = map(str, input().split())
    game = TickTackToe(first_player, second_player)
    game.is_walking()
    game.make_a_x_move(1)
    game.is_walking()
    game.make_a_x_move(4)
    game.make_a_o_move(4)
    game.make_a_x_move(5)
    game.make_a_o_move(6)
    game.is_win()
    game.make_a_x_move(9)
    game.is_game_over()
    game.withdraw_playing_field()
    game.is_win()
