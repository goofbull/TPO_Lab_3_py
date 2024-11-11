import tkinter as tk
from tkinter import messagebox


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")

        self.display = tk.Entry(self.root, width=30, borderwidth=5, font=("Arial", 14), justify='right')
        self.display.grid(row=0, column=0, columnspan=4)

        # Кнопки калькулятора
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

        self.clear_button = tk.Button(self.root, text="C", width=10, height=2, font=("Arial", 12),
                                      command=self.clear_display)
        self.clear_button.grid(row=5, column=0, columnspan=4)

    def create_button(self, text, row, col):
        button = tk.Button(self.root, text=text, width=10, height=2, font=("Arial", 12),
                           command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col)

    def on_button_click(self, value):
        current_text = self.display.get()

        if value == '=':
            try:
                result = eval(current_text)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display_error("Ошибка вычисления!")
        elif value == 'C':
            self.clear_display()
        else:
            self.display.insert(tk.END, value)

    def clear_display(self):
        self.display.delete(0, tk.END)

    def display_error(self, message):
        messagebox.showerror("Ошибка", message)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
