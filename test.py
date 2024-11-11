import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk
from tkinter import messagebox
from io import StringIO

from main import CalculatorApp


class TestCalculatorApp(unittest.TestCase):

    @patch('tkinter.messagebox.showerror')
    def test_display_error_called_on_invalid_expression(self, mock_showerror):

        root = tk.Tk()
        app = CalculatorApp(root)

        app.display.insert(tk.END, '1 / 0')
        app.on_button_click('=')

        mock_showerror.assert_called_with("Ошибка", "Ошибка вычисления!")

    @patch.object(CalculatorApp, 'display_error')
    def test_clear_display(self, mock_display_error):

        root = tk.Tk()
        app = CalculatorApp(root)

        app.display.insert(tk.END, "12345")
        app.clear_display()

        self.assertEqual(app.display.get(), "")

    @patch.object(CalculatorApp, 'display_error')
    @patch('tkinter.messagebox.showerror')
    def test_button_click(self, mock_showerror, mock_display_error):

        root = tk.Tk()
        app = CalculatorApp(root)


        app.on_button_click('1')
        self.assertEqual(app.display.get(), "1")

        app.on_button_click('+')
        self.assertEqual(app.display.get(), "1+")

        app.on_button_click('2')
        self.assertEqual(app.display.get(), "1+2")

        app.on_button_click('=')
        self.assertEqual(app.display.get(), "3")

    @patch('tkinter.messagebox.showerror')
    def test_invalid_expression(self, mock_showerror):
        # Создаем объект приложения
        root = tk.Tk()
        app = CalculatorApp(root)


        app.display.insert(tk.END, "1 / 0")
        app.on_button_click("=")


        mock_showerror.assert_called_once_with("Ошибка", "Ошибка вычисления!")


if __name__ == '__main__':
    unittest.main()
