import json


class SlackSettings(object):
    def __init__(self):
        with open('settings.json') as f:
            slack_keys = json.load(f)

        self.webhook_url = slack_keys['webhook_url']
        self.post_channel = slack_keys['post_channel']
        self.username = slack_keys['username']
        self.icon_emoji = slack_keys['icon_emoji']

    def get_slack_keys(self):
        return self.webhook_url, self.post_channel, self.username, self.icon_emoji
