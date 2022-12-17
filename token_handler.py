import base64


def deserialzie_token(token: str) -> dict:
    token_list = base64.b64decode(token).decode('utf-8').split('&')
    
    payload = {}
    for i in token_list:
        k, v = i.split('=')
        payload[k] = v
    return payload 

if __name__ == "__main__":
    pass
