import tkinter as tk
import random

# Константы игры
BOARD_PATH_LENGTH = 14   # Длина пути
TOKENS_PER_PLAYER = 7    # Количество фишек
CELL_SIZE = 50


class Game:
    def init(self, root):
        self.root = root
        self.root.title("Царская игра Ура")

        self.canvas = tk.Canvas(
            root,
            width=BOARD_PATH_LENGTH * CELL_SIZE,
            height=3 * CELL_SIZE
        )
        self.canvas.pack()

        self.info_label = tk.Label(
            root,
            text="Игрок 1 (красный) бросает кости"
        )
        self.info_label.pack()

        self.roll_button = tk.Button(
            root,
            text="Бросить кости",
            command=self.roll_dice
        )
        self.roll_button.pack()

        self.dice_result = 0
        self.current_player = 1

        # Позиции фишек (-1 = вне доски, 14 = финиш)
        self.positions = {
            1: [-1] * TOKENS_PER_PLAYER,
            2: [-1] * TOKENS_PER_PLAYER
        }

        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")

        # Рисуем клетки
        for i in range(BOARD_PATH_LENGTH):
            x1 = i * CELL_SIZE
            y1 = CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            self.canvas.create_rectangle(x1, y1, x2, y2)

        # Рисуем фишки
        for player in [1, 2]:
            for pos in self.positions[player]:
                if 0 <= pos < BOARD_PATH_LENGTH:
                    x = pos * CELL_SIZE + CELL_SIZE // 2
                    y = CELL_SIZE + CELL_SIZE // 2
                    color = "red" if player == 1 else "blue"
                    self.canvas.create_oval(
                        x - 15, y - 15,
                        x + 15, y + 15,
                        fill=color
                    )

    def roll_dice(self):
        # 4 бинарных кубика (0 или 1)
        self.dice_result = sum(random.randint(0, 1) for _ in range(4))

        self.info_label.config(
            text=f"Игрок {self.current_player} выбросил {self.dice_result}"
        )

        if self.dice_result == 0:
            self.switch_player()
        else:
            self.root.bind("<Button-1>", self.move_token)

    def move_token(self, event):
        for i in range(TOKENS_PER_PLAYER):
            if self.positions[self.current_player][i] < BOARD_PATH_LENGTH:
                new_pos = (
                    self.positions[self.current_player][i]
                    + self.dice_result
                )

                if new_pos > BOARD_PATH_LENGTH:
                    continue

                # Проверка взятия фишки
                opponent = 2 if self.current_player == 1 else 1
                if new_pos in self.positions[opponent]:
                    index = self.positions[opponent].index(new_pos)
                    self.positions[opponent][index] = -1

                self.positions[self.current_player][i] = new_pos
                break

        self.root.unbind("<Button-1>")
        self.draw_board()
        self.check_win()
        self.switch_player()

    def switch_player(self):
        self.current_player = 2 if self.current_player == 1 else 1
        color = "красный" if self.current_player == 1 else "синий"

        self.info_label.config(
            text=f"Игрок {self.current_player} ({color}) ходит"
        )

    def check_win(self):
        if all(
            pos >= BOARD_PATH_LENGTH
            for pos in self.positions[self.current_player]
        ):
            self.info_label.config(
                text=f"Игрок {self.current_player} победил!"
            )
            self.roll_button.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    game = Game()
    root.mainloop()