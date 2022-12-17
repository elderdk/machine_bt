from translator import trans
from lang_handler import check_lang
from token_handler import deserialzie_token
from urllib import parse
from slack_handler import get_block


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
    
    # tokens = deserialzie_token(unquote(event["body"], encoding='utf-8'))
    tokens = deserialzie_token(parse.unquote_plus(event['body']))
    text = tokens['text']
    slang = 'ko'
    tlang = 'en'
    
    response = back_translate(text, slang, tlang)
    
    block = get_block(response)
    print(block)
    return {
        'statusCode': 200,
        'body': block
    }
    

if __name__ == "__main__":
    pass
