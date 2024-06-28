from turtle import Screen


class PlayArea():
    window = Screen()
    width = 800
    height = 600
    window.listen()

    def __init__(self):
        super().__init__()
        self.window.setup(self.width, self.height)

    def bind_press_action(self, action_key, function):
        self.window.onkeypress(key=action_key, fun=function)

    def bind_release_action(self, action_key, function):
        self.window.onkeyrelease(key=action_key, fun=function)
