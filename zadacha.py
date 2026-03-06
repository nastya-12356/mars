import arcade

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TITLE = "Texture"


class MyGame(arcade.Window):
    def __init__(self, width, height, title, filename):
        super().__init__(width, height, title)
        self.filename = filename
        self.background = None

    def setup(self):
        # Строка должна быть строго ВНУТРИ метода setup с отступом!
        # Здесь self существует и указывает на текущий объект игры.
        file_path = f"images/backgrounds/{self.filename}"
        self.background = arcade.load_texture(file_path)

    def on_draw(self):
        self.clear()
        # Самый универсальный способ для новых версий:
        arcade.draw_texture_rect(
            texture=self.background,
            rect=arcade.LRBT(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)
        )




def setup_game(width=800, height=600, title="Texture", filename='fon1.png'):
    game = MyGame(width, height, title, filename)
    game.setup()
    return game


if __name__ == "__main__":
    setup_game()
    arcade.run()
