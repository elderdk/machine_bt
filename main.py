from translator import trans

from urllib import parse

import json


def back_translate(text: str) -> dict:

    slang, tlang, tr = trans(text)
    back_tr = trans(tr, tlang, slang)

    return {
        "original_text": text,
        "original_translation": tr,
        "back_translation": back_tr,
    }


def handler(event, context):
    
    print(event)
    
    body = json.loads(event['body'])
    
    text = parse.unquote_plus(body['text'])
    
    response = back_translate(text)
    

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
    

if __name__ == "__main__":
    content = handler(
        {"body": '{"text": "this is a test."}'}, {}
        )