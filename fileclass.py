class File():

    def __init__(self, newdir, move):
        self.__newdir = newdir
        self.__move = move

    def get_newdir(self):
        return self.__newdir

    def set_newdir(self, newdir):
        self.__newdir = newdir

    def get_move(self):
        return self.__move

    def set_move_false(self):
        move = False
