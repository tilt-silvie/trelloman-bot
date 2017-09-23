from flask import Flask, request, abort
from slacker import Slacker
import configparser

SETTING_FILE = "settings.cfg"
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        action_type = request.json["action"]["display"]["translationKey"]

        if action_type == "action_move_card_from_list_to_list":
            card_name = request.json["action"]["data"]["card"]["name"]
            before_list = request.json["action"]["data"]["listBefore"]["name"]
            after_list = request.json["action"]["data"]["listAfter"]["name"]
            user_name = request.json["action"]["memberCreator"]["username"]

            message = None

            if before_list == todo_list_name and after_list == doing_list_name:
                # You can modify post message
                # TODO : message format can be defined in config file
                message = user_name + "さんが「" + card_name + "」に取りかかりました。ファイト！"

            elif before_list == doing_list_name and after_list == done_list_name:
                # You can modify post message
                # TODO : message format can be defined in config file
                message = user_name+ "さんが「" + card_name + "」を完了しました。お疲れ様です！"

            if message is not None:
                slack.chat.post_message(channel_name, message, as_user=True)

        return '', 200
    else:
        abort(400)


@app.route("/webhook", methods=["HEAD"])
def webhook_registation():
    if request.method == "HEAD":
        return "", 200
    else:
        abort(400)


if __name__ == '__main__':
    settings = configparser.ConfigParser()
    settings.read(SETTING_FILE, encoding="utf-8")

    port = settings.get("Flask", "port")
    slack_token = settings.get("Slack", "token")
    channel_name = settings.get("Slack", "post_channel")
    todo_list_name = settings.get("Trello", "todo_list_name")
    doing_list_name = settings.get("Trello", "doing_list_name")
    done_list_name = settings.get("Trello", "done_list_name")

    slack = Slacker(slack_token)
    app.run(port=int(port), host="0.0.0.0")
