import tkinter as tk

CELL_SIZE = 40
ROWS = 10
COLS = 10
ERASER_SIZE = 60

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas Eraser")

        self.canvas = tk.Canvas(root, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE, bg="white")
        self.canvas.pack()

        self.cells = []
        self.draw_grid()

        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="gray", outline="black")
        self.canvas.bind("<B1-Motion>", self.move_eraser)  # Drag with left click

    def draw_grid(self):
        for i in range(ROWS):
            row = []
            for j in range(COLS):
                x1 = j * CELL_SIZE
                y1 = i * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
                row.append(rect)
            self.cells.append(row)

    def move_eraser(self, event):
        x1 = event.x - ERASER_SIZE // 2
        y1 = event.y - ERASER_SIZE // 2
        x2 = x1 + ERASER_SIZE
        y2 = y1 + ERASER_SIZE

        self.canvas.coords(self.eraser, x1, y1, x2, y2)

        for row in self.cells:
            for rect in row:
                coords = self.canvas.coords(rect)
                if self.rectangles_overlap((x1, y1, x2, y2), coords):
                    self.canvas.itemconfig(rect, fill="white")

    def rectangles_overlap(self, r1, r2):
        return not (r1[2] < r2[0] or r1[0] > r2[2] or r1[3] < r2[1] or r1[1] > r2[3])

if __name__ == "__main__":
    root = tk.Tk()
    app = EraserApp(root)
    root.mainloop()
