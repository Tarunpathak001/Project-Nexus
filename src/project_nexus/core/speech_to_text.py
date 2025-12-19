import speech_recognition as sr
class SpeechToTextService:
    def __init__(self):
        self.recognizer = sr.Recognizer()
    def listen(self):
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)
                text = self.recognizer.recognize_google(audio)
                return {"text": text}
        except sr.UnknownValueError:
            return {"error": "Could not understand the audio"}
        except sr.RequestError as e:
            return {"error": f"Could not request results; {e}"}
        except Exception as e:
             return {"error": f"Error: {e}"}
stt_service = SpeechToTextService()