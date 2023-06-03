from tkinter import Label, Entry, Button, messagebox
from weather_api import WeatherAPI

class WeatherGUI:
    def __init__(self, root):
        self.root = root
        
        # Create weather API instance
        self.weather_api = WeatherAPI()
        
        # Create UI elements
        self.label_city = Label(root, text="Enter City:")
        self.entry_city = Entry(root)
        self.button_get_weather = Button(root, text="Get Weather", command=self.get_weather)
        self.label_weather_info = Label(root, text="")
        
        # Set UI element positions
        self.label_city.pack()
        self.entry_city.pack()
        self.button_get_weather.pack()
        self.label_weather_info.pack()
    
    def get_weather(self):
        city = self.entry_city.get()
        if city:
            try:
                # Get weather information
                weather_info = self.weather_api.get_weather(city)
                
                # Display weather information
                self.label_weather_info.config(text=weather_info)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Warning", "Please enter a city.")

