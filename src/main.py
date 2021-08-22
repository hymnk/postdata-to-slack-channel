import sys
from slack_post import slack_post


try:
    if (sys.argv):
        text = sys.argv[1]
except Exception as err:
    raise err


if __name__ == '__main__':
    res = slack_post(text)
    print(res.text)
