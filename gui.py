import tkinter as tk
from tkinter import font as tkFont
from tkinter import messagebox
from calculator import Calculator

class CalculatorApp(tk.Tk):
    """
    CalculatorApp class represents the main application window for the UNO Calculator.

    This calculator provides a user interface for performing basic mathematical operations,
    including addition, subtraction, multiplication, division, exponentiation, and more.

    Attributes:
    - calculator_font (tkFont.Font): Font for calculator buttons.
    - display_font (tkFont.Font): Font for the display entry.
    - bg_color (str): Background color of the calculator.
    - button_color (str): Color for general buttons.
    - number_button_color (str): Color for number buttons.
    - special_button_color (str): Color for special function buttons.
    - equal_button_color (str): Color for the equal button.
    - text_color (str): Color for text on buttons.
    - display_text_color (str): Color for text in the display entry.
    - current_operation (str): Current mathematical operation (e.g., '+', '-', '*', '/').
    - first_number (float): First number in a mathematical operation.
    - last_result (float): Result of the last completed calculation.
    - new_input (bool): Flag indicating whether a new input is expected.
    - calculation_completed (bool): Flag indicating whether a calculation has been completed.

    Methods:
    - create_widgets(): Create the GUI widgets for the calculator.
    - adjust_window_size(): Adjust the window size of the calculator.
    - on_button_click(button_value): Handle button clicks for the calculator.
    - perform_operation(): Perform the mathematical operation based on the current state.
    - update_display(value): Update the display of the calculator with the given value.
    - show_error_popup(message): Display an error popup with the provided message.
    """
    def __init__(self):
        """
        Initialize the UNO Calculator application.
        """

        super().__init__()
        self.title("UNO Calculator")
        self.calculator_font = tkFont.Font(family="Courier", size=18)
        self.display_font = tkFont.Font(family="Courier", size=24)

        # UNO colors
        self.bg_color = "#222222"  # Dark Gray
        self.button_color = "#dddddd"  # Black
        self.number_button_color = "#999999"  # Light Gray
        self.special_button_color = "#FF0000"  # Red
        self.equal_button_color = "#FFFFFF"  # White
        self.text_color = "#000000"  # Black
        self.display_text_color = "#FF0000"  # Red

        self.configure(bg=self.bg_color)
        self.current_operation = None
        self.first_number = None
        self.last_result = None
        self.new_input = True
        self.calculation_completed = False

        self.create_widgets()
        self.adjust_window_size()

    def create_widgets(self):
        """
        Create the GUI widgets for the calculator.
        """

        # Display Entry - adjusted to span the full width
        self.display = tk.Entry(self, font=self.display_font, fg=self.display_text_color, bg=self.button_color, borderwidth=2, relief="groove")
        self.display.grid(row=0, column=0, columnspan=7, padx=0, pady=15)  # span across all columns
        
        # Define buttons with their labels, positions, and specific colors
        buttons = [
            ('7', 1, 0, self.number_button_color),
            ('8', 1, 1, self.number_button_color),
            ('9', 1, 2, self.number_button_color),
            ('!', 1, 3, self.button_color),
            ('/', 1, 4, self.button_color),
            ('4', 2, 0, self.number_button_color),
            ('5', 2, 1, self.number_button_color),
            ('6', 2, 2, self.number_button_color),
            ('x^y', 2, 3, self.button_color),
            ('*', 2, 4, self.button_color),
            ('1', 3, 0, self.number_button_color),
            ('2', 3, 1, self.number_button_color),
            ('3', 3, 2, self.number_button_color),
            ('x^2', 3, 3, self.button_color),
            ('-', 3, 4, self.button_color),
            ('+/-', 4, 0, self.button_color),
            ('0', 4, 1, self.number_button_color),
            ('.', 4, 2, self.button_color),
            ('ln', 4, 3, self.button_color),
            ('+', 4, 4, self.button_color),
            ('C', 5, 0, self.special_button_color),
            ('Del', 5, 1, self.button_color),
            ('sqrt', 5, 2, self.button_color),
            ('e^x', 5, 3, self.button_color),
            ('=', 5, 4, self.equal_button_color),
        ]
        
        for label, row, col, bg_color in buttons:
            # Create a button
            button = tk.Button(self, text=label, font=self.calculator_font, 
                               fg=self.text_color, bg=bg_color, 
                               command=lambda l=label: self.on_button_click(l))
            # Place the button in the grid starting from column 1
            button.grid(row=row + 1, column=col + 1, sticky="nsew", padx=5, pady=5)
            button.config(width=4)

        # Add spacer frames for horizontal padding
        left_spacer = tk.Frame(self, width=20, bg=self.bg_color)
        left_spacer.grid(row=1, column=0, rowspan=7)

        right_spacer = tk.Frame(self, width=20, bg=self.bg_color)
        right_spacer.grid(row=1, column=6, rowspan=7)

        # Add spacer for extra space below the last row of buttons
        bottom_spacer = tk.Frame(self, height=20, bg=self.bg_color)
        bottom_spacer.grid(row=8, column=0, columnspan=7)

        # Force update the window after all buttons are created
        self.update()
    
    def adjust_window_size(self):
        """
        Adjust the window size of the calculator.
        """

        self.update_idletasks()
        self.resizable(False, False)

    def on_button_click(self, button_value):
        """
        Handle button clicks for the calculator.

        Parameters:
        - button_value (str): The value of the button clicked.
        """
        if button_value in {'+', '-', '*', '/', 'x^y'}:
            if self.current_operation:
                self.perform_operation()  # Perform the current operation
                self.first_number = self.last_result  # Use the result as the first number for the next operation
            else:
                self.first_number = float(self.display.get()) if self.display.get() else 0
                self.last_result = self.first_number

            self.current_operation = button_value  # Set the new operation
            self.new_input = True  # Prepare for the new input
            self.calculation_completed = False

        elif button_value == '=':
            self.perform_operation()

        elif button_value in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}:
            if self.calculation_completed:
                self.display.delete(0, tk.END)
                self.calculation_completed = False

            if button_value == '.' and '.' in self.display.get():
                # If the button is a period and there's already a period in the display, do nothing
                return

            if self.new_input:
                self.display.delete(0, tk.END)
                self.new_input = False
            self.display.insert(tk.END, button_value)

        elif button_value == 'C':
            self.display.delete(0, tk.END)
            self.current_operation = None
            self.first_number = None
            self.last_result = None
            self.new_input = True

        elif button_value == '+/-':
            current_value = self.display.get()
            if current_value:
                new_value = -float(current_value)
                self.update_display(new_value)

        elif button_value == '!':
            current_value = self.display.get()
            if current_value.isdigit():
                try:
                    result = Calculator.factorial(int(current_value))
                    self.update_display(result)
                except ValueError as ve:
                    self.show_error_popup(str(ve))
            self.calculation_completed = True

        elif button_value == 'x^2':
            current_value = self.display.get()
            if current_value:
                result = Calculator.power(float(current_value), 2)
                self.update_display(result)
            self.calculation_completed = True

        elif button_value == 'ln':
            current_value = self.display.get()
            if current_value:
                try:
                    result = Calculator.natural_log(float(current_value))
                    self.update_display(result)
                except ValueError as ve:
                    self.show_error_popup(str(ve))
            self.calculation_completed = True

        elif button_value == 'sqrt':
            current_value = self.display.get()
            if current_value:
                try:
                    result = Calculator.square_root(float(current_value))
                    self.update_display(result)
                except ValueError as ve:
                    self.show_error_popup(str(ve))
            self.calculation_completed = True

        elif button_value == 'e^x':
            current_value = self.display.get()
            if current_value:
                result = Calculator.exp(float(current_value))
                self.update_display(result)
            self.calculation_completed = True

        elif button_value == 'Del':
            current_value = self.display.get()
            if current_value:
                # Delete the last character
                self.display.delete(len(self.display.get())-1, tk.END)
            else:
                # Handle cases where the display is empty or invalid
                self.display.delete(0, tk.END)

    def perform_operation(self):
        """
        Perform the mathematical operation based on the current state.
        """
        # Ensure there is a first number to operate on
        if self.first_number is None:
            self.first_number = 0

        second_number = float(self.display.get()) if self.display.get() else 0

        # If no operation is set, just display the second number or the first number if the second is 0
        if self.current_operation is None:
            result = second_number if second_number != 0 else self.first_number
            self.update_display(result)
            self.last_result = result
            return

        try:
            # Perform the operation based on the current_operation
            if self.current_operation == '+':
                self.last_result = Calculator.add(self.first_number, second_number)
            elif self.current_operation == '-':
                self.last_result = Calculator.subtract(self.first_number, second_number)
            elif self.current_operation == '*':
                self.last_result = Calculator.multiply(self.first_number, second_number)
            elif self.current_operation == '/':
                self.last_result = Calculator.divide(self.first_number, second_number)
            elif self.current_operation == 'x^y':
                self.last_result = Calculator.power(self.first_number, second_number)

            # Update the display with the result
            self.update_display(self.last_result)

        except ValueError as ve:
            self.show_error_popup(str(ve))
        except OverflowError as oe:
            self.show_error_popup(str(oe))
        except Exception as e:
            self.show_error_popup(f"Error: {e}")
            return

        # Reset the operation state for the next calculation
        self.current_operation = None
        self.new_input = True
        self.calculation_completed = True

    def update_display(self, value):
        """
        Update the display of the calculator with the given value.

        Parameters:
        - value: The value to be displayed on the calculator.
        """
        if isinstance(value, float) and value.is_integer():
            value = int(value)
        self.display.delete(0, tk.END)
        self.display.insert(0, str(value))

    def show_error_popup(self, message):
        """
        Display an error popup with the provided message.

        Parameters:
        - message (str): The error message to be displayed.
        """
        messagebox.showerror("Error", message)

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
