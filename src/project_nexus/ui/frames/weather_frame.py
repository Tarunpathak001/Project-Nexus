import customtkinter as ctk
from .modern_base_frame import ModernBaseFrame
from ...core.weather import weather_service
from ...core.text_to_speech import tts_service
from ...core.logger import logger

class WeatherFrame(ModernBaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "weather.png")
        
        self.label = ctk.CTkLabel(self.content_frame, text="🌤️ Weather Information", font=("Roboto Medium", 24))
        self.label.pack(pady=10)
        
        self.city_entry = ctk.CTkEntry(self.content_frame, placeholder_text="Enter City Name", width=300)
        self.city_entry.pack(pady=10)
        self.city_entry.bind("<Return>", lambda event: self.get_weather())
        
        ctk.CTkButton(self.content_frame, text="Get Weather", command=self.get_weather).pack(pady=5)
        
        self.output_label = ctk.CTkLabel(self.content_frame, text="", font=("Roboto", 16), justify="left")
        self.output_label.pack(pady=20)
        
        self.add_back_button()

    def get_weather(self):
        city = self.city_entry.get().strip()
        if not city:
            self.output_label.configure(text="Please enter a city name.")
            return
            
        result = weather_service.get_weather(city)
        if "error" in result:
             self.output_label.configure(text=f"Error: {result['error']}")
             tts_service.speak(result["error"])
        else:
             info = f"📍 Location: {city}\n🌡️ Temp: {result['temp']}°C\n☁️ Condition: {result['main']}\n📝 Description: {result['description']}"
             self.output_label.configure(text=info)
             tts_service.speak(f"The weather in {city} is {result['description']} with {result['temp']} degrees.")