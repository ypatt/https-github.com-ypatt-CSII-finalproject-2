# main.py
# This script serves as the entry point for the calculator application.

from gui import CalculatorApp  # Ensure this import works correctly

def main():
    """
    Initialize and start the calculator application.
    """
    try:
        app = CalculatorApp()
        app.mainloop()  # Changed from app.run() to app.mainloop()
    except Exception as e:
        print(f"An error occurred while starting the application: {e}")

if __name__ == "__main__":
    main()
