from google.cloud import translate_v2 as translate
import os
import settings

def translate_text(text, target=settings.TARGET_LANGUAGE, format=settings.GOOGLE_TRANSLATE_FORMAT):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = settings.GOOGLE_CREDENTIALS
    # Translates some text into Spanish
    translate_client = translate.Client()
    #text = text.decode('utf-8')
    #print (text)
    result = translate_client.translate(text, target_language=target, format_=format)
    return result['translatedText']