from deep_translator import GoogleTranslator

class TranslatorService:
    def __init__(self):
        self._lang_map = GoogleTranslator().get_supported_languages(as_dict=True)
        self.languages = {v: k.title() for k, v in self._lang_map.items()}

    def translate(self, text, src_lang, dest_lang):
        try:
            src_code = self._lang_map.get(src_lang.lower(), 'auto')
            dest_code = self._lang_map.get(dest_lang.lower(), 'en')
            
            translator = GoogleTranslator(source=src_code, target=dest_code)
            translated_text = translator.translate(text)
            
            return {
                "text": translated_text,
                "pronunciation": ""
            }
        except Exception as e:
            return {"error": str(e)}

translator_service = TranslatorService()