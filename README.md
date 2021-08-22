# 事前準備

1. Slack -> アプリを管理 -> カスタムインテグレーション からIncoming Webhookを選択
2. [Slackに追加]を選択。投稿先チャンネルを選択してIncoming Webhookインテグレーションの追加を実施
3. 表示されたWebhook URLをメモ。その他の設定は好みでカスタマイズ（投稿名、アイコン等）

# System Requirement
- Python3.8 or higher

# QuickStart
1. Run `$ poetry install`
1. Edit `settings.json.sample` and Rename `settings.json.sample -> settings.json`
1. Enable environment variables for poetry `$ poetry shell`
1. Run `$ python3 ./postdata-to-slack-channel/src/main.py "Text content you want to sent here"`

# TODO
- Write the test code.
- Write the logging code.
