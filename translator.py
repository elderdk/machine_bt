from cred_handler import set_creds
from google.cloud import translate
from exceptions import TextTooLongError, LanguageCodeUnclearError


def trans(text, slang=None, tlang=None):
    """Translate the text.

    This is a wrapper for google.cloud translate.
    """
    
    # validate text length
    if len(text) > 250:
        raise TextTooLongError("Sorry! The requested text is too long! (Current cap: 250 characters)")
    
    project_id = set_creds()

    parent = f"projects/{project_id}/locations/global"
    client = translate.TranslationServiceClient()

    if not slang:
        slang = client.detect_language(content=text, parent=parent, mime_type="text/plain").languages[0].language_code


        if slang == "ko":
            tlang = "en"
        elif slang == "en":
            tlang = "ko"

    response = client.translate_text(
        contents=[text],
        source_language_code=slang,
        target_language_code=tlang,
        parent=parent,
    )

    return  response.translations[0].translated_text


if __name__ == "__main__":
    resp = trans("테스트 입니다.", "ko", "en")
    print(resp)