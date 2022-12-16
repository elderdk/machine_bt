from cred_handler import set_creds
from google.cloud import translate


def trans(text, slang, tlang):
    """Translate the text.

    This is a wrapper for google.cloud translate.
    """
    project_id = set_creds()
    assert project_id
    parent = f"projects/{project_id}"
    client = translate.TranslationServiceClient()

    response = client.translate_text(
        contents=[text],
        source_language_code=slang,
        target_language_code=tlang,
        parent=parent,
    )

    return response.translations[0].translated_text


if __name__ == "__main__":
    pass
