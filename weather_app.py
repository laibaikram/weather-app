from tkinter import Tk
from weather_gui import WeatherGUI

def main():
    # Create the main window
    root = Tk()
    root.title("Weather App")
    
    # Create the WeatherGUI instance
    app = WeatherGUI(root)
    
    # Start the application main loop
    root.mainloop()

if __name__ == '__main__':
    main()
