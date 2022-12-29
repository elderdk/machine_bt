import json
from urllib import parse
from translator import trans
from exceptions import TextTooLongError


def back_translate(text: str) -> dict:

    tr = trans(text)
    back_tr = trans(tr)

    return {
        "original_text": text,
        "original_translation": tr,
        "back_translation": back_tr,
    }


def handler(event, context):
    
    print(event)
    
    body = json.loads(event['body'])
    text = parse.unquote_plus(body['text'])
    
    try:
    
        response = back_translate(text)
    
    except TextTooLongError as err:
        return {
            "statusCode": 502,
            "body": err
        }
    
    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
    

if __name__ == "__main__":
    content = handler(
        {"body": '{"text": "수도권 대표 해돋이 명소는 북한산 백운대다. 일대에서 가장 높은 산답게 날씨만 좋다면 대도시 경치라 믿기 어려운 경이로운 일출을 볼 수 있다. 북한산우이역 2번 출구에서 2.3km를 도로 따라 올라서, 백운대탐방지원센터에서 하루재와 백운대피소를 거쳐 오르는 2.4km 산길이 최단 코스다. 산길만 1시간 30분 정도 걸리므로, 지하철에서 등산로 입구까지 2.3km 찻길은 택시를 타는 것이 합리적이다. 국립공원이라 이정표가 많아 길찾기는 어렵지 않지만, 초행이라면 야간산행 특성상 갈림길을 만날 때마다 주의해서 살펴야 한다. 암릉 구간이 있어 쇠난간을 붙잡아야 하므로, 장갑 필수. 2023년 1월 1일 서울 강북구의 일출 시간은 7시 47분이며, 여명이 20여 분 전부터 밝아오는 걸 감안하면 7시 30분까지는 백운대에 도착해야 한다. 첫차신설동역(1호선·2호선·우이신설경전철)에서 오전 5시30분에 첫차가 있으며 북한산우이역까지 23분 걸린다. 성신여대입구(4호선·우이신설경전철)에서 오전 5시34분에 첫차가 있으며 북한산우이역까지 18분 걸린다."}'}, {}
        )
    
    print(content)
