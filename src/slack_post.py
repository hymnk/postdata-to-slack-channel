import requests
import json
from slack_settings import SlackSettings

slack_settings = SlackSettings()
webhook_url, post_channel, username, icon_emoji = slack_settings.get_slack_keys()


def slack_post(text):
    payload = {
        "channel": post_channel,
        "username": username,
        "icon_emoji": icon_emoji,
        "text": text
    }

    res = requests.post(webhook_url, data=json.dumps(payload))
    return res
