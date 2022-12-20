from translator import trans
from lang_handler import check_lang

from urllib import parse

import json


def back_translate(text: str, slang: str = "ko", tlang: str = "en") -> dict:

    check_result = check_lang(slang, tlang)

    if not check_result["okay"]:
        return {"error": check_result["message"]}

    tr = trans(text, slang, tlang)
    back_tr = trans(tr, tlang, slang)

    return {
        "original_text": text,
        "original_translation": tr,
        "back_translation": back_tr,
    }


def handler(event, context):
    
    text = parse.unquote_plus(event['body'])
    slang = 'ko'
    tlang = 'en'
    
    response = back_translate(text, slang, tlang)
    

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
    

if __name__ == "__main__":
    pass