from translator import trans
from lang_handler import check_lang


def back_translate(text: str, slang: str, tlang: str) -> dict:

    check_result = check_lang(slang, tlang)

    if not check_result["okay"]:
        return {"error": check_result["message"]}

    tr = trans(text, slang, tlang)
    back_tr = trans(tr, tlang, slang)

    return {
        "original text": text,
        "original_translation": tr,
        "back_translation": back_tr,
    }


if __name__ == "__main__":
    resp = back_translate("번역할 텍스트", slang="ko", tlang="en")

    if resp["error"]:
        print(resp["error"])
    else:
        print(resp["original_translation"])
        print(resp["back_translation"])
