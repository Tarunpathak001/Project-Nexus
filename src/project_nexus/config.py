import os
class Config:
    API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    ASSETS_DIR = os.path.join(BASE_DIR, "assets")
    IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
    STICKY_NOTE_PATH = os.path.join(ASSETS_DIR, "sticky_note", "index.html")
    DB_PATH = os.path.join(BASE_DIR, "nexus.db")