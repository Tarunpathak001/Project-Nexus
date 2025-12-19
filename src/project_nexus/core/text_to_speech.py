import pyttsx3
class TextToSpeechService:
    def __init__(self):
        self.engine = pyttsx3.init()
    def speak(self, text):
        if text:
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except Exception as e:
                print(f"TTS Error: {e}")
tts_service = TextToSpeechService()