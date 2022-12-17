import base64
from typing import Union

def deserialzie_token(token: Union[str, bytes]) -> dict:
    
    if type(token) == 'bytes':
        token_list = base64.b64decode(token).decode('utf-8').split('&')
    else:
        token_list = token.split('&')
    
    payload = {}
    for i in token_list:
        k, v = i.split('=')
        payload[k] = v
    return payload 

if __name__ == "__main__":
    pass
