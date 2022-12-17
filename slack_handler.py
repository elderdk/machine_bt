def get_block(response):

    otxt = response["original_text"]
    otr = response["original_translation"]
    btr = response["back_translation"]

    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Please see below for machine back translation of your original text.\n\n",
            },
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"*Original Text*\n\n{otxt}"},
        },
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"*Original Translation*\n\n{otr}"},
        },
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"*Back Translation*\n\n{btr}"},
        },
        {"type": "divider"},
    ]
