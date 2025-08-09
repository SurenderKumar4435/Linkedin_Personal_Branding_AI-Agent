




from googletrans import Translator, LANGUAGES

def translate_text(text: str, dest_lang: str = "hi"):
    """
    Translate text to a specified language using Google Translate unofficial API.
    
    Args:
        text (str): Text to translate.
        dest_lang (str): Target language code (e.g., 'hi' for Hindi).
    
    Returns:
        str: Translated text or error message.
    """
    try:
        if dest_lang not in LANGUAGES:
            return f"Unsupported language code: '{dest_lang}'."

        translator = Translator()
        translated = translator.translate(text, dest=dest_lang)
        return translated.text

    except Exception as e:
        return f"Translation failed: {str(e)}"
