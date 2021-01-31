class TickTackToe:
    def __init__(self, name1, name2):
        self.X = name1
        self.O = name2
        self.playing_field = [" "] * 9


if __name__ == '__main__':
    first_player, second_player = map(str, input().split())
    game = TickTackToe(first_player, second_player)
